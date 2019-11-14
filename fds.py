#-*- coding:utf-8 -*-
# author:Lizengxin
# datetime:2019/8/23 10:23
# software: PyCharm
import socks   #设置全局端口代理
import requests
import time
import socket
import stem #换ip
from stem import Signal #信号
from stem.control import  Controller #控制器

controller=Controller.from_port(port=9151) #端口转发，
controller.authenticate() #控制器，换ip

#tor   9150默认 的端口
socks.set_default_proxy(socks.SOCKS5,"127.0.0.1",9150)
socket.socket=socks.socksocket #用这个代理登录
for   i   in range(10):
    print(i,requests.get("http://checkip.amazonaws.com").text)
    controller.signal(Signal.NEWNYM)
    time.sleep(5)