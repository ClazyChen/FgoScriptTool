# -*- coding: utf-8 -*-

from pykeyboard import PyKeyboard
from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
from pywinauto.win32functions import GetForegroundWindow
import time
import os
import aircv as ac
import numpy as np
import cv2
from config import *
from cut import cut

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
阵容卡组 = {}
remain_phase_number = 3
master_image = ac.imread('master_anchor.png') if 自动选卡策略 else None
ban_image = ac.imread('ban_anchor.png') if 自动选卡策略 else None
apple_image = ac.imread('apple.png') if 自动选卡策略 else None
stone_image = ac.imread('stone.png') if 自动选卡策略 else None


def wait_until_next_phase():
    while True:
        src_image = cut(save_picture=False)
        pos = ac.find_template(src_image,
                               master_image if remain_phase_number > 0 else ban_image)
        if pos is not None and pos['confidence'] > 0.95:
            break
        等待(1.0)
    等待(0.2 if remain_phase_number > 0 else 1.0)


def treasure_time(servant_name):
    for test_time in 宝具时间.keys():
        if servant_name in 宝具时间[test_time]:
            return test_time
    return 18.0


def 设置阵容(目标阵容, 面数=3):
    global 阵容
    global 阵容卡组
    global remain_phase_number
    remain_phase_number = 面数
    阵容 = 目标阵容
    if 自动选卡策略:
        color_list = ['R', 'B', 'G']
        color_name_map = {
            'R': '红',
            'B': '蓝',
            'G': '绿'
        }
        for servant_name in 阵容:
            servant_true_name = servant_name
            if servant_name[-1] in '12':
                servant_true_name = servant_name[:-1]
            servant_cardset = {}
            for color in color_list:
                temp_list = []
                temp_index = 1
                while os.path.exists('cardset\\%s-%s-%d.png'
                                     % (servant_true_name, color, temp_index)):
                    temp_list.append(cv2.imdecode(np.fromfile('cardset\\%s-%s-%d.png'
                                     % (servant_true_name, color, temp_index),
                                       dtype=np.uint8), -1))
                    temp_index += 1
                servant_cardset[color_name_map[color]] = temp_list
            阵容卡组[servant_name] = servant_cardset


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


def 匹配(order, mode):
    user, card_type = tuple(order.split('-'))
    mode_user, mode_card_type = tuple(mode.split('-'))
    if mode_user != '任意' and mode_user != user:
        return False
    return mode_card_type == '任意' or mode_card_type == card_type


def 查找从者(从者名):
    for i in range(6):
        if 阵容[i] == 从者名:
            return i
    return 0


# 进行匹配操作，返回一个选卡方式
def 选卡匹配(选卡策略, 给定卡组):
    card_pos = []
    for 选卡 in 选卡策略:
        user, card_type = tuple(选卡.split('-'))
        if card_type == '宝具':
            card_pos.append('WER'[查找从者(user)])
        else:
            card_pos.append(''.join([
                'ASDFG'[i] for i in range(5)
                if 匹配(给定卡组[i], 选卡)
            ]))
    used_key = []
    for c in card_pos[0]:
        used_key.append(c)
        for d in card_pos[1]:
            if d not in used_key:
                used_key.append(d)
                for e in card_pos[2]:
                    if e not in used_key:
                        used_key.append(e)
                        return used_key
                used_key.remove(d)
        used_key.remove(c)
    return []


def 宝具(user, 手动选卡=False, 敌对目标=0, 选卡策略=[]):
    global remain_phase_number
    if 敌对目标 > 0:
        tap_key('234'[敌对目标-1], 普通操作时间)
    tap_key('\n', 进入选卡界面时间)
    index = 查找从者(user)
    # 识别5张牌都是啥
    # 5张牌在标准化图片（992*611）上的位置：
    # （10+200X,300）-（190+200X,5320），X=0,1,2,3,4
    if 自动选卡策略:
        src_image = cv2.resize(cut(save_picture=False), (992, 611))
        found_card_list = []
        for i in range(5):
            card_area_image = src_image[300:520, 10+200*i:190+200*i]
            found = '未定义-未定义'
            for servant_name in 阵容[:3]:
                if servant_name != '':
                    for color in ['红', '蓝', '绿']:
                        for test_image in 阵容卡组[servant_name][color]:
                            pos = ac.find_template(card_area_image, test_image)
                            # 这里有一个助战图标的问题
                            if pos is not None and pos['confidence'] > 0.8:
                                found = '%s-%s' % (servant_name, color)
                                break
                                break
                                break
            found_card_list.append(found)

    print('检测结果:')
    print(found_card_list)

    if not 手动选卡:
        result = []
        if 自动选卡策略:
            for 策略 in 选卡策略:
                # 试图匹配策略
                result = 选卡匹配(策略, found_card_list)
                if len(result) > 0:
                    break
        if len(result) == 0:
            result = ['WER'[index], 'S', 'D']
        tap_key(result[0], 普通操作时间)
        tap_key(result[1], 普通操作时间)
        if not 自动选卡策略:
            tap_key(result[2], treasure_time(user) + 换面时间)
        else:
            tap_key(result[2], 普通操作时间)
            remain_phase_number -= 1
            print('剩余面数：%d' % remain_phase_number)
            wait_until_next_phase()
            if remain_phase_number <= 0:
                remain_phase_number = 3
    else:
        tap_key('WER'[index], 普通操作时间)
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
