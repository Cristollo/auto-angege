# !/usr/bin/python
# -*- coding:utf-8 -*-
import subprocess, time, sys

TIME = 600  # 程序状态检测间隔（单位：分钟）
CMD = sys.argv[1]  # 需要执行程序的绝对路径，支持jar 如：D:\\calc.exe 或者D:\\test.jar


class Auto_Run():
    def __init__(self, sleep_time, cmd):
        self.sleep_time = sleep_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()  # 判断文件的后缀名，全部换成小写
        self.p = None  # self.p为subprocess.Popen()的返回值，初始化为None

        self.add_a = 0
        self.add_b = 0

        self.run()  # 启动时先执行一次程序

        try:
            while 1:
                time.sleep(sleep_time * 1)  # 休息10分钟，判断程序状态
                self.poll = self.p.poll()  # 判断程序进程是否存在，None：表示程序正在运行 其他值：表示程序已退出
                if self.poll is None:
                    print
                    "运行正常"
                else:
                    print
                    "未检测到程序运行状态，准备启动程序"
                    time.sleep(sleep_time * 3)
                    self.run()
        except KeyboardInterrupt as e:
            print
            "检测到CTRL+C，准备退出程序!"

    #            self.p.kill()                   #检测到CTRL+C时，kill掉CMD中启动的exe或者jar程序

    def run(self):
        if self.ext == ".py":
            print
            'start OK!'
            self.add_a += 1
            self.add_b += 1
            self.p = subprocess.Popen(['python', '%s' % self.cmd, '%d' % self.add_a, '%d' % self.add_b],
                                      stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=False)
        else:
            pass



app = Auto_Run(TIME,CMD)