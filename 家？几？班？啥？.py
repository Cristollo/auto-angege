# encoding=utf-8
from wxpy import *
import time

'''
作者：刘源
时间：2020/1/3
功能：微信网页版聊天机器人 自动给安哥哥发送几?家?班?啥?；在包含有安哥哥的群聊中@安哥哥
'''

bot = Bot()
my_friend = bot.friends().search('常安', sex=MALE, city="保定")[0]
wxpy_groups = bot.groups().search('定州常务委员会', [常安])
while(1):
    my_friend.send('几?家?班?啥?')
    wxpy_groups.send('@安哥哥')
    sleep_time = random.randint(sys.argv[1], sys.argv[2])#最短睡眠时间和最长睡眠时间
	print("sleeping, %d seconds remains"%(sleep_time))
	time.sleep(sleep_time)