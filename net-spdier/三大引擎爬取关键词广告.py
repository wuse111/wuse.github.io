# coding: utf-8
# Author：戏不能停啊
# Date ：2020/11/21 16:31
# Tool ：PyCharm
import requests
from time import sleep
import random

def baidu_(keyword):
    import re
    headers = {
        "User-Agent": random.choice(headersPool),
        "Connection": "close"
    }
    b_cookie = {}
    link_list = []
    count = 0
    cookie = ""
    new_ip = ""
    ips_ = {}
    some_last = 0
    while True:
        error = 0
        if b_cookie == {}:
            ips_ = {
                "https": "https://" + input_ip
            }
            try:
                res = requests.get("https://www.baidu.com/", headers=headers, proxies=ips_, timeout=15)
                b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                all_t = ''
                for key, value in b_cookie.items():
                    all_t = all_t + key + '=' + value + ';'
                cookie = all_t
            except Exception as e:
                some_last += 1
                print(f"百度错误:{e}")
                error = 1
                ip_block.append(input_ip)
        elif new_ip != " ":
            if error == 1:
                ips_ = {
                    "https": "https://" + new_ip
                }
                try:
                    res = requests.get("https://www.baidu.com/", headers=headers, proxies=ips_, timeout=15)
                    b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                    all_t = ''
                    for key, value in b_cookie.items():
                        all_t = all_t + key + '=' + value + ';'
                    cookie = all_t
                except Exception as e:
                    some_last += 1
                    print(f"百度错误:{e}")
                    error = 1
                    ip_block.append(new_ip)
        if error == 0:
            some_last = 0
            headers = headers.copy()
            headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9"})

            if count == 0:
                param = {
                    "ie": "UTF-8",
                    "wd": keyword
                }
            else:
                param = {
                    "wd": keyword,
                    "pn": count * 10,
                    "oq": keyword
                }
            sleep(5)
            res = ""
            headers.update({"cookie": cookie})
            try:
                res = requests.get("http://www.baidu.com/s", params=param, headers=headers, proxies=ips_, timeout=15)
                res.encoding = 'utf-8'
                if "百度安全验证" in res.text:
                    error = 1
                else:
                    alls = re.findall(re.compile(r'data-landurl="(.*?)"'), res.text)
                    new_list = deal_list(alls)
                    link_list.extend(new_list)
                    print("百度", link_list)
                    print("error", error)
            except Exception as e:
                some_last += 1
                print(f"错误:{e}")
                error = 1
        if some_last >= 5:
            if len(link_list) == 0:
                return [" ", " ", " ", " ", " "]
            else:
                s = 5 - len(link_list)
                if s == 0:
                    return link_list
                else:
                    for i in range(s):
                        link_list.append(" ")
                    return link_list
        error_count = 0
        if error == 1:
            while True:
                sleep(1.5)
                name_back = get_ip(input_name)
                if name_back != "":
                    new_ip = name_back
                    break
                else:
                    error_count += 1
                if error_count >= 8:
                    if len(link_list) == 0:
                        return [" ", " ", " ", " ", " "]
                    else:
                        s = 5 - len(link_list)
                        if s == 0:
                            return link_list
                        else:
                            for i in range(s):
                                link_list.append(" ")
                            return link_list
        else:
            if len(link_list) < 5:
                count += 1
            elif len(link_list) > 5:
                s = len(link_list) - 5
                if s == 1:
                    new = len(link_list) - 1
                    del link_list[new]
                else:
                    for ss in range(s):
                        new = len(link_list) - (ss + 1)
                        del link_list[new]
                return link_list
            elif len(link_list) == 5:
                return link_list
            if count >= 5:
                if len(link_list) == 0:
                    return [" ", " ", " ", " ", " "]
                else:
                    s = 5 - len(link_list)
                    if s == 0:
                        return link_list
                    else:
                        for i in range(s):
                            link_list.append(" ")
                        return link_list

