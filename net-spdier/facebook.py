# coding: utf-8
# Author：戏不能停啊
# Date ：2020/9/21 21:09
# Tool ：PyCharm

import requests


def get_facebook(url, keyword, name):
    import re
    from bs4 import BeautifulSoup
    import json
    from time import sleep
    import time
    string = ''
    #提取post链接和cookie
    res = requests.get(url, headers=headers)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    all_t = ''
    for key, value in cookie.items():
        all_t = all_t + key + '=' + value + ';'
    cookie = all_t
    try:
        #取帖子的链接
        post_url = re.search(re.compile(r'aria-current="page" href="(.*?)">'), res.text).group(1)
        post_url = 'https://www.facebook.com' + post_url
        # print(post_url)
        if 'posts' not in post_url:
            one_list = re.findall(re.compile(r'<a class="_2yau" data-endpoint="(.*?)"'), res.text)
            for post in one_list:
                if 'posts' in post:
                    post_url = 'https://www.facebook.com' + post
                    print(post_url)
                    break
    except:
        return []
    if post_url == '':
        return []
    headers.update({"cookie": cookie})
    print(cookie)
    sleep(1.5)
    #访问post链接
    res = requests.get(post_url, headers=headers).text
    # headers.update()
    # print(res)
    back_list = []
    while True:
        #提取更多帖子的链接
        # if string == '':
        #     p_list = re.findall(re.compile(
        #         r'"i18n_comment_count":"(.*?)","url":"(.*?)","i18n_reaction_count":"(.*?)"[\s\S]*?"i18n_share_count":"(.*?)"'),
        #         res)
        #     # <a ajaxify="
        #     try:
        #         string = "https://www.facebook.com" + "/pages_reaction_units/more/" + str(
        #             re.search(re.compile(r'a ajaxify="/pages_reaction_units/more/(.*?)"'), res).group(1)).replace(
        #             "&amp;",
        #             "&") + "&fb_dtsg_ag&__user=0&__a=1"
        #     except AttributeError:
        #         pass
        #     try:
        #         user_id = re.search(re.compile(r'page_id=(.*?)&'), string).group(1)
        #     except:
        #         user_id = 'None'
        # while True:
            # if string == '':
        #     return back_list
        try:
            string = "https://www.facebook.com" + "/pages_reaction_units/more/" + str(
                re.search(re.compile(r'a ajaxify="/pages_reaction_units/more/(.*?)"'), res).group(1)).replace(
                "&amp;",
                "&") + "&fb_dtsg_ag&__user=0&__a=1"
        except AttributeError:
            pass
        try:
            #提取用户id
            user_id = re.search(re.compile(r'page_id=(.*?)&'), string).group(1)
        except:
            user_id = 'None'
        try:
            sleep(1.5)
            # headers.update({"referer": post_url})
            #访问帖子链接
            res = requests.get(
                f'https://www.facebook.com/ajax/pagelet/generic.php/PagePostsSearchResultsPagelet?fb_dtsg_ag&data=%7B%22page_id%22%3A%22{user_id}%22%2C%22search_query%22%3A%22climate%20change%22%7D&__user=0&__a=10',
                headers=headers).text.split("for (;;);")[1]
            break
        except:
            sleep(2)
    p_list = re.findall(re.compile(
        r'"i18n_comment_count":"(.*?)","url":"(.*?)","i18n_reaction_count":"(.*?)"[\s\S]*?"i18n_share_count":"(.*?)"'),
        res)
    res = json.loads(res)
    res = res['payload']
    # string = re.search(re.compile(r'<div><a ajaxify="(.*?)"'), res).group(1).replace(
    #     "&amp;",
    #     "&")
    # print(string)
    other = re.findall(re.compile(r'<span class="fsm fwn fcg"><a href="(.*?)"'),
                       res)
    for n_url in other:
        n_url = 'https://www.facebook.com/' + n_url
        res = requests.get(n_url, headers=headers).text
        print(res)
        try:
            #提取具体的内容
            some = re.findall(re.compile(r'<div class="hidden_elem">(.*?)--></code></div>'), res)[1]
        except:
            return back_list
        # print(some)
        soup = BeautifulSoup(some, 'html.parser')
        # print(soup)
        new_ = soup.find_all('div', class_="_1dwg _1w_m _q7o")
        for i in new_:
            all_t_t = str(i)
            soup1 = BeautifulSoup(all_t_t, 'lxml')
            compare_text = ''
            # had_bool = False
            al_con_url = ''
            # p的内容
            for p in soup1.find_all('p'):
                try:
                    # p里面的链接
                    # print('最开始p', p)
                    # print('测试提取的p', p.text)
                    con_url = p.a.text
                    # print('con_url', con_url)
                    if 'http' in con_url:
                        al_con_url = al_con_url + con_url + ','
                    elif 'www' in con_url:
                        al_con_url = al_con_url + con_url + ','
                    else:
                        al_con_url = 'None'
                except:
                    con_url = 'None'
                    al_con_url = con_url
                compare_text = compare_text + p.text
                # print(compare_text)
                # print(compare_text)
                # print(deal_keyword(keyword))
            # if con_url == '':
            #     con_url = 'None'
            try:
                timestamps = soup1.find_all('span', class_="timestampContent")[0].text
                print('time', soup1.find_all('span', class_="timestampContent"))
            except:
                timestamps = soup1.find('span', class_="timestampContent")
                print('time', timestamps)
            finally:
                pass
            if timestamps == None:
                pass
            for post_url in p_list:
                new_url = str(post_url[1]).replace('\\', '').split('/')[-1]
                if new_url in all_t_t:
                    comment_count = post_url[0]
                    reaction_count = post_url[2]
                    share_count = post_url[3]
            try:
                # 提取提及的账户
                back = ''
                high = soup1.find_all('a', class_="profileLink")
                for hi in high:
                    back = back + hi.text + ','
            except:
                back = 'None'
            # 提取时间
            try:
                # 提取图片链接和视频
                imgs = soup1.find_all('img', class_="scaledImageFitWidth img")
                a_b = ''
                for img_url in imgs:
                    a_b = a_b + img_url['src'] + ','
            except:
                a_b = 'None'
            try:
                # 提取新闻或文章链接
                wb_url = soup1.find_all('div', class_="_3ekx _29_4")
                wb_ = ''
                for wb in wb_url:
                    wb_ = wb_ + wb.a['href'] + ','
            except:
                wb_ = 'None'
            # 提取hashtags
            tags = soup1.find_all('span', class_="_58cm")
            if tags != []:
                al_tag = ''
                for hash_tag in tags:
                    al_tag = al_tag + hash_tag.text + ','
            else:
                al_tag = 'None'
            data = user_id, name, compare_text, al_tag, al_con_url, a_b, wb_, back, timestamps, comment_count, share_count, reaction_count
            back_list.append(data)

        # try:
        #     string = "https://www.facebook.com" + "/pages" + str(
        #         re.search(re.compile(r'<a ajaxify="/pages(.*?)"'), res).group(1)).replace(
        #         "&amp;",
        #         "&") + "&fb_dtsg_ag&__user=0&__a=1"
        #     # print('有sting', string)
        # except:
        #     break
    #用soup提取帖子具体内容
    # some = re.search(re.compile(r'<div class="_4-u2 mbm _4mrt _5v3q _7cqq _4-u8"(.*?)--></code></div>'),res).group(1)
    # # print(some)
    # soup = BeautifulSoup(some, 'html.parser')
    # # print(soup)
    # new_ = soup.find_all('div', class_="_1dwg _1w_m _q7o")
    # print(new_)
    # for i in new_:
    #     all_t_t = str(i)
    #     soup1 = BeautifulSoup(all_t_t, 'lxml')
    #     compare_text = ''
    #     had_bool = False
    #     al_con_url = ''
    #     #p的内容
    #     for p in soup1.find_all('p'):
    #         try:
    #             # p里面的链接
    #             # print('最开始p', p)
    #             # print('测试提取的p', p.text)
    #             con_url = p.a.text
    #             # print('con_url', con_url)
    #             if 'http' in con_url:
    #                 al_con_url = al_con_url + con_url + ','
    #             elif 'www' in con_url:
    #                 al_con_url = al_con_url + con_url + ','
    #             else:
    #                 al_con_url = 'None'
    #         except:
    #             con_url = 'None'
    #             al_con_url = con_url
    #         compare_text = compare_text + p.text
    #         # print(compare_text)
    #         # print(compare_text)
    #         # print(deal_keyword(keyword))
    #     # if con_url == '':
    #     #     con_url = 'None'
    #     try:
    #         timestamps = soup1.find_all('span', class_="timestampContent")[0].text
    #         print('time', soup1.find_all('span', class_="timestampContent"))
    #     except:
    #         timestamps = soup1.find('span', class_="timestampContent")
    #         print('time', timestamps)
    #     finally:
    #         pass
    #     if timestamps == None:
    #         pass
    #     for post_url in p_list:
    #         new_url = str(post_url[1]).replace('\\', '').split('/')[-1]
    #         if new_url in all_t_t:
    #             comment_count = post_url[0]
    #             reaction_count = post_url[2]
    #             share_count = post_url[3]
    #     try:
    #         # 提取提及的账户
    #         back = ''
    #         high = soup1.find_all('a', class_="profileLink")
    #         for hi in high:
    #             back = back + hi.text + ','
    #     except:
    #         back = 'None'
    #     # 提取时间
    #     try:
    #         # 提取图片链接和视频
    #         imgs = soup1.find_all('img', class_="scaledImageFitWidth img")
    #         a_b = ''
    #         for img_url in imgs:
    #             a_b = a_b + img_url['src'] + ','
    #     except:
    #         a_b = 'None'
    #     try:
    #         # 提取新闻或文章链接
    #         wb_url = soup1.find_all('div', class_="_3ekx _29_4")
    #         wb_ = ''
    #         for wb in wb_url:
    #             wb_ = wb_ + wb.a['href'] + ','
    #     except:
    #         wb_ = 'None'
    #     # 提取hashtags
    #     tags = soup1.find_all('span', class_="_58cm")
    #     if tags != []:
    #         al_tag = ''
    #         for hash_tag in tags:
    #             al_tag = al_tag + hash_tag.text + ','
    #     else:
    #         al_tag = 'None'
    #     data = user_id, name, compare_text, al_tag, al_con_url, a_b, wb_, back, timestamps, comment_count, share_count, reaction_count
    #     back_list.append(data)
            # try:
            #     timestamps = soup1.find_all('span', class_="timestampContent")[0].text
            #     print('time', soup1.find_all('span', class_="timestampContent"))
            # except:
            #     timestamps = soup1.find('span', class_="timestampContent")
            #     print('time', timestamps)
            # finally:
            #     pass
            # if timestamps == None:
            #     pass
            # else:
            #     if '年' not in timestamps:
            #         if '月' in timestamps:
            #             new_time = '2020年' + timestamps
            #             try:
            #                 timeArray = time.strptime(new_time, "%Y年%m月%d日")
            #                 timeStamp = int(time.mktime(timeArray))
            #                 print(timeStamp)
            #             except ValueError:
            #                 timeArray = time.strptime(new_time, "%Y年%m月%d日 %H:%M")
            #                 timeStamp = int(time.mktime(timeArray))
            #                 print(timeStamp)
            #             if timeStamp <= 1496246400:
            #                 return back_list
            #     else:
            #         try:
            #             timeArray = time.strptime(timestamps, "%Y年%m月%d日")
            #             timeStamp = int(time.mktime(timeArray))
            #             print(timeStamp)
            #         except ValueError:
            #             timeArray = time.strptime(timestamps, "%Y年%m月%d日 %H:%M")
            #             timeStamp = int(time.mktime(timeArray))
            #             print(timeStamp)
            #         if timeStamp <= 1496246400:
            #             return back_list
            # #关键词比对
            # for key in deal_keyword(keyword):
            #     if str(key) in compare_text:
            #         if had_bool == False:
            #             print('已找到', name)
            #             had_bool = True
            #             # back_list.append(user_id)
            #             # back_list.append(compare_text)
            #             #提取评论数，点赞数，转发数
            #             for post_url in p_list:
            #                 new_url = str(post_url[1]).replace('\\', '').split('/')[-1]
            #                 if new_url in all_t_t:
            #                     comment_count = post_url[0]
            #                     reaction_count = post_url[2]
            #                     share_count = post_url[3]
            #                     # back_list.append(comment_count)
            #                     # back_list.append(reaction_count)
            #                     # back_list.append(share_count)
            #             try:
            #                 #提取提及的账户
            #                 back = ''
            #                 high = soup1.find_all('a', class_="profileLink")
            #                 for hi in high:
            #                     back = back + hi.text + ','
            #             except:
            #                 back = 'None'
            #             # 提取时间
            #             try:
            #                 #提取图片链接和视频
            #                 imgs = soup1.find_all('img', class_="scaledImageFitWidth img")
            #                 a_b = ''
            #                 for img_url in imgs:
            #                     a_b = a_b + img_url['src'] + ','
            #             except:
            #                 a_b = 'None'
            #             try:
            #                 # 提取新闻或文章链接
            #                 wb_url = soup1.find_all('div', class_="_3ekx _29_4")
            #                 wb_ = ''
            #                 for wb in wb_url:
            #                     wb_ = wb_ + wb.a['href'] + ','
            #             except:
            #                 wb_ = 'None'
            #             # 提取hashtags
            #             tags = soup1.find_all('span', class_="_58cm")
            #             if tags != []:
            #                 al_tag = ''
            #                 for hash_tag in tags:
            #                     al_tag = al_tag + hash_tag.text + ','
            #             else:
            #                 al_tag = 'None'
            #             data = user_id, name, compare_text, al_tag, al_con_url, a_b, wb_, back, timestamps, comment_count, share_count, reaction_count
            #             back_list.append(data)
                        # print(new_url, comment_count, reaction_count, share_count)
                #'fb_id', 'text', 'fb_hash tags', 'fb_img & url', 'mention', 'time', 'reply', 'share', 'likes'
            # data = user_id, compare_text, al_tag, a_b + "|" + wb_, back, timestamps, comment_count, share_count, reaction_count
            # back_list.append(data)
        #     if len(back_list) == 2:
        #         break
        # if len(back_list) == 2:
        #     break
    return back_list


