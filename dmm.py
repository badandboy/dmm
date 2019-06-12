#coding:utf-8
import os
import time
import random

num = 41
# 获取屏幕尺寸
# adb = "adb shell wm size"
# print(os.system(adb))

for i in range(1, num):
    print(i)
    # 领喵币
    adb5 = "adb shell input tap 900 1600"
    os.system(adb5)
    rand = random.randint(1,5)
    time.sleep(rand)

    # 去逛店
    adb1 = "adb shell input tap 1050 1300"
    os.system(adb1)
    time.sleep(12)

    # 睡眠12,点击得喵币
    adb2 = "adb shell input tap 1050 1150"
    os.system(adb2)
    rand = random.randint(1,5)
    time.sleep(rand)

    # 点击开心收下
    adb3 = "adb shell input tap 545 1590"
    os.system(adb3)
    rand = random.randint(1,5)
    time.sleep(rand)

    #返回到喵页面
    adb4 = "adb shell input keyevent 4 "
    os.system(adb4)
    rand = random.randint(1,5)
    time.sleep(rand)