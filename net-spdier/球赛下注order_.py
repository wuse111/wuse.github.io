import requests
from time import sleep
class Soccer:
    def __init__(self):
        self.phone_headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36"}
        self.de_user = self.phone_headers.copy()
        self.user_ag = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        self.de = self.user_ag.copy()

    def login(self, username, password):
        sleep(5)
        res = requests.get("https://m1.tg6000.net/", headers=self.phone_headers, allow_redirects=False)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        all_t = ''
        for key, value in cookie.items():
            all_t = all_t + key + '=' + value + ';'
        cookie = all_t
        self.phone_headers.update({"cookie": cookie})
        res = requests.get("https://m1.tg6000.net/login.php", headers=self.phone_headers)
        b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        for key, value in b_cookie.items():
            all_t = all_t + key + '=' + value + ';'
        cookie = all_t
        # print(cookie)
        data = {
            'account': username,
            'pwd': password
        }
        self.phone_headers.update({"cookie": cookie,
                                   "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                   "x-requested-with": "XMLHttpRequest"})
        res = requests.post("https://m1.tg6000.net/other/login.php", data=data, headers=self.phone_headers)
        s_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        all_t = ''
        for key, value in s_cookie.items():
            all_t = all_t + key + '=' + value + ';'
        s_cookie = all_t
        print(cookie)
        return cookie

    def get_tg(self, cookie):
        import re
        from lxml import etree
        # res = requests.get("https://m1.tg6000.net/", headers=self.phone_headers, allow_redirects=False)
        # cookie = requests.utils.dict_from_cookiejar(res.cookies)
        # all_t = ''
        # for key, value in cookie.items():
        #     all_t = all_t + key + '=' + value + ';'
        # cookie = all_t
        # self.phone_headers.update({"cookie": cookie})
        # res = requests.get("https://m1.tg6000.net/login.php", headers=self.phone_headers)
        # b_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        # for key, value in b_cookie.items():
        #     all_t = all_t + key + '=' + value + ';'
        # cookie = all_t
        # data = {
        #     'account': username,
        #     'pwd': password
        # }
        # sleep(2)
        # self.phone_headers.update({"cookie": cookie,
        #                            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        #                            "x-requested-with": "XMLHttpRequest"})
        # res = requests.post("https://m1.tg6000.net/other/login.php", data=data, headers=self.phone_headers)
        self.phone_headers = self.de_user
        self.phone_headers.update({"cookie": cookie})
        while True:
            res = requests.get("https://m1.tg6000.net/market.php", headers=self.phone_headers).text
            tree = etree.HTML(res)
            li_list = tree.xpath('//ul[@class="game_list"]/li')
            ok_list = []
            new_ok = []
            for li in li_list:
                some = str(li.xpath('./@onclick')[0]).replace("listmrketorder", "").replace("(", "").replace(")", "")
                new = re.findall(re.compile("'(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)'"), some)[0]
                if new[5] == "1":
                    ok_list.append(new)
            if len(ok_list) == 0:
                sleep(5)
            else:
                for i in ok_list:
                    if i not in new_ok:
                        new_ok.append(i)
                return new_ok
        # print(f"一共找到保本{len(new_ok)}个")

    def deal_time(self, some):
        import time
        current_milli_time = lambda: int(round(time.time() * 1000))
        now_time = current_milli_time()
        timeArray = time.strptime(some, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        milli_time = lambda: int(round(timeStamp * 1000))
        tomorrow_start_time = milli_time()
        if now_time <= tomorrow_start_time:
            return False
        else:
            return True
    def order_money(self, new_ok, cookies, who_):
        import re
        from lxml import etree
        requests.packages.urllib3.disable_warnings()
        if len(new_ok) == 0:
            return "保本结束"
        # for iss in new_ok:
        iss = new_ok[who_]
        url = 'https://m1.tg6000.net/marketorder.php'
        param = {
            'gc12': iss[0],
            'gameid': iss[1],
            'time': iss[2],
            'name': iss[3],
            'competitionname': iss[4],
            'status_id': iss[5]
        }
        self.phone_headers = self.de_user
        self.phone_headers.update({"cookie": cookies})
        res = requests.get(url, params=param, headers=self.phone_headers, verify=False).text
        print(res)
        selector = etree.HTML(res)
        money = str(selector.xpath('//div[@class="money"]/span/text()')[0]).replace(",", "")
        if money == "0.00":
            return "没钱了"
        div_list = selector.xpath('//div[@class="content_row"]')
        somes = ''
        do_money = ''
        for div in div_list:
            somes = div.xpath('./@onclick')[0].replace("moveorder", "").replace("(", "").replace(")", "")
            ok_if = div.xpath('./div[@class="content_cell table_option"]/span/@style')[0]
            if 'block' in ok_if:
                try:
                    do_money = str(
                        div.xpath('./div[@class="content_cell table_trade table_trade_align"]/text()')[
                            0]).replace(
                        "￥",
                        "").replace(",", "")
                    print(f"提取到额度{do_money}")
                    break
                except IndexError:
                    break
            else:
                continue
        try:
            news = re.findall(re.compile(
                "'(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','','(.*?)','','(.*?)','(.*?)','','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)','(.*?)'"),
                somes)[0]
            print(f"读取{news[4]}的点数")
        except:
            return "继续"
        if news[7] and news[8] != '':
            print("出现点数，准备下单")
            # https://m1.tg5000.net/order.php
            if float(money) <= int(do_money):
                order_money = money
            else:
                order_money = do_money
            data = {
                'c2betorder[0][selectname]': news[0],
                'c2betorder[0][time]': news[1],
                'c2betorder[0][gameid]': news[2],
                'c2betorder[0][markettype]': news[3],
                'c2betorder[0][gamename]': news[4],
                'c2betorder[0][marketname]': news[6],
                'c2betorder[0][Rate]': news[7],
                'c2betorder[0][Bet]': '',
                'c2betorder[0][BetType]': 'L',
                'c2betorder[0][MarketId]': news[5],
                'c2betorder[0][SelectionId]': news[10],
                'c2betorder[0][betfairori]': '',
                'c2betorder[0][percent]': news[11],
                'c2betorder[0][chk]': 'order',
                'c2betorder[0][category]': news[12],
                'c2betorder[0][selectrateL1]': news[8],
                'c2betorder[0][sel]': '',
                'c2betorder[0][gc12]': news[9],
                'c2betorder[0][pawben]': news[13],
                'c2betorder[0][selectmoneyL1]': news[14],
                'c2betorder[0][activity_icon_val]': news[17]
            }
            self.phone_headers.update({"X-Requested-With": "XMLHttpRequest",
                                       "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
            res = requests.post("https://m1.tg5000.net/order.php", data=data,
                                headers=self.phone_headers).text
            new_list = re.findall(
                re.compile(r'<input type="hidden" name=".*?" id=".*?" value="(.*?)">'),
                res)
            # money = re.search(re.compile("<span>可用余额：</span><span>(.*?)</span>"), res).group(1)
            data = {
                'c2betorder[0][handicap]': new_list[4],
                'c2betorder[0][inplay]': new_list[13],
                'c2betorder[0][selectname]': new_list[12],
                'c2betorder[0][time]': new_list[11],
                'c2betorder[0][gameid]': new_list[1],
                'c2betorder[0][markettype]': new_list[10],
                'c2betorder[0][gamename]': new_list[5],
                'c2betorder[0][marketname]': new_list[6],
                'c2betorder[0][Rate]': new_list[7],
                'c2betorder[0][Bet]': order_money,
                'c2betorder[0][BetType]': new_list[3],
                'c2betorder[0][MarketId]': new_list[0],
                'c2betorder[0][SelectionId]': new_list[2],
                'c2betorder[0][betfairori]': new_list[9],
                'c2betorder[0][percent]': new_list[8],
                'c2betorder[0][chk]': 'order',
                'c2betorder[0][selectrateL1]': new_list[14],
                'c2betorder[0][category]': new_list[16],
                'c2betorder[0][sel]': new_list[17],
                'c2betorder[0][gc12]': new_list[15]
            }
            # data = {
            #     'c2betorder[0][handicap]': '',
            #     'c2betorder[0][inplay]': '0',
            #     'c2betorder[0][selectname]': news[0],
            #     'c2betorder[0][time]': str(news[1]).replace(":", "%3A").replace(" ", "+"),
            #     'c2betorder[0][gameid]': news[2],
            #     'c2betorder[0][markettype]': news[3],
            #     'c2betorder[0][gamename]': news[4],
            #     'c2betorder[0][marketname]': news[6],
            #     'c2betorder[0][Rate]': news[7],
            #     'c2betorder[0][Bet]': ,
            #     'c2betorder[0][BetType]': 'L',
            #     'c2betorder[0][MarketId]': news[5],
            #     'c2betorder[0][SelectionId]': news[10],
            #     'c2betorder[0][betfairori]': '',
            #     'c2betorder[0][percent]': news[11],
            #     'c2betorder[0][chk]': 'order',
            #     'c2betorder[0][selectrateL1]': news[8],
            #     'c2betorder[0][category]': news[12],
            #     'c2betorder[0][sel]': '',
            #     'c2betorder[0][gc12]': news[9]
            # }
            # self.phone_headers.update({"X-Requested-With": "XMLHttpRequest",
            #                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            #                            })
            # # https://m1.tg5000.net/order_finish.php
            # proxies = {
            #     "http": "http://123.133.194.113:4245",
            #     # "https": "https://123.133.194.113:4245"
            # }
            res = requests.post("https://m1.tg5000.net/order_finish.php", data=data,
                                headers=self.phone_headers).text
            print("交易源码返回", res)
            if "交易成功" in res:
                print(f"{news[12]}:抢单成功")
            else:
                print(f"{news[12]}:抢单失败")
            bools = self.deal_time(news[1])
            if bools == True:
                return "保本结束"
        else:
            return "继续"

if __name__ == '__main__':
    alls = open("账号.txt", 'r').readlines()
    nums = len(alls)
    times = 0.0
    if nums == 5:
        times = 1.0
    elif nums == 1:
        times = 5.0
    elif nums >= 2 or nums <= 4:
        times = 2.0
    over = 0
    cookie_list = []
    soccer = Soccer()
    say_cookie = 0
    count_sai = -1
    while True:
        for i in alls:
            ok = i.replace("\n", "")
            usernames = ok.split("-")
            cookie = soccer.login(usernames[0], usernames[1])
            # print(f"账号{usernames[0]}的cookie为{cookie}")
            if "say" in cookie:
                cookie = cookie
                cookie_list.append(cookie)
                for n in range(nums):
                    test = alls[n].split('-')[0]
                    if usernames[0] == test:
                        del alls[n]
                        break
        if len(cookie_list) == nums:
            break
    some = []
    while True:
        if len(some) == 0:
            print("获取保本中....")
            first = cookie_list[0]
            some = soccer.get_tg(first)
            print("进入保本读取点数")
        if count_sai == -1:
            if len(some) != 0:
                print(f"选择你确定的赛事，输入序号即可：{some}")
                no = int(input("输入序号单次输入一个（例：1,2,3):"))
                if no < 0 or no > len(some):
                    print("输入错误")
                else:
                    no = no - 1
                    count_sai = no
                    for i in cookie_list:
                        sleep(times)
                        error = soccer.order_money(some, i, no)
                        if error == "继续":
                            continue
                        elif error == "保本结束":
                            count_sai = -1
                            for n in range(nums):
                                del some[no]
                                break
                            break
                        if error == "没钱了":
                            print("此账号没钱了")
                            if len(cookie_list) == 1:
                                say_cookie = 1
                                break
                            else:
                                for s in range(len(cookie_list)):
                                    if i == cookie_list[s]:
                                        del cookie_list[s]
                                        break
                    if say_cookie == 1:
                        break
        else:
            for i in cookie_list:
                sleep(times)
                error = soccer.order_money(some, i, count_sai)
                if error == "继续":
                    continue
                elif error == "保本结束":
                    count_sai = -1
                    for n in range(nums):
                        del some[count_sai]
                        break
                    break
                if error == "没钱了":
                    print("此账号没钱了")
                    if len(cookie_list) == 1:
                        say_cookie = 1
                        break
                    else:
                        for s in range(len(cookie_list)):
                            if i == cookie_list[s]:
                                del cookie_list[s]
                                break
            if say_cookie == 1:
                break
    input("运行结束")

