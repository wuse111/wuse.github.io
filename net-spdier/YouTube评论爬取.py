# coding: utf-8
# Author：戏不能停啊
# Date ：2020/9/21 19:09
# Tool ：PyCharm
import requests
from time import sleep
def get_youtu(num,ares):
    import re
    # headers.update({"x-client-data": "CJC2yQEIpbbJAQjBtskBCKmdygEIhrXKAQiZtcoBCPXHygEI58jKAQjpyMoBCLTLygE="})
    # headers.update({"x-client-data": "CJC2yQEIpbbJAQjBtskBCKmdygEIhrXKAQiZtcoBCPXHygEI58jKAQjpyMoBCLTLygE=",
    #                 "cookie": "VISITOR_INFO1_LIVE=HOfa9LST_24;PREF=f4=4000000&gl=BD; YSC=rg2sBkF8Fxg; GPS=1"})
    while True:
        sleep(2.5)
        session.cookies.clear()
        last_list = []
        requests.adapters.DEFAULT_RETRIES = 5
        #https://www.youtube.com/
        res = requests.get('https://www.youtube.com/', headers=headers)
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        all_t = ''
        for key, value in cookie.items():
            if 'VISITOR_INFO1_LIVE'in key:
                all_t = all_t + key + '=' + 'HOfa9LST_24;'
            else:
                all_t = all_t + key + '=' + value + ';'
        cookie = all_t
        # PREF=f4=4000000&gl={ares}&hl=hi;
        # print(cookie)

        # print(requests .get('https://www.youtube.com/',headers=headers).text)
        headers.update({"cookie": cookie})
        #https://www.youtube.com/?gl=
        res = session.get(f'https://www.youtube.com/?persist_gl=1&gl={ares}', headers=headers, allow_redirects=False)
        # print('g', res.url)
        n_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        # print(n_cookie)
        all_t = ''
        for key, value in n_cookie.items():
            if 'PREF' in key:
                all_t = all_t + key + '=' + value + '&f4=4000000&hl=hi' + ';'
            else:
                all_t = all_t + key + '=' + value + ';'
        n_cookie = all_t
        # print(n_cookie)
        cookie = cookie + n_cookie
        headers.update({"cookie": cookie})
        res = session.get(f'https://www.youtube.com/?gl={ares}', headers=headers)
        n_cookie = requests.utils.dict_from_cookiejar(res.cookies)
        all_t = ''
        for key, value in n_cookie.items():
            all_t = all_t + key + '=' + value + ';'
        n_cookie = all_t
        # print(res.text)
        cookie = cookie + n_cookie
        # print(cookie)
        continuation = re.search(re.compile(r'"token":"(.*?)"'), res.text).group(1)
        visitorData = re.search(re.compile(r'"visitorData":"(.*?)"'), res.text).group(1)
        clickTrackingParams = re.search(re.compile(r'"clickTrackingParams":"(.*?)"'), res.text).group(1)
        browserVersion = re.search(re.compile(r'"browserVersion":"(.*?)"'), res.text).group(1)
        sessionId = re.search(re.compile(r'"sessionId":"(.*?)"'), res.text).group(1)
        key = re.search(re.compile(r'"INNERTUBE_API_KEY":"(.*?)"'), res.text).group(1)
        version = re.search(re.compile(r'"key":"cver","value":"(.*?)"'), res.text).group(1)
        osname = re.search(re.compile(r'"osName":"(.*?)"'), res.text).group(1)
        osVersion = re.search(re.compile(r'"osVersion":"(.*?)"'), res.text).group(1)
        useragent = re.search(re.compile(r'"userAgent":"(.*?)"'), res.text).group(1)
        browserName = re.search(re.compile(r'"browserName":"(.*?)"'), res.text).group(1)
        text_json = re.findall(re.compile(r'"url":"/watch(.*?)"'), res.text)
        # print(continuation, visitorData, clickTrackingParams, browserVersion, sessionId, key)
        # print(osVersion, osname, useragent, browserName)
        back_list = []
        encryptedToken = ''
        while True:
            if encryptedToken == '':
                headers.update({"content-type": "application/json", "cookie": cookie})
                datas = {"context":
                             {"client": {"hl": "zh-CN", "gl": ares, "visitorData": visitorData,
                                         "userAgent": useragent,
                                         "clientName": "WEB", "clientVersion": version, "osName":
                                             osname,
                                         "osVersion": osVersion, "browserName": browserName,
                                         "browserVersion": browserVersion,
                                         "screenWidthPoints": 1536, "screenHeightPoints": 754, "screenPixelDensity": 1,
                                         "utcOffsetMinutes": 480, "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                                         "connectionType": "CONN_CELLULAR_4G"},
                              "request": {"sessionId": sessionId, "internalExperimentFlags": [],
                                          "consistencyTokenJars": []}, "adSignalsInfo": {
                                 "consentBumpParams": {"consentHostnameOverride": "https://www.youtube.com",
                                                       "urlOverride": ""}},
                              "user": {}, "clientScreenNonce": "MC4wMDI1MjcyMjc2MjU3ODI2MTM.",
                              "clickTracking": {"clickTrackingParams": clickTrackingParams}},
                         "continuation": continuation}
                res = session.post(f'https://www.youtube.com/youtubei/v1/browse?key={key}', json=datas, headers=headers)
                # print(res.text)
                new_token = re.search(re.compile(r'"token": "(.*?)"'), res.text).group(1)
                n_text_json = re.findall(re.compile(r'"url": "/watch(.*?)"'), res.text)
                res = res.json()
                encryptedToken = res['responseContext']['consistencyTokenJar']['encryptedTokenJarContents']
                expirationSec = res['responseContext']['consistencyTokenJar']['expirationSeconds']
                clickTrackingParams = res['onResponseReceivedActions'][0]['clickTrackingParams']
                n_text_json.extend(text_json)
                # print(new_token,expirationSec,encryptedToken)
                # print(n_text_json)
                some_list = get_all(n_text_json, version, num, cookie)
                last_list.extend(some_list)
                if len(some_list) >= num:
                    return last_list
            else:
                headers.update({"content-type": "application/json", "cookie": cookie})
                new_data = {"context":
                                {"client": {"hl": "zh-CN", "gl": ares, "visitorData": visitorData,
                                            "userAgent": useragent,
                                            "clientName": "WEB", "clientVersion": version, "osName":
                                                osname,
                                            "osVersion": osVersion, "browserName": browserName,
                                            "browserVersion": browserVersion,
                                            "screenWidthPoints": 1536, "screenHeightPoints": 754, "screenPixelDensity": 1,
                                            "utcOffsetMinutes": 480, "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                                            "connectionType": "CONN_CELLULAR_4G"},
                                 "request": {"sessionId": sessionId, "internalExperimentFlags": [],
                                             "consistencyTokenJars": [{"encryptedTokenJarContents": encryptedToken,
                                                                       "expirationSeconds": expirationSec}]}, "adSignalsInfo": {
                                    "consentBumpParams": {"consentHostnameOverride": "https://www.youtube.com",
                                                          "urlOverride": ""}},
                                 "user": {}, "clientScreenNonce": "MC4wMDI1MjcyMjc2MjU3ODI2MTM.",
                                 "clickTracking": {"clickTrackingParams": clickTrackingParams}},
                            "continuation": new_token}
                # print(new_data)
                res = session.post(f'https://www.youtube.com/youtubei/v1/browse?key={key}', json=new_data, headers=headers)
                # print(res.text)
                try:
                    new_token = re.search(re.compile(r'"token": "(.*?)"'), res.text).group(1)
                except:
                    pass
                try:
                    n_text_json = re.findall(re.compile(r'"url":"/watch(.*?)"'), res.text)
                except:
                    pass
                res = res.json()
                try:
                    encryptedToken = res['responseContext']['consistencyTokenJar']['encryptedTokenJarContents']
                    expirationSec = res['responseContext']['consistencyTokenJar']['expirationSeconds']
                    clickTrackingParams = res['onResponseReceivedActions'][0]['clickTrackingParams']
                    # print(encryptedToken, clickTrackingParams, expirationSec, new_token)
                except KeyError:
                    pass
                some_list = get_all(n_text_json, version, num, cookie)
                last_list.extend(some_list)
                if len(some_list) >= num:
                    return last_list


def get_all(new_list, version, num, cookie):
    import re
    from urllib import parse
    g = 0
    back_list = []
    out = False
    # print(cookie)
    # print(len(new_list))
    headers.update({"cookie": cookie})
    for urls in new_list:
        # print(f'第{g + 1}条链接', urls)
        new_url = f'https://www.youtube.com/watch{urls}'
        sleep(2)
        res = session.get(new_url, headers=headers)
        # print(res.text)
        cl = re.search(re.compile(r'"PAGE_CL":(.*?),'), res.text).group(1)
        # "VARIANTS_CHECKSUM": "e05a2b4cf8828342601331d6a8c851c0"
        checksum = re.search(re.compile(r'"VARIANTS_CHECKSUM":"(.*?)"'), res.text).group(1)
        # print(checksum,cl)
        ctoken = re.search(re.compile(r'"continuation":"(.*?)"'), res.text).group(1)
        # "clickTrackingParams":"
        cit = re.search(re.compile(r'"clickTrackingParams":"(.*?)"'), res.text).group(1)
        cit = parse.quote(cit)
        # print(cit)
        # "xsrf_token":"
        session_token = re.search(re.compile(r'"XSRF_TOKEN":"(.*?)"'), res.text).group(1)
        # print(ctoken, cit, session_token)
        next_url = ''
        next_token = ''
        while True:
            if next_url != '':
                url = f'https://www.youtube.com/comment_service_ajax?action_get_comments=1&pbj=2&ctoken={next_url}&continuation={next_url}&itct={next_token}'
            else:
                url = f'https://www.youtube.com/comment_service_ajax?action_get_comments=1&pbj=2&ctoken={ctoken}&continuation={ctoken}&itct={cit}'
            data = {
                "session_token": session_token
            }
            headers.update({"content-type": "application/x-www-form-urlencoded",
                            "referer": new_url,
                            "x-spf-previous": new_url,
                            "x-spf-referer": new_url,
                            "x-youtube-page-cl": cl,
                            'x-youtube-client-name': '1',
                            'x-youtube-client-version': version,
                            "x-youtube-variants-checksum": checksum
                            # "x-youtube-device": "cbr=Chrome&cbrver=84.0.4147.135&ceng=WebKit&cengver=537.36&cos=Macintosh&cosver=10.0"
                            })
            # print('这里？')
            sleep(2)
            try:
                res = session.post(url, data=data, headers=headers)
            except:
                break
            # print(res)
            try:
                # continuations
                res = res.json()
                # print(res)
                next_url = res['response']['continuationContents']['itemSectionContinuation']['continuations'][0][
                    'nextContinuationData']['continuation']
                next_token = res['response']['continuationContents']['itemSectionContinuation']['continuations'][0][
                    'nextContinuationData']['clickTrackingParams']
                # print(next_url)
                # print(next_token)
            except:
                try:
                    # print('jinru')
                    # print(res.text)
                    next_url = re.search(re.compile('ctoken=(.*?)&'), res.text).group(1)
                    next_token = re.search(re.compile('itct=(.*?)"'), res.text).group(1)
                    # print(next_url)
                    # print(next_token)
                except:
                    break
            list1 = res['response']['continuationContents']['itemSectionContinuation']['contents']
            for i in list1:
                # print(i['commentThreadRenderer']['comment']['commentRenderer'])
                list2 = i['commentThreadRenderer']['comment']['commentRenderer']['contentText']['runs']
                # print("num", len(list2))
                for n in list2:
                    comment = n['text']
                    # highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
                    # comment = highpoints.sub(u'',comment)
                    back = check(comment)
                    # print(comment, back)
                    if back == 'hi':
                        g += 1
                        print(f'符合要求{g}个', comment)
                        back_list.append(comment)
                        if g == num:
                            break
                if g == num:
                    break
            if g == num:
                break
        if g == num:
            break
    return back_list


def check(text):
    import langid
    back = langid.classify(text)[0]
    return back


def get_country():
    #https://www.youtube.com/picker_ajax?action_country_json=1
    headers.update({"cookie": 'PREF=f4=4000000&gl=PY&hl=zh-CN'})
    res = session.get('https://www.youtube.com/picker_ajax?action_country_json=1', headers=headers).json()
    some = []
    for i in res['data'][1]:
        dic = {}
        gl = i[1]
        name = i[2]
        dic["代码"] = gl
        dic["名称"] = name
        some.append(dic)
    return some



if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
        # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
        }
    session = requests.Session()
    city = get_country()
    new_list = []
    print('选择所爬取地区，然后输入')
    for g in range(0,len(city)):
        print(f'{g + 1}:{city[g]["名称"]}')
    new = input('请输入国家代码，多个请用逗号：')
    if ',' not in new:
        n_new = city[int(new) - 1]
        ares = n_new['代码']
        # print(ares)
        num = int(input('请输入提取符合的数量：'))
        file = input('请输入保存的文件名：')
        if file == '':
            file = 'youtu_comment.txt'
        else:
            file = file + '.txt'
        if num == 0:
            print('请输入')
        else:
            b_list = get_youtu(num, ares)
            # print(b_list)
            s = ''
            for i in range(0, len(b_list)):
                if i == 0:
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(b_list[i] + '\n')
                else:
                    s = open(file, 'r', encoding='utf-8').read()
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(s + b_list[i] + '\n')
    else:
        for new_ in new.split(','):
            n_new = city[int(new_) - 1]
            new_list.append(n_new)
        for x in new_list:
            ares = x['代码']
            print(ares)
            num = 0
            file = ''
            if num == 0:
                num = int(input('请输入提取符合的数量：'))
            if file == '':
                file = input('请输入保存的文件名：')
            if file == '':
                file = 'youtu_comment.txt'
            else:
                file = file + '.txt'
            if num == 0:
                print('请输入')
            else:
                b_list = get_youtu(num, ares)
                # print(b_list)
                s = ''
                for i in range(0, len(b_list)):
                    if i == 0:
                        with open(file, 'w', encoding='utf-8') as f:
                            f.write(b_list[i] + '\n')
                    else:
                        s = open(file, 'r', encoding='utf-8').read()
                        with open(file, 'w', encoding='utf-8') as f:
                            f.write(s + b_list[i] + '\n')
    input('输入任意键退出')
