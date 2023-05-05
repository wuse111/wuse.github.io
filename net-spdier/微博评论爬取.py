# coding: utf-8
# Author：
# Tool ：PyCharm
import requests
import pandas as pd
from time import sleep
import random

#随机使用手机user-agent
USE_AGENT = [
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN",
    "Mozilla/5.0 (Linux; Android 10; CDY-AN90 Build/HUAWEICDY-AN90; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200801 Mobile Safari/537.36 MMWEBID/4006 MicroMessenger/7.0.18.1740(0x2700123B) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
]

#获取评论函数
def get_weibocom(mid, cookie):
    headers = {
        "User-Agent": random.choices(USE_AGENT)[0],
        "Content-Type": "application/x-www-form-urlencoded",
        # "x-requested-with": "XMLHttpRequest",
    }
    cookies = {
        "cookie": cookie
    }
    #更新最新cookie
    res = requests.get(f"https://m.weibo.cn/detail/{mid}", headers=headers, cookies=cookies)
    cookie_dict = res.cookies.get_dict()
    #提取cookie并更新
    cookie_dict[cookie.split("=")[0]] = cookie.split("=")[1].replace(";", '')
    headers['x-xsrf-token'] = cookie_dict['XSRF-TOKEN']
    #设定header的来源
    headers["referer"] = f"https://m.weibo.cn/detail/{mid}"
    print(headers)
    com_list = []
    count = 0
    try:
        new = open("log.txt", 'r', encoding="utf-8").read().split("|")
        max_id = new[0]
        max_id_type = new[1]
        count += 1
    except:
        max_id_type = "0"
    #设置错误值
    error = 0
    while True:
        #设定延时
        sleep(5)
        if count == 0:
            url = f'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id_type={max_id_type}'
        else:
            url = f'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id={max_id}&max_id_type={max_id_type}'
        count += 1
        #错误次数大于10次或多次进行退出
        if error > 10:
            f = open("log.txt", "w", encoding="utf-8")
            f.write(f"{max_id}|{max_id_type}")
            f.close()
            print("error:多次报错")
            return com_list
        try:
            #设定重连次数
            requests.adapters.DEFAULT_RETRIES = 5
            #不保持长时间连接
            requests.keep_alive = False
            res = requests.get(url, headers=headers, cookies=cookie_dict)
            res = res.json()
            print(res)
        except Exception as e:
            #访问网页出现错误提示跳转
            print(f'错误情况:{e}')
            #尝试更新ua
            headers["User-Agent"] = random.choices(USE_AGENT)[0]
            error += 1
        else:
            print(f"爬取第{count}页的评论")
            try:
                #提取每次的max_id和max_id_type
                max_id = res['data']['max_id']
                max_id_type = res['data']['max_id_type']
                com_data = res['data']['data']
            except Exception as e:
                print(f'错误情况:{e}')
                headers["User-Agent"] = random.choices(USE_AGENT)[0]
                error += 1
            else:
                for com in com_data:
                    #提取评论文本
                    com_text = com['text']
                    #提取用户名
                    user_name = com['user']['screen_name']
                    #提取用户id
                    user_id = com['user']['id']
                    #提取用户下回复数
                    f_comment = com['comments']
                    #元组保存数据
                    data = str(user_id), user_name, com_text
                    com_list.append(data)
                    if f_comment != False:
                        for fs in f_comment:
                            f_com = fs['text']
                            f_user = fs['user']['screen_name']
                            f_user_id = com['user']['id']
                            data = str(f_user_id), f_user, f_com
                            com_list.append(data)
                print(f"已经爬取{len(com_list)}条数据")
                #指定提取数据的数量
                # if len(com_list) >= 1000:
                #     return com_list
                #max_id为0的时候数据获取不了
                if max_id == 0:
                    return com_list
                else:
                    max_id = str(max_id)


if __name__ == '__main__':
    #存在sub的cookie
    the_cookie = 'SUB=_2A25PaKQPDeRhGeFI61AU8C_FwzmIHXVsksxHrDV6PUJbkdAKLRbRkW1NfWXCZJZFjSBV1gcqonS9e7JFZDyWwmlU;'
    back = get_weibocom('4750364861792281', the_cookie)
    df = pd.DataFrame(back, columns=["用户ID", "用户昵称", "评论文本"])
    # 张文宏微博评论保存csv
    df.to_csv("张文宏微博评论.csv", index=False, encoding="utf_8_sig")
    #txt文件保存
    file = open("评论文本.txt", 'w', encoding='utf-8')
    for i in back:
        file.write(i[2] + '\n')
    file.close()