def third_six(keyword):
    #https://www.so.com/s?ie=utf-8&q=epic
    #https://www.so.com/s?q=epic&pn=2
    import re
    headers = {
        "User-Agent": random.choice(headersPool),
        "Connection": "close"
    }
    b_cookie = {}
    cookie = ""
    new_ip = ""
    ips_ = {}
    link_list = []
    # cookies = open("360_cookies.txt", "r").read().replace("\n", "")
    # cookie = cookie + cookies
    count = 1
    some_last = 0
    while True:
        error = 0
        if b_cookie == {}:
            ips_ = {
                "https": "https://" + input_ip
            }
            try:
                res = requests.get("https://www.so.com/", headers=headers, proxies=ips_, timeout=15)
                b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                all_t = ''
                for key, value in b_cookie.items():
                    all_t = all_t + key + '=' + value + ';'
                cookie = all_t
            except Exception as e:
                print(f"错误:{e}")
                some_last += 1
                error = 1
                ip_block.append(input_ip)
        elif new_ip != " ":
            if error == 1:
                ips_ = {
                    "https": "https://" + new_ip
                }
                try:
                    res = requests.get("https://www.so.com/", headers=headers, proxies=ips_, timeout=15)
                    b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                    all_t = ''
                    for key, value in b_cookie.items():
                        all_t = all_t + key + '=' + value + ';'
                    cookie = all_t
                except Exception as e:
                    print(f"错误:{e}")
                    some_last += 1
                    error = 1
                    ip_block.append(new_ip)
        if error == 0:
            some_last = 0
            if count == 1:
                param = {
                    "ie": "utf-8",
                    "q": keyword
                }
            else:
                param = {
                    "q": keyword,
                    "pn": count
                }
            sleep(5)
            res = ""
            headers.update({"cookie":cookie})
            try:
                res = requests.get("https://www.so.com/s", params=param, headers=headers, proxies=ips_, timeout=15)
                if "系统检测到您操作" in res.text:
                    error = 1
                else:
                    new_list = re.findall(re.compile(r'e-landurl="(.*?)"'), res.text)
                    link_list.extend(deal_list(new_list))
                    link_list = deal_list(link_list)
                    print("360", link_list)
                    print("error", error)
            except Exception as e:
                some_last += 1
                print(f"错误:{e}")
                error = 1
        if some_last >= 5:
            if len(link_list) == 0:
                return [" ", " ", " ", " ", " "]
            else:
                s = 5 - len(link_list)
                if s == 0:
                    return link_list
                else:
                    for i in range(s):
                        link_list.append(" ")
                    return link_list
        error_count = 0
        if error == 1:
            while True:
                sleep(1.5)
                name_back = get_ip(input_name)
                if name_back != "":
                    new_ip = name_back
                    break
                else:
                    error_count += 1
                if error_count >= 8:
                    if len(link_list) == 0:
                        return [" ", " ", " ", " ", " "]
                    else:
                        s = 5 - len(link_list)
                        if s == 0:
                            return link_list
                        else:
                            for i in range(s):
                                link_list.append(" ")
                            return link_list
        else:
            if len(link_list) < 5:
                count += 1
            elif len(link_list) == 5:
                return link_list
            elif len(link_list) > 5:
                s = len(link_list) - 5
                if s == 1:
                    new = len(link_list) - 1
                    del link_list[new]
                else:
                    for ss in range(s):
                        new = len(link_list) - (ss + 1)
                        del link_list[new]
                return link_list
            if count >= 5:
                if len(link_list) == 0:
                    return [" ", " ", " ", " ", " "]
                else:
                    s = 5 - len(link_list)
                    if s == 0:
                        return link_list
                    else:
                        for i in range(s):
                            link_list.append(" ")
                        return link_list

