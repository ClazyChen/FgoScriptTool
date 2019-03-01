# -*- coding: utf-8 -*-

import win32gui
import win32api
import win32con
from time import sleep
from random import randint
from config import *


# 获取窗口上方标题栏的高度
def GetWindowHeaderHeight(windowName=FGO窗口名):
    hwnd = win32gui.FindWindow(None, windowName)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    h = bottom - top
    return h * 2 - 900


# 用键盘映射获取x和y的坐标
# 键盘映射为旧版FGO Script的标准，详见README
def GetButtonPositionByKey(key):
    x, y = {
        '\n': (1420, 760),
        ' ': (1485, 850),
        'Z': (90, 725),
        'X': (205, 725),
        'C': (320, 725),
        'V': (490, 725),
        'B': (605, 725),
        'N': (720, 725),
        'M': (890, 725),
        ',': (1005, 725),
        '.': (1120, 725),
        'A': (160, 630),
        'S': (480, 630),
        'D': (800, 630),
        'F': (1120, 630),
        'G': (1440, 630),
        'W': (515, 255),
        'E': (800, 255),
        'R': (1085, 255),
        ']': (1495, 395),
        'O': (1135, 395),
        'P': (1245, 395),
        '[': (1355, 395),
        '5': (175, 435),
        '6': (425, 435),
        '7': (675, 435),
        '8': (925, 435),
        '9': (1175, 435),
        '0': (1425, 435),
        '-': (800, 790),
        '2': (60, 55),
        '3': (360, 55),
        '4': (660, 55),
        '1': (1220, 225),
        'J': (400, 560),
        'K': (800, 560),
        'L': (1200, 560),
        '\\': (1045, 165),
        ';': (550, 705),
        '\'': (1050, 705)
    }[key]
    return x//2, (y + GetWindowHeaderHeight())//2


# 键盘映射Q键代表上划
# 按照README的做法，应该允许划6下
def drug(windowName=FGO窗口名):
    hwnd = win32gui.FindWindow(None, windowName)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 1)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x51, 0)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x51, 0)
    sleep(0.02+randint(0, 10)/1000.0)


# 点击一个点，默认随机误差为±5，随机延长0.00~0.01秒
# 在点击之后等待delayTime时间，默认的等待时间为0.0s
def Click(position, delayTime=0.0, randRange=(2, 2), windowName=FGO窗口名):
    hwnd = win32gui.FindWindow(None, windowName)
    x, y = position
    x += randint(-randRange[0], randRange[0])
    y += randint(-randRange[1], randRange[1])
    pos = win32api.MAKELONG(x, y)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 1)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.VK_LBUTTON, pos)
    sleep(0.01)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, pos)
    sleep(0.02+randint(0, 10)/1000.0)
    sleep(delayTime)


# 按下一个按键，不过在实际操作中以点击形式体现
def Tap(key, delayTime=0.0, randRange=(2, 2), windowName=FGO窗口名):
    Click(GetButtonPositionByKey(key), delayTime, randRange, windowName)
