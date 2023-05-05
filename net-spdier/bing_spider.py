# coding: utf-8
import requests
# import random
import pandas as pd

headersPool = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"]


def search_word():
    from urllib import parse
    text = open('keyword.txt', 'r', encoding='utf-8').read().split('\n')
    new_list = []
    for i in text:
        if i.isalpha() == False:
            new = i.replace(' ', '+')
        else:
            new = parse.quote(i)
        new_list.append(new)
    return new_list, text

def get_back(list1):
    news_list = []
    for li in list1:
        if li not in news_list:
            news_list.append(li)
    return news_list

def bing_search(keywords):
    from lxml import etree
    from time import sleep
    from bs4 import BeautifulSoup
    start = 0
    first = 1
    error = 0
    record = 0
    all_list = []
    # ua = random.choice(headersPool)
    ua = headersPool[0]
    headers = {
        "User-Agent": ua,
    }
    res = requests.get('https://cn.bing.com/', headers=headers)
    cookies = dict(res.cookies.get_dict())
    while True:
        while True:
            if start == 0:
                if '%' in keywords:
                    new_from = 'QBLHCN'
                else:
                    new_from = 'QBLH'
                # https://cn.bing.com/search?q={keywords}&qs=HS&sc=2-0&FORM=BESBTB&sp=1&ensearch=1
                urls = f'https://cn.bing.com/search?q={keywords}&qs=n&FORM={new_from}&sp=-1'
                # urls = f'https://cn.bing.com/search?q={keywords}&sp=-1'
            else:
                first = first + one_count
                if start == 1:
                    froms = 'PERE'
                else:
                    froms = f'PERE{start-1}'
                #https://cn.bing.com/search?q={keywords}&qs=HS&sp=1&ensearch=1&first={first}&FORM={froms}
                urls = f'https://cn.bing.com/search?q={keywords}&qs=n&sp=-1&first={first}&FORM={froms}'
            sleep(3.5)
            res = requests.get(urls, headers=headers, cookies=cookies)
            tree = etree.HTML(res.text)
            li_list = tree.xpath('//ol[@id="b_results"]/li[@class="b_algo"]')
            one_count = len(li_list)
            headers.update(
                {"referer": urls, 'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
                 'sec-ch-ua-arch': '"x86"',
                 'sec-ch-ua-bitness': '"64"',
                 'sec-ch-ua-full-version': '"94.0.992.38"',
                 'sec-ch-ua-mobile': '?0',
                 'sec-ch-ua-model': '""',
                 'sec-ch-ua-platform': '"Windows"',
                 'sec-ch-ua-platform-version': '"10.0.0"',
                 'sec-fetch-dest': 'document',
                 'sec-fetch-mode': 'navigate',
                 'sec-fetch-site': 'same-origin',
                 'sec-fetch-user': '?1',
                 'upgrade-insecure-requests': '1',
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
                 })
            if one_count == 0:
                error += 1
                continue
            else:
                start += 1
                error = 0
                break
        if error >= 10:
            print("多次未出结果，爬取词条数量达到最大")
            break
        else:
            for i in li_list:
                html_text = etree.tostring(i).decode('utf-8')
                soup = BeautifulSoup(html_text, 'lxml')
                try:
                    url = i.xpath('.//h2/a/@href')[0]
                    title = soup.find('h2').a.get_text()
                except:
                    url = ""
                    title = ""
                some = soup.find('p')
                if some != None:
                    data = title, url, some.get_text()
                else:
                    data = title, url, ""
                print('爬取显示：', data)
                all_list.append(data)
            all_list = get_back(all_list)
            print(len(all_list))
            if len(all_list) >= nums:
                return all_list
            elif record == len(all_list):
                return all_list
            else:
                record = len(all_list)




if __name__ == '__main__':
    input_some = input("输入每个关键词爬取的数量：")
    if input_some == "":
        nums = 100  # 默认每个关键词爬取数量
    else:
        nums = int(input_some)
    print("读取关键词=====")
    back_list, sheet_names = search_word()
    if back_list ==[]:
        print("未读取到关键词=====")
    write_list = []
    for keys in back_list:
        print("爬取关键词:",keys)
        news = bing_search(keys)
        write_list.append(news)
    writer = pd.ExcelWriter('test.xlsx', engin='openpyxl')
    count = 0
    for words in write_list:
        count += 1
        df = pd.DataFrame(words, columns=['标题', '链接', '摘要'])
        df.to_excel(excel_writer=writer, sheet_name=str(count), encoding="utf-8", index=False)
    writer.save()
    print("保存成功")
    writer.close()
