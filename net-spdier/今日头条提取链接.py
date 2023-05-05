# coding: utf-8
# Author：戏不能停啊
# Date ：2020/7/14 10:23
# Tool ：PyCharm
import requests
from base64 import b64decode
import json


def get_url(num):
    """
    :param num: 页数
    :return: 视频列表
    """
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    res = requests.post(f'http://www.365yg.com/xigua/feed/?ChannelID=6797027941&Count={num}&UseHQ=true',
                        headers=headers,
                        allow_redirects=False).json()
    data_list = []
    base_list = res['Data']
    for base in base_list:
        base = base['raw_data']
        raw = b64decode(base).decode()
        raw = json.loads(raw)
        title = raw['title']
        group_id = raw['group_id']
        video_id = raw['video_id']
        token = raw['play_biz_token']
        auth_token = raw['play_auth_token']
        #第一种，通过group_id提取视频的链接

        # res = requests.post(f'http://www.365yg.com/xigua/play/?GroupID={group_id}', headers=headers,
        #                     allow_redirects=False).json()
        # video_list = json.loads(res['InformationResponse']['Info']['PackedJson'])['video_play_info']
        # video_list = json.loads(video_list)['video_list']

        #第二种，通过提取video_id和两个token，提取视频链接

        url = f'http://vas.snssdk.com/video/openapi/v1/?format_type=dash&action=GetPlayInfo&video_id={video_id}&nobase64=false&ptoken={token}&vfrom=xgplayer'
        headers.update({'Authorization': auth_token})
        res = requests.get(url, headers=headers).json()

        #这下面的提取是两种方法通用
        try:
            video_list = res['data']['dynamic_video']['dynamic_video_list']
            # print("dv_list", video_list)
            for video in video_list:
                video_type = video['definition']
                video_url = b64decode(video['main_url']).decode()
                # print(title + ':' + video_type + '|' + video_url)
                data = title, video_type, video_url
                data_list.append(data)
        except TypeError:
            video_list = res['data']['video_list']
            # print("v_list", video_list)
            for i in range(1, 5):
                try:
                    video_type = video_list[f'video_{i}']['definition']
                    video_url = b64decode(video_list[f'video_{i}']['main_url']).decode()
                    # print(title + ':' + video_type + '|' + video_url)
                    data = title, video_type, video_url
                    data_list.append(data)
                except KeyError:
                    pass
        finally:
            pass
    return data_list


if __name__ == '__main__':
    num = int(input('提取多少:'))
    g = 0
    b_list = get_url(num)
    for b in b_list:
        try:
            s = open('提取的视频链接.txt', 'r').read()
            with open('提取的视频链接.txt', 'w') as f:
                f.write(s)
                f.write(b[0] + '\n' + b[1] + '-' + b[2] + '\n')
        except FileNotFoundError:
            with open('提取的视频链接.txt', 'w') as f:
                f.write(b[0] + '\n' + b[1] + '-' + b[2] + '\n')
