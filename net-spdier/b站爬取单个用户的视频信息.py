import requests
from lxml import etree
import re
from time import sleep
import pandas as pd


def find_space(pages):
    import math
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    if pages == 0:
        headerss = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            'referer': 'https://space.bilibili.com/'
        }
        res = requests.get("需要爬取的链接",
                           headers=headerss)
        page = math.ceil(int(re.search(r'"video":(.*?),', res.text).group(1)) / 30)
        start = 1
        end = page + 1
    else:
        start = int(pages[0])
        end = int(pages[1]) + 1
    data_list = []
    for i in range(start, end):
        sleep(3)
        url = "爬取的页数的链接"
        try:
            res = requests.get(url, headers=headers).json()
            v_list = res['data']['list']['vlist']
            for n in v_list:
                com = n['comment']
                leng = n['length']
                bv = n['bvid']
                data = bv, leng, com
                data_list.append(data)
            print(f"已经提取{len(data_list)}个视频链接")
        except Exception as e:
            print(f"Error:{e}")
            return data_list
    return data_list


def bv_content(bv_id, length, comms):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    # https://space.bilibili.com/
    url = f"https://www.bilibili.com/video/{bv_id}"
    try:
        res = requests.get(url, headers=headers)
    except Exception as e:
        print(f"Error:{e}")
        return all_list
    tree = etree.HTML(res.text)
    title = ""
    data_time = ""
    try:
        data_time = tree.xpath('//div[@class="video-data"]/span[3]/text()')[0]
        title = tree.xpath('//h1[@class="video-title"]/@title')[0]
    except Exception as e:
        print(f"Error:{e}")
    try:
        pattern = '"view":(.*?),"danmaku":(.*?),"reply":(.*?),"favorite":(.*?),"coin":(.*?),"share":(.*?),"now_rank":.*?,"his_rank":.*?,"like":(.*?),'
        data = re.search(pattern, res.text).groups()  # 播放数，弹幕，评论，收藏，投币，分享，点赞
    except Exception as e:
        print(f"Error:{e}")
        try:
            play_count = tree.xpath('//div[@class="video-data"]/span[@class="view"]/@title')[0].replace("总播放数", "")
            dm_count = tree.xpath('//div[@class="video-data"]/span[@class="dm"]/@title')[0].replace("历史累计弹幕数", "")
            like = tree.xpath('//span[@class="like"]/@title')[0].replace("点赞数", "")
            coin = tree.xpath('//span[@class="coin"]/@title')[0].replace("投硬币枚数", "")
            collect = tree.xpath('//span[@class="collect"]/@title')[0].replace("收藏人数", "")
            share = tree.xpath('//span[@class="share"]/text()')[0].replace("\n", "").strip()
            data = play_count, dm_count, collect, coin, share, like
        except Exception as e:
            print(f"Error:{e}")
            data = []
    if data == []:
        return []
    else:
        data = list(data)
        if len(data) < 7:
            data.insert(2, comms)
        data.insert(0, url)
        data.insert(1, title)
        data.insert(2, data_time)
        data.insert(3, length)
        return tuple(data)


if __name__ == '__main__':
    # bv_content("test")
    files = input("输入保存文件名（留空为默认文件名）")
    if files == "":
        files = "默认文件名"
    input_page = input("输入要提取的页数（例：1-30）：")
    page1 = ""
    if input_page == "":
        page1 = 0
    else:
        if input_page.find("-") != -1:
            page1 = input_page.split("-")
    back = find_space(page1)
    all_list = []
    for b in back:
        bv = b[0]
        length = b[1]
        coms = b[2]
        datas = bv_content(bv, length, coms)
        if datas:
            all_list.append(datas)
            print(f"已经提取{len(all_list)}个视频数据")
            sleep(3)
        else:
            print("Error:数据信息无法提取出来")
    print("爬取完成，开始保存")
    df = pd.DataFrame(all_list)
    df.to_excel(files, index=False,
                header=["视频链接", "视频标题", "视频投稿时间", "视频时长", "播放数", "弹幕数", "评论数", "收藏", "投币", "分享", "点赞"])
