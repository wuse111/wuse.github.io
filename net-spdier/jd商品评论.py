import pandas as pd
import requests


def spider():
    import json
    from time import sleep
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
        "Connection": "close",
        "cookie": "__jdu=15954869081851532851244; shshshfpa=7ced5464-2160-2ad4-7037-be68cab621fd-1595486909; shshshfpb=dAmV1AKQvtBBfBMOA0N%2Fhwg%3D%3D; PCSYCityID=CN_420000_420100_420115; jwotest_product=99; areaId=17; ipLoc-djd=17-1381-50713-0; user-key=08cae084-fb05-4d33-9093-a470364a1cd9; cn=0; unpl=V2_ZzNtbRdVFBF2XBQELx1bAGIKRQ5LAEAUcg1BUnsRDAdiVBMJclRCFnQURldnGFQUZwcZXUZcRxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdVAFiChVVQ15DHHEIQlZ4EFgFZAYXbXJQcyVFCkNRfxBVNWYzE20AAx8RfAlPUH9UXAFvBxdURV9CHHUBQlR%2fG18MYwMRWEdnQiV2; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d3f52ecae56448fb8f20646719a34f0e|1607498153649; __jda=122270672.15954869081851532851244.1595486908.1607410637.1607498154.11; __jdc=122270672; shshshfp=13bcfd254969cbc223ddfceeced4039c; 3AB9D23F7A4B3C9B=HW4D3G5A3Q2IXJ4SY6S2NM7ICPLYGK733YMZDIRQMHJREZCEQX4RJ7G2PEDYN6ROJ7R7RQWIADFI3SZ3WZCTEFK2VU; shshshsID=77f1b2020bc53d696b11e30087379ec6_5_1607498180412; __jdb=122270672.5.15954869081851532851244|11.1607498154"}
    page = 0
    back_list = []
    soType = ''
    scores = ["3", "2", "1"]  # 好评，中评，差评
    # productId = ["100009077475", "100016168278"]  # 苹果和华为id
    product = "55701411500"
    li = ''
    # so = '2'
    # for product in productId:
    #     for so in scores:
    # if so == "3":
    #     li = "好评"
    # elif so == "2":
    #     li = "中评"
    # else:
    #     li = "差评"
    print(li)
    while True:
        sleep(2)
        if soType == '':
            sorts = '5'
        else:
            sorts = str(soType)
        param = {
            "callback": "fetchJSON_comment98",
            "productId": product,
            "score": "0",
            "sortType": sorts,
            "page": page,
            "pageSize": "10",
            "isShadowSku": "0",
            "fold": "1"
        }
        page += 1
        try:
            res = requests.get("https://club.jd.com/comment/productPageComments.action", params=param,
                               headers=headers).text
        except Exception as e:
            print(e)
            break
        alls = res.replace("fetchJSON_comment98(", "").replace(");", "")
        try:
            ok = json.loads(alls)
        except:
            break
        # 1.分析大多数用户所购买的手机颜色和存储空间，得出大众选择的手机颜色和类型
        # 2.通过评分的分析那款手机最受大众喜欢
        # 3.评论情感分析对产品的真实评价和评分的对比
        # 4.手机的配送时间的分析手机配送的效率
        print(ok)
        try:
            ok_list = ok['comments']
            soType = ok['soType']
        except:
            break
        if ok_list == []:
            break
        for i in ok_list:
            content = i['content']
            productColor = i['productColor']
            productsize = i['productSize']
            score = i['score']
            order_time = i['referenceTime']
            days = i['days']
            new = content, productColor, productsize, score, order_time, days
            back_list.append(new)
        print(f"已经爬取{len(back_list)}")
    # if product == "100009077475":
    #     path = f"jd_iPhone12_{li}.xlsx"
    # else:
    #     path = f"jd_HUAWEI Mate 40 Pro_{li}.xlsx"
    df = pd.DataFrame(back_list)
    df.to_excel(excel_writer=f'湖北宜昌秭归橙子{li}.xlsx', sheet_name="sheet1", index=False,
                header=['评论内容', '手机颜色', '手机尺寸', '评分', '预定时间', '配送时间'])



def deal_with(path):
    import re
    df = pd.read_excel(io=path, sheet_name=[0, ])
    comment_list = df[0]['评论内容'].drop_duplicates()
    b_list = ["外形外观：", "屏幕音效：", "运行速度：", "待机时间：", "其他特色：", "拍照效果："]
    all_list = []
    for i in comment_list:
        new = i.replace('\n', '')
        ok = re.sub(r"&(.*?);", "", new)
        if "高大上，很棒 。" not in ok:
            for n in b_list:
                if n == "外形外观：":
                    ok = ok.replace(n, "")
                else:
                    ok = ok.replace(n, "")
            ok = re.sub(r'[-!?:#~！？*]', "", ok)
            if len(ok) > 3:
                if "一般" not in ok:
                    all_list.append(ok)
    return all_list


def data_preprocessing(path):
    # path_list = ["HUAWEI Mate 40 Pro"]
    # so_list = ["中评", "差评"]  #, "中评", "差评"
    # for paths in path_list:
    #     other_list = []
    # for so in so_list:
    #     path = f"jd_{paths}_{so}.xlsx"
    #     print(path)
    #
    #     other_list.extend(b_list)
    other_list = deal_with(path)
    string = []
    for i in other_list:
        txt_list = seg_sentence(i.strip())
        string1 = txt_list
        string.append(string1)
    df = pd.DataFrame(string)
    df.to_excel(f"湖北宜昌分词处理.xlsx", header=['分词'], index=False)
    # df = pd.DataFrame(other_list)
    # df.to_excel(excel_writer=f"jd_{paths}_好评分词.xlsx", header=["处理过后的评论"], index=False)