def deal_keyword(keyword):
    new_list = []
    for key in keyword:
        new_list.append(key)
        new_list.append(key.upper())
        new_list.append(key.capitalize())
    return new_list


def read_csv(file):
    import pandas as pd
    #读取csv
    files = pd.read_csv(file, usecols=[1, 3])
    data_list = files.values
    # print(data_list)
    return data_list


def writer(data, file_name):
    import xlwt
    if file_name == '':
        file_name = 'facebook.xls'
    else:
        file_name = file_name + '.xls'
    number = len(data)
    # print(data)
    # print(number)
    save_book = xlwt.Workbook(encoding='utf-8')
    save_sheet = save_book.add_sheet('sheet1')
    names = (
    'fb_id','name', 'text', 'fb_hash tags', 'con_url', 'fb_img', 'news_url', 'mention', 'time', 'reply', 'share', 'likes')
    for i in range(0, len(names)):
        save_sheet.write(0, i, names[i])
    for i in range(0, number):
        writer = data[i]
        # print('writer', writer)
        for j in range(0, len(names)):
            # print('new', i, j, writer[j])
            save_sheet.write(i + 1, j, writer[j])
    save_book.save(file_name)
    print('保存完成')


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    }
    #关键词读取
    alll_list = []
    s = open('keyword.txt', 'r').read()
    key_list = s.split('\n')
    print('关键词', key_list)
    #读取账户
    account = read_csv('Facebook带desmog.csv')
    for i in account:
        url = i[1]
        name = i[0]
        print('爬取', url)
        al_list = get_facebook(url, key_list, name)
        if al_list != []:
            #写出xls
            writer(al_list, 'facebook')
            # alll_list.extend(al_list)
            # print(len(alll_list))
            # if len(alll_list) == 300:
            #     writer(al_list, 'facebook')
        else:
            s = open("死链接.txt", 'r').read()
            with open("死链接.txt", "w") as f:
                f.write(s + url + '\n')
                f.close()
    print('爬取结束')

