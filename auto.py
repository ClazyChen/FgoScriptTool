# -*- coding: utf-8 -*-

from pykeyboard import PyKeyboard
from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
from pywinauto.win32functions import GetForegroundWindow
import time
from config import *

k = PyKeyboard()


def tap_key(key, delay=1.0):
    if 操作完后回到原来窗口:
        original_window = GetForegroundWindow()
        SetForegroundWindow(find_window(title=FGO窗口名))
    k.tap_key(key)
    time.sleep(0.02)
    if 操作完后回到原来窗口:
        SetForegroundWindow(original_window)
    time.sleep(delay)


阵容 = []


def treasure_time(servant_name):
    for test_time in 宝具时间.keys():
        if servant_name in 宝具时间[test_time]:
            return test_time
    return 18.0


def 设置阵容(目标阵容):
    global 阵容
    阵容 = 目标阵容


def 使用技能(user, index, 目标='', 敌对目标=0):
    if 敌对目标 > 0:
        tap_key('234'[敌对目标-1], 普通操作时间)
    if 目标 == '':
        if user == 阵容[0]:
            tap_key('ZXC'[index-1], 放技能后等待时间)
        elif user == 阵容[1]:
            tap_key('VBN'[index-1], 放技能后等待时间)
        elif user == 阵容[2]:
            tap_key('M,.'[index-1], 放技能后等待时间)
        elif '咕哒' in user:
            tap_key(']', 普通操作时间)
            tap_key('OP['[index-1], 放技能后等待时间)
    else:
        if user == 阵容[0]:
            tap_key('ZXC'[index-1], 放技能弹出选择目标窗口时间)
        elif user == 阵容[1]:
            tap_key('VBN'[index-1], 放技能弹出选择目标窗口时间)
        elif user == 阵容[2]:
            tap_key('M,.'[index-1], 放技能弹出选择目标窗口时间)
        elif '咕哒' in user:
            tap_key(']', 普通操作时间)
            tap_key('OP['[index-1], 放技能弹出选择目标窗口时间)
        if 目标 == 阵容[0]:
            tap_key('J', 放技能选择目标后等待时间)
        elif 目标 == 阵容[1]:
            tap_key('K', 放技能选择目标后等待时间)
        elif 目标 == 阵容[2]:
            tap_key('L', 放技能选择目标后等待时间)


def 换人(servant1, servant2):
    index1 = -1
    index2 = -1
    for i in range(6):
        if 阵容[i] == servant1:
            index1 = i
        if 阵容[i] == servant2:
            index2 = i
    tap_key('567890'[index1], 普通操作时间)
    tap_key('567890'[index2], 普通操作时间)
    temp = 阵容[index1]
    阵容[index1] = 阵容[index2]
    阵容[index2] = temp
    tap_key('-', 换人时间)


def 等待(delay):
    time.sleep(delay)


def 宝具(user, 手动选卡=False, 敌对目标=0):
    if 敌对目标 > 0:
        tap_key('234'[敌对目标-1], 普通操作时间)
    tap_key('\n', 进入选卡界面时间)
    index = -1
    for i in range(6):
        if 阵容[i] == user:
            index = i
    tap_key('WER'[index], 普通操作时间)
    if not 手动选卡:
        tap_key('S', 普通操作时间)
        tap_key('D', treasure_time(user) + 换面时间)
    else:
        等待操作()
        等待(treasure_time(user) + 换面时间)
    if user == '大英雄':
        阵容[index] = 阵容[3]
        阵容[3] = 阵容[4]
        阵容[4] = 阵容[5]
        阵容[5] = ''


def 等待操作():
    print('等待操作')
    SetForegroundWindow(find_window(title=FGO窗口名))
    input()
