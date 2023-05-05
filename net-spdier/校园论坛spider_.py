import requests
from time import sleep
from lxml import etree


class Bbs:
    def __init__(self):
        self.phone_headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }
        self.de_user = self.phone_headers.copy()
        self.cookie = {}
        self.host = "https://bbs.pku.edu.cn/v2/mobile/"
        self.error = "校外IP可能需要登录后才能访问本页面。"

    def get_all(self):
        link_list = []
        #再首页提取一些cookie
        res = requests.get("https://bbs.pku.edu.cn/v2/mobile/board.php", headers=self.phone_headers)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        self.cookie = cookie
        res = requests.get("https://bbs.pku.edu.cn/v2/mobile/board.php?bid=679", headers=self.phone_headers,
                           cookies=cookie)
        try:
            selector = etree.HTML(res.text)
            con_list = selector.xpath('//div[@class="item"]')
            for i in con_list:
                link = self.host + i.xpath('./a/@href')[0]
                link_list.append(link)
            return link_list
        except Exception as e:
            print(f"提取版面链接报错:{e}")
    def get_cons(self,list1):
        self.phone_headers.update({"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
        post_list = []
        count = 1
        print(f"一共有{len(list1)}个版面..")
        boos = 0
        for i in list1:
            sleep(3.5)
            print(f"爬取第{count}个版面..")
            count += 1
            res = requests.get(i, headers=self.phone_headers, cookies=self.cookie)
            if self.error in res.text:
                print(f"错误:{self.error},先返回已爬取的帖子链接")
                return post_list
            selector = etree.HTML(res.text)
            try:
                max_page = int(selector.xpath('//div[@class="pagination"]/input/@max')[0])
            except:
                max_page = int(selector.xpath('//div[@class="row"]/span/text()')[0].replace("1 / ", ""))
            #&mode=topic&page=2
            print(max_page)
            for n in range(1, max_page + 1):
                print(f"爬取第{n}页的帖子链接.")
                if n == 1:
                    new_link = i + f'&mode=topic'
                else:
                    new_link = i + f"&mode=topic&page={n}"
                sleep(3.5)
                res = requests.get(new_link, headers=self.phone_headers, cookies=self.cookie)
                if self.error in res.text:
                    print(f"错误:{self.error},先返回已爬取的帖子链接")
                    return post_list
                selector = etree.HTML(res.text)
                # class="thread-item"
                item_list = selector.xpath('//div[@class="thread-item"]')
                for item in item_list:
                    time = item.xpath('./div[@class="row info"]/div[@class="item time"]/span[2]/text()')[0]
                    reply = item.xpath('./div[@class="row info"]/div[@class="item reply r"]/span/text()')[0]
                    boos = self.deal_(time, reply)
                    if boos == 1:
                        print("找到符合的帖子链接")
                        post_link = self.host + item.xpath('./a[@class="thread-link"]/@href')[0]
                        post_list.append(post_link)
                    elif boos == 3:
                        print("帖子时间太长，进行过滤")
                        break
                if boos == 3:
                    break
        return post_list



    def get_tie(self,url):
        com_back = []
        res = requests.get(url, headers=self.phone_headers, cookies=self.cookie)
        if self.error in res.text:
            print(f"错误:{self.error}")
            com_back.append(self.error)
            return com_back
        selector = etree.HTML(res.text)
        try:
            con_page = int(selector.xpath('//div[@class="pagination"]/input/@max')[0])
        except:
            con_page = int(selector.xpath('//div[@class="row"]/span/text()')[0].replace("1 / ", ""))
        try:
            title = selector.xpath('//p[@class="title"]/text()')[0]
            comment_list = selector.xpath('//div[@class="post-card"]')
            post_cons = comment_list[0].xpath('./div[@class="file-read body"]/p/text()')
        except Exception as e:
            print(f"爬取帖子内容报错:{e}")
            return com_back
        cons = ''
        for posts in post_cons:
            one = posts.replace('\xa0', '') + '\n'
            cons = cons + one
        sum_con = title + "\n" + cons
        boos = self.deal_com(sum_con)
        if boos == True:
            print("找到符合感情词典的要求,进行爬取原帖和评论.")
            for i in range(1, con_page + 1):
                if i == 1:
                    link = url
                else:
                    link = url + f"&page={i}"
                sleep(3.5)
                res = requests.get(link, headers=self.phone_headers, cookies=self.cookie)
                if self.error in res.text:
                    print(f"错误:{self.error}")
                    com_back.append(self.error)
                    return com_back
                selector = etree.HTML(res.text)
                comment_list = selector.xpath('//div[@class="post-card"]')
                for comm in comment_list:
                    two = comm.xpath('./div[@class="file-read body"]/p/text()')
                    cons = ''
                    for posts in two:
                        one = posts.replace('\xa0', '') + '\n'
                        cons = cons + one
                    com_back.append(cons)
            return com_back
        else:
            return com_back

    def deal_com(self, cons):
        word_list = open("感情词典.txt", 'r', encoding="utf-8").readlines()
        word_list = [str(n).replace("\n", "") for n in word_list]
        count = 0
        for i in word_list:
            if i in cons:
                return True
            else:
                return False
    def deal_(self,times,replys):
        bingo = 0
        #years后面接年数
        now_years = 2020
        #设置几年
        year_count = 3
        #设置回复数
        reply_ok = 50
        years = [now_years - ye for ye in range(1, year_count)]
        if str(now_years) not in times:
            if ":" in times:
                bingo += 1
            elif "分钟" in times:
                bingo += 1
            else:
                for year in years:
                    if str(year) in times:
                        bingo += 1
                        break
                    else:
                        new = times.split("-")[0]
                        if int(new) < years[year_count - 2]:
                            return 3
        if int(replys) >= reply_ok:
            bingo += 1
        if bingo == 2:
            return 1
        else:
            return 0



if __name__ == '__main__':
    import pandas as pd

    spider = Bbs()
    print("进入七区，爬取所有的版面...")
    b_list = spider.get_all()
    print("版面链接爬取完成，进入每个版面...")
    back = spider.get_cons(b_list)
    print(f"符合要求的帖子数量{len(back)}个...")
    print("爬取帖子内容...")
    post_count = 1
    for post in back:
        print(f"爬取第{post_count}个帖子..")
        post_count += 1
        post_back = spider.get_tie(post)
        if post_back != []:
            print("爬取完成，进入保存...")
            df = pd.DataFrame(post_back)
            try:
                df.to_csv(path_or_buf=f"第{post_count}个帖子.csv", header=['内容'], index=False)
            except Exception as e:
                print(f"保存文件报错:{e},更换保存方式")
                df.to_excel(excel_writer=f"第{post_count}个帖子.xlsx", sheet_name="sheet1", header=['内容'], index=False)
        elif "校外IP可能需要登录后才能访问本页面" in post_back:
            continue
        else:
            continue
    print("保存成功")
    input("输入任意键退出")