def sougo(keyword):
    import re
    from bs4 import BeautifulSoup
    #https://www.sogou.com/sogou?query=epic
    headers = {
        "User-Agent": random.choice(headersPool),
        "Connection": "close"
    }
    b_cookie = {}
    cookie = ""
    new_ip = ""
    ips_ = {}
    new_list = []
    link_list = []
    count = 1
    some_last = 0
    while True:
        error = 0
        if b_cookie == {}:
            ips_ = {
                "https": "https://" + input_ip
            }
            try:
                res = requests.get("https://www.sogou.com/", headers=headers, proxies=ips_, timeout=15)
                b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                all_t = ''
                for key, value in b_cookie.items():
                    all_t = all_t + key + '=' + value + ';'
                cookie = all_t
            except Exception as e:
                some_last += 1
                print(f"错误:{e}")
                error = 1
                ip_block.append(input_ip)
        elif new_ip != " ":
            if error == 1:
                ips_ = {
                    "https": "https://" + new_ip
                }
                try:
                    res = requests.get("https://www.sogou.com/", headers=headers, proxies=ips_, timeout=15)
                    b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
                    all_t = ''
                    for key, value in b_cookie.items():
                        all_t = all_t + key + '=' + value + ';'
                    cookie = all_t
                except Exception as e:
                    some_last += 1
                    print(f"错误:{e}")
                    error = 1
                    ip_block.append(new_ip)
        if error == 0:
            some_last = 0
            if count == 1:
                param = {
                    "query": keyword
                }
            else:
                #query=epic&page=2&ie=utf8
                param = {
                    "query": keyword,
                    "page": count,
                    "ie": "utf8"
                }
            sleep(5)
            res = ""
            headers.update({"cookie": cookie})
            try:
                res = requests.get("https://www.sogou.com/sogou", params=param, headers=headers,proxies=ips_, timeout=15)
                if "您的访问过于频繁" in res.text:
                    error = 1
                else:
                    soup = BeautifulSoup(res.text, 'html.parser')
                    alls = soup.find_all("h3", class_="biz_title")
                    for ace in alls:
                        a_link = ace.a['href']
                        sleep(1.5)
                        res = requests.get(a_link, headers=headers)
                        try:
                            new = re.search(re.compile(r"window.location.href='(.*?)'"), res.text).group(1)
                            new_list.append(new)
                        except:
                            new = re.search(re.compile(r"content='0; url=(.*?)'"), res.text).group(1)
                            new_list.append(new)
                        finally:
                            continue
                    link_list.extend(deal_list(new_list))
                    link_list = deal_list(link_list)
                    print("搜狗", link_list)
                    print("error", error)
            except Exception as e:
                some_last += 1
                print(f"错误:{e}")
                error = 1
        if some_last >= 5:
            if len(link_list) == 0:
                return [" ", " ", " ", " ", " "]
            else:
                s = 5 - len(link_list)
                if s == 0:
                    return link_list
                else:
                    for i in range(s):
                        link_list.append(" ")
                    return link_list
        error_count = 0
        if error == 1:
            while True:
                sleep(1.5)
                name_back = get_ip(input_name)
                if name_back != "":
                    new_ip = name_back
                    break
                else:
                    error_count += 1
                if error_count >= 8:
                    if len(link_list) == 0:
                        return [" ", " ", " ", " ", " "]
                    else:
                        s = 5 - len(link_list)
                        if s == 0:
                            return link_list
                        else:
                            for i in range(s):
                                link_list.append(" ")
                            return link_list
        if len(link_list) == 5:
            return link_list
        elif len(link_list) > 5:
            s = len(link_list) - 5
            if s == 1:
                new = len(link_list) - 1
                del link_list[new]
            else:
                for ss in range(s):
                    new = len(link_list) - (ss + 1)
                    del link_list[new]
            return link_list
        else:
            count += 1
        if count >= 5:
            if len(link_list) == 0:
                return [" ", " ", " ", " ", " "]
            else:
                s = 5 - len(link_list)
                if s == 0:
                    return link_list
                else:
                    for i in range(s):
                        link_list.append(" ")

                    return link_list

def get_ip(name):
    ares_code = ["110000", "440000,441900", "440000,440700", "310000"]  #北  广东莞   广东江  上
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    #http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro={code}&city=0&yys=0&port=11&pack=128908&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=
    # code = " "
    # city = " "
    if name == "北京":
        code = ares_code[0]
        city = "0"
    elif "广东" in name:
        if "东莞" in name:
            code = ares_code[1].split(",")[0]
            city = ares_code[1].split(",")[1]
        else:
            code = ares_code[2].split(",")[0]
            city = ares_code[2].split(",")[1]
    else:
        code = ares_code[3]
        city = "0"
    print(code, city)
    #http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro={code}&city={city}&yys=0&port=11&pack=128908&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=
    #http://http.tiqu.letecs.com/getip3?num=1&type=1&pro={code}&city={city}&yys=0&port=11&pack=128908&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions=
    while True:
        url = f"http://http.tiqu.letecs.com/getip3?num=1&type=1&pro={code}&city={city}&yys=0&port=11&pack=128908&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions=&gm=4"
        res = requests.get(url, headers=headers).text.replace("\n", "").strip()
        print(res)
        if res in ip_block:
            sleep(1.5)
            continue
        elif ":" not in res:
            print(f"提取出现问题：{res}")
            return " "
        else:
            return res

