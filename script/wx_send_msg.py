import csv
from time import sleep

from wxpy import *

path = './sample.csv'


def read_file():
    f = open(path, 'r')
    reader = csv.DictReader(f)
    # 列表解析式
    return [info for info in reader]


def create_msg(info):
    template = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}，收到请回复，谢谢！'
    return [template.format(n=i['姓名'],
                            t=i['上课时间'],
                            s=i['课程'],
                            a=i['上课地址']
                            ) for i in info]


def send_msg(msg):
    friend_name = msg.split('-')[0]
    bot = Bot()
    f = bot.friends().search(friend_name)
    if len(f) == 1:
        try:
            f[0].send_msg(msg)
        except:
            print('Stop at: ')
            print(msg)
    else:
        print(friend_name)
        print('Please check this name')
    sleep(3)


info = read_file()
msgs = create_msg(info)
for msg in msgs:
    send_msg(msg)
