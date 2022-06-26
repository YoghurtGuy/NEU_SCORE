import os
import re
import sys

from lxml import etree

import requests


def get_xpath(r, xpath_str):
    html = etree.HTML(r.text)
    res_list = html.xpath(xpath_str)
    return res_list


def write_js(num):
    x = 'async function getData(){const num = "' + str(num) + '";return num;}' \
                                                              'getData().then((num) => {console.log(num);return num;});'
    with open('score_num.js', "w") as file:
        file.write(x)


class NEU:
    def __init__(self):
        self.id = os.environ.get('SID')
        self.password = os.environ.get('PASSWORD')
        self.pushkey = os.environ.get('PUSHKEY')
        self.session = requests.session()

    def login_base(self, login_url, post_url):
        # 登陆，更新session
        response = self.session.get(login_url)
        if response.status_code != 200:
            print(str(response) + '登录失败！' + '(响应异常)')
            sys.exit()
        lt = re.findall(r'LT-[0-9]*-[0-9a-zA-Z]*-tpass', response.text, re.S)[0]

        login_form_items = {
            'rsa': self.id + self.password + lt,
            'ul': str(len(self.id)),
            'pl': str(len(self.password)),
            'lt': lt,
            'execution': 'e1s1',
            '_eventId': 'submit'
        }
        response = self.session.post(post_url, login_form_items)
        if response.status_code != 200:
            print(str(response) + '登录失败！' + '(响应异常)')
            sys.exit()

    def login(self):
        login1_url = 'https://webvpn.neu.edu.cn/'
        login2_url = 'https://webvpn.neu.edu.cn/https/77726476706e69737468656265737421e0f6528f693e6d45300d8db9d6562d' \
                     '/tpass/login?service=http%3A%2F%2F219.216.96.4%2Feams%2FhomeExt.action%3Bjsessionid' \
                     '%3D1CD246CF33E2553CCA315F972A65FB21.std10 '
        post1_url = 'https://pass.neu.edu.cn/tpass/login'
        post2_url = 'https://webvpn.neu.edu.cn/https/77726476706e69737468656265737421e0f6528f693e6d45300d8db9d6562d' \
                    '/tpass/login'

        self.login_base(login1_url, post1_url)
        self.login_base(login2_url, post2_url)

    def check_score(self):
        score_url = 'https://webvpn.neu.edu.cn/http/77726476706e69737468656265737421a2a618d275613e1e275ec7f8/eams' \
                    '/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR'
        response = self.session.get(score_url)
        if response.status_code != 200:
            print(str(response) + '获取成绩失败！' + '(响应异常)')
            sys.exit()
        xpath_str = '//*[@id="grid21344342991_data"]/tr[*]/td[{}]/text()'
        x = get_xpath(response, xpath_str.format(3))
        if len(x) != int(os.environ.get('NUM')):
            new = get_xpath(response, xpath_str.format(4))[-1].replace('\n', '').replace('\t', '')
            print(len(x), "有新成绩:" + new)
            self.push(new)
        else:
            print(len(x), "成绩未增加")
        write_js(len(x))
        

    def push(self, name):
        push_url = 'https://api2.pushdeer.com/message/push?pushkey=' + self.pushkey + '&text=' + name + '成绩公布'
        self.session.get(push_url)


if __name__ == '__main__':
    neu = NEU()
    neu.login()
    neu.check_score()