def check_ip1():
    from lxml import etree
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    res = requests.get("https://202020.ip138.com/", headers=headers).text
    selector = etree.HTML(res)
    #/html/body/p[1]/text()[2]
    ip = selector.xpath('//p[@align="center"]/text()[2]')
    s = str(ip[0]).replace("\r\n", "").replace("] ", "").replace("来自：", "")
    return s

def check_ip(ips):
    from lxml import etree
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    ips_ = {
        "https": "https://" + ips
    }
    try:
        res = requests.get("https://2021.ip138.com/", headers=headers, proxies=ips_, timeout=15).text
        selector = etree.HTML(res)
        # /html/body/p[1]/text()[2]
        ip = selector.xpath('//p[@align="center"]/text()[2]')
        s = str(ip[0]).replace("\r\n", "").replace("] ", "").replace("来自：", "")
        return s
    except Exception as e:
        return "该ip无法使用"


def deal_list(list1):
    new = []
    for i in list1:
        if i not in new:
            new.append(i)
    return new

def to_excels(data,ares):
    import xlwt
    save_book = xlwt.Workbook(encoding='utf-8')
    save_sheet = save_book.add_sheet(ares)
    names = []
    number = len(data)
    names.append("游戏/词")
    for num in range(5):
        names.append(f"{ares}{num + 1}")
    names.append("搜索渠道")
    for i in range(0, len(names)):
        save_sheet.write(0, i, names[i])
    for i in range(0, number):
        writer = data[i]
        for j in range(0, len(names)):
            for key, value in writer[0].items():
                keys = key
                values = value
            if j == 0:
                save_sheet.write(i + 1, j, keys)
            if j == 1:
                for s in range(0, len(values)):
                    print(j + s, values[s - 1])
                    save_sheet.write(i + 1, j + s, values[s - 1])
            elif j == 6:
                save_sheet.write(i + 1, j, writer[1])
            else:
                continue
    save_book.save(f"{ares}链接.xls")
    print('保存完成')

def first():
    baidu_dict = {}
    new = []
    print("进入百度爬取")
    back = baidu_(fs)
    baidu_dict[fs] = back
    new.append(baidu_dict)
    new.append("百度")
    baidu_list.append(new)
    print("百度出来了")
def second():
    ts_dict = {}
    new = []
    print("进入360爬取")
    back1 = third_six(fs)
    ts_dict[fs] = back1
    new.append(ts_dict)
    new.append("360")
    ts_list.append(new)
    print("360出来了")
def third():
    sogo_dict = {}
    new = []
    print("进入搜狗爬取")
    back2 = sougo(fs)
    sogo_dict[fs] = back2
    new.append(sogo_dict)
    new.append("搜狗")
    sogo_list.append(new)
    print("搜狗出来了")






def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    import ctypes
    import inspect
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    headersPool = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
        "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"]
    from threading import Thread
    ip_block = []
    #修改为测试代理
    input_ip = " "
    input_name = input("输入地址：").strip()
    # ip_list = open("input_ip.txt", 'r', encoding="utf-8").readlines()
    # ip_list = [str(n).replace("\n", "") for n in ip_list]
    while True:
        ip_back = get_ip(input_name)
        if ip_back == " ":
            continue
        else:
            input_ip = ip_back
            ares = check_ip(input_ip)
            if ares == "该ip无法使用":
                print(ares)
            else:
                print(f"ip地址为{ares}")
                break
    f_list = open("search_keyword.txt", 'r', encoding="utf-8").readlines()
    f_list = [str(n).replace("\n", "") for n in f_list]
    #360的反爬和搜狗的反爬
    all_list = []
    baidu_list = []
    ts_list = []
    sogo_list = []
    for fs in f_list:
        print(f"爬取词语:{fs}")
        sleep(1.5)
        # first()
        # second()
        # third()
        t1 = Thread(target=first)
        t2 = Thread(target=second)
        t3 = Thread(target=third)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        if t1.is_alive() == True:
            stop_thread(t1)
        if t2.is_alive() == True:
            stop_thread(t2)
        if t3.is_alive() == True:
            stop_thread(t3)
    all_list.extend(baidu_list)
    all_list.extend(ts_list)
    all_list.extend(sogo_list)
    to_excels(all_list, input_name)