def seg_sentence(sentence):
    import jieba
    sentence_seged = jieba.cut(sentence.strip())
    #print("/ ".join(sentence_seged))
    stopwords = [word.replace('\n', '').strip() for word in open("stopwords.txt", "r", encoding="utf-8").readlines()]
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def get_wordcloud():
    import wordcloud
    from wordcloud import STOPWORDS
    # import jieba
    path = 'jd_HUAWEI Mate 40 Pro_全部.xlsx'
    df = pd.read_excel(path)
    data = df['处理过后的评论'].values
    string = []
    for i in data:
        txt_list = seg_sentence(i)
        # txt_list = jieba.lcut(i)
        string1 = txt_list
        # string = string + string1
        string.append(string1)
    df = pd.DataFrame(string)
    df.to_excel("jd_HUAWEI Mate 40 Pro_分词.xlsx", header=['分词'], index=False)
    # stopwords = set(STOPWORDS)
    # print(string)
    # alls = [s.replace("\n", "") for s in open("words.txt", "r", encoding="utf-8").readlines()]
    # for a in alls:
    #     stopwords.add(a)
    # w = wordcloud.WordCloud(width=1300, height=1000, background_color='white', font_path='msyh.ttc',
    #                         stopwords=stopwords)
    # w.generate(string)
    # w.to_file("词云.png")


def get_wc(path):
    import wordcloud
    from wordcloud import STOPWORDS
    df = pd.read_excel(path)
    data = df['分词'].values
    string = ''
    for i in data:
        string = string + i
    stopwords = set(STOPWORDS)
    alls = [s.replace("\n", "") for s in open("words.txt", "r", encoding="utf-8").readlines()]
    for a in alls:
        stopwords.add(a)
    stopwords = stopwords
    w = wordcloud.WordCloud(width=1000, height=700, background_color='white', font_path='msyh.ttc',
                            stopwords=stopwords)
    w.generate(string)
    w.to_file("词云.png")

def LDA(path):
    from gensim import corpora, models
    import re
    df = pd.read_excel(path)
    data = df['分词'].values
    string = []
    stopword = [s.replace("\n", "") for s in open("words.txt", "r", encoding="utf-8").readlines()]
    new = []
    for i in data:
        s = str(i).split(" ")
        for gg in s:
            if gg != '':
                if gg not in stopword:
                    new.append(gg)
        string.append(new)
    pos_dict = corpora.Dictionary(string)
    pos_corpus = [pos_dict.doc2bow(i) for i in string]
    pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)
    # 展示主题
    pos_theme = pos_lda.show_topics()
    print(pos_theme)
    import pyLDAvis  # 可视化
    # import pyLDAvis.gensim
    # vis = pyLDAvis.gensim.prepare(pos_lda, pos_corpus, pos_dict)
    # # 在浏览器中心打开一个界面
    # pyLDAvis.show(vis)
    # for i in pos_theme:
    #     print(i[1])
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # pattern.findall(pos_theme[0][1])
    # pos_key_words = []
    # for i in range(3):
    #     pos_key_words.append(pattern.findall(pos_theme[i][1]))
    # pos_key_words = pd.DataFrame(data=pos_key_words, index=['主题1', '主题2', '主题3'])
    # pos_key_words.to_csv("负面.csv", index=False, encoding='utf_8_sig')
def get_pic():
    import matplotlib.pyplot as plt

    labels = '积极情绪', '中性情绪', '消极情绪'
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文字体的函数
    # 12.08%	85.85%	2.07%
    sizes = [12.08, 85.85, 2.07]
    explode = (0, 0.1, 0)
    colors = ['b', 'r', 'g']
    # 华为mate 40 Pro的情感分析
    plt.title(r'华为mate 40 Pro的情感分析', fontproperties='SimHei', fontSize=15)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', pctdistance=0.7,
            shadow=True, startangle=90, counterclock=False, wedgeprops=dict(edgecolor='w', width=0.7, linewidth=10))
    plt.axis('equal')  # 正圆形的饼图
    plt.savefig("华为的情感分析.png", dpi=200, bbox_inches='tight')
    plt.show()



if __name__ == '__main__':
    # spider()
    # data_preprocessing('湖北宜昌秭归橙子.xlsx')
    # get_wc('湖北宜昌分词处理.xlsx')
    LDA('湖北宜昌分词处理.xlsx')
    # pos_theme = [(0,
    #               '0.019*"屏幕" + 0.014*"拍照" + 0.011*"速度" + 0.009*"说" + 0.008*"流畅" + 0.008*"好看" + 0.007*"运行" + 0.007*"屏" + 0.006*"麒麟" + 0.006*"手感"'),
    #              (1,
    #               '0.020*"屏幕" + 0.015*"拍照" + 0.012*"速度" + 0.009*"流畅" + 0.009*"说" + 0.009*"好看" + 0.008*"手感" + 0.007*"运行" + 0.007*"屏" + 0.006*"抢"'),
    #              (2,
    #               '0.017*"屏幕" + 0.013*"拍照" + 0.011*"速度" + 0.009*"外观" + 0.008*"支持" + 0.007*"手感" + 0.007*"屏" + 0.007*"好看" + 0.007*"说" + 0.006*"麒麟"')]
    # import re
    #
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # pattern.findall(pos_theme[0][1])
    # pos_key_words = []
    # for i in range(3):
    #     pos_key_words.append(pattern.findall(pos_theme[i][1]))
    #
    # pos_key_words = pd.DataFrame(data=pos_key_words, index=['主题1', '主题2', '主题3'])
    # pos_key_words.to_csv("测试.csv", index=False, encoding='utf_8_sig')

    # get_wc()
    # get_wordcloud()
    # data_preprocessing()
    # spider()

