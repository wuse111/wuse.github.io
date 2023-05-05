# coding: utf-8

import requests
from lxml import etree
import re
import time


class Spider_bj:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
        }
        # 设定无法提取的或者不需要提取的数据
        self.data_list = []
        self.website = '首都医科大学附属北京儿童医院'
        self.extracted = 'N'
        self.doctor_hospital = '首都医科大学附属北京儿童医院'
        self.grab_date = time.strftime('%Y-%m-%d')
        self.doctor_sex = ''
        self.doctor_major = ''
        self.doctor_achievement = ''
        self.doctor_works = ''
        self.doctor_type = '医生'
        self.experience = ''
        # 设置前缀链接
        self.font = 'https://www.bch.com.cn/'

    def get_alloffice(self):
        '''爬取所有科室链接'''
        res = requests.get('https://www.bch.com.cn/Html/Hospitals/Departments/Overview0.html', headers=self.headers)
        tree = etree.HTML(res.text)
        ul_list = tree.xpath('//ul[@class="dep_list"]')
        url_list = []
        for ul in ul_list:
            li_list = ul.xpath('./li/a/@href')
            url_list.extend(li_list)
        return url_list

    def enter_url(self, list1):
        for i in list1:
            time.sleep(1.5)
            if i != '#':
                alls = self.font + i
                res = requests.get(alls, headers=self.headers)
                res.encoding = res.apparent_encoding
                if res.text.find('>更多专家>>') != -1:
                    # 进入更多专家页面
                    more = re.search(r'<a href="(.*?)">更多专家>></a>', res.text).group(1)
                    res = requests.get(self.font + more, headers=self.headers)
                    res.encoding = res.apparent_encoding
                    tree = etree.HTML(res.text)
                    # 爬取医生详情链接
                    li_list = tree.xpath('//ul[@class="docteam_list"]/li')
                    for n in li_list:
                        # 设置延时，防止爬取报错
                        time.sleep(2.5)
                        doctor_img = self.font + n.xpath('.//a/img/@src')[0]
                        url = self.font + n.xpath('.//a[@class="doc_name"]/@href')[0]
                        _id = url
                        doctor_name = n.xpath('.//a[@class="doc_name"]/text()')[0]
                        res = requests.get(url, headers=self.headers)
                        res.encoding = res.apparent_encoding
                        tree1 = etree.HTML(res.text)
                        doctor_title = tree1.xpath('//div[@class="doctor_con"]/dl/dd[1]/text()')[1]
                        doctor_department = tree1.xpath('//div[@class="doctor_con"]/dl/dd[2]/a/text()')[0].replace(
                            ' \xa0', '')
                        dd_list = tree1.xpath('//div[@class="doctor_con"]/dl/dd[3]/p/text()')
                        # 处理社会任职数据
                        strs = ''
                        for d in dd_list:
                            strs = strs + d + ';'
                        social_position = strs
                        news = tree1.xpath('//div[@id="Descri_all"]/p/text()')
                        # 处理医生简介
                        for ne in news:
                            strs = strs + ne
                        doctor_info = strs.replace('\xa0', '')
                        # 判断是否存在博士身份,不智能
                        if '博士' in doctor_info:
                            education = '博士'
                        # 设置多种爬取方式
                        try:
                            skill = tree1.xpath('//div[@id="specialty"]/p[2]/text()')[0].replace(' \xa0', '')
                        except IndexError:
                            try:
                                skill = tree1.xpath('//div[@id="specialty"]/p/text()')[0].replace(' \xa0', '')
                            except:
                                skill = ''
                        data = _id, url, self.grab_date, self.website, self.extracted, doctor_name, doctor_img, self.doctor_sex, education, doctor_department, doctor_title, self.doctor_major, skill, \
                               self.doctor_achievement, self.doctor_works, self.experience, social_position, doctor_info, self.doctor_hospital, self.doctor_type
                        print(data)
                        self.data_list.append(data)
        return self.data_list


if __name__ == '__main__':
    sp = Spider_bj()
    back_list = sp.get_alloffice()
    some = sp.enter_url(back_list)
    import pandas as pd

    # 保存excel文件
    df = pd.DataFrame(some, columns=['_id', 'url', 'grab_date', 'website', 'extracted', 'doctor_name', 'doctor_img',
                                     'doctor_sex', 'education', 'doctor_department', 'doctor_title', 'doctor_major',
                                     'skill',
                                     'doctor_achievement', 'doctor_works', 'experience', 'social_position',
                                     'doctor_info', 'doctor_hospital', 'doctor_type'])
    df.to_excel('data.xlsx', index=False)
