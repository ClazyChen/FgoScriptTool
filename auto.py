# -*- coding: utf-8 -*-

import win32gui
from time import sleep
import aircv as ac

from cut import cut
from config import *
from click import Tap

hwnd = win32gui.FindWindow(None, FGO窗口名)
team = []
remainPhases = 3

# Attack按钮的图像
masterImage = ac.imread('master_anchor.png')
# 羁绊窗口的图像
banImage = ac.imread('ban_anchor.png')


def Delay(delayTime):
    sleep(delayTime)


def GetNpTime(servantName):
    if servantName in 宝具时间.keys():
        return 宝具时间[servantName]
    return 默认宝具时间


def GetServantIndex(servantName):
    for i in range(len(team)):
        if team[i] == servantName:
            return i
    return 0


def WaitUntil(waitImage, beforeDelay, afterDelay):
    Delay(beforeDelay)
    while True:
        srcImage = cut(savePicture=False)
        pos = ac.find_template(srcImage, waitImage)
        if pos is not None and pos['confidence'] > 0.9:
            break
        Delay(1.0)
    Delay(afterDelay)


# 等待直到下一回合
# 现在默认一回合清一面
# 未来会改成第三回合允许补刀
def WaitUntilNext():
    WaitUntil(masterImage if remainPhases > 0 else banImage, 2.0, 1.2 if remainPhases > 0 else 3.0)


def SetTeam(targetTeam, phaseNumber=3):
    global team
    global remainPhases
    team = targetTeam
    remainPhases = phaseNumber


def UseSkill(user, index, target='', antiTarget=0):
    if antiTarget > 0:
        Tap('234'[antiTarget-1], 普通操作时间)
    waitTime = 放技能后等待时间 if target == '' else 放技能弹出选择目标窗口时间
    if '咕哒' in user:
        Tap(']', 普通操作时间)
        Tap('OP['[index - 1], waitTime)
    else:
        for i in range(3):
            if user == team[i]:
                Tap('ZXCVBNM,.'[i * 3 + index - 1], waitTime)
    for i in range(3):
        if target == team[i]:
            Tap('JKL'[i], 放技能选择目标后等待时间)


def Exchange(servant1, servant2):
    index1 = GetServantIndex(servant1)
    index2 = GetServantIndex(servant2)
    Tap('567890'[index1], 普通操作时间)
    Tap('567890'[index2], 普通操作时间)
    temp = team[index1]
    team[index1] = team[index2]
    team[index2] = temp
    Tap('-', 换人时间)


def NoblePhantasm(user, antiTarget=0):
    global remainPhases
    if antiTarget > 0:
        Tap('234'[antiTarget-1], 普通操作时间)
    userList = user.split('&')
    Tap('\n', 进入选卡界面时间)
    indices = map(GetServantIndex, userList)
    for index in indices:
        Tap('WER'[index], 普通操作时间)
    Tap('S', 普通操作时间)
    Tap('D', 普通操作时间)
    remainPhases -= 1
    WaitUntilNext()
    if remainPhases <= 0:
        remainPhases = 3
    if user == '大英雄':
        team[index] = team[3]
        team[3] = team[4]
        team[4] = team[5]
        team[5] = 'unknown'


# 中文版本的函数
def 换人(servant1, servant2):
    Exchange(servant1, servant2)


def 宝具(user, 敌对目标=0):
    NoblePhantasm(user, antiTarget=敌对目标)


def 使用技能(user, index, 目标='', 敌对目标=0):
    UseSkill(user, index, target=目标, antiTarget=敌对目标)


def 设置阵容(targetTeam, 面数=3):
    SetTeam(targetTeam, phaseNumber=面数)


def 等待(delayTime):
    Delay(delayTime)
