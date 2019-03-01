# -*- coding: utf-8 -*-

import win32gui
import win32ui
import win32con
from PIL import Image

from config import *
import numpy as np


# cut函数提供了一个对FGO窗口进行截图的方法
# 要求FGO窗口处在1600×900的分辨率下
# 且Mumu模拟器设置为隐藏下方工具栏
# 这个函数会把上方工具栏截掉，留下1600×900的图像以供后期操作
def cut(savePicture=True, windowName=FGO窗口名):
    hwnd = win32gui.FindWindow(None, windowName)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bottom - top

    # 这个地方需要手动调整
    # 这里的2代表windows的“显示大小”设置为200%
    # 因为作者的电脑分辨率过高，所以为200%
    w *= 2
    h *= 2

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)

    img_dc = mfcDC
    mem_dc = saveDC
    mem_dc.BitBlt((0, 0), (w, h), img_dc, (0, 0), win32con.SRCCOPY)
    bmpInfo = saveBitMap.GetInfo()
    bmpStr = saveBitMap.GetBitmapBits(True)

    srcImage = Image.frombuffer('RGB', (bmpInfo['bmWidth'], bmpInfo['bmHeight']), bmpStr, 'raw', 'BGRX', 0, 1)
    srcImage = srcImage.convert('L').convert('RGB').crop((0, h - 900, w, h))
    if savePicture:
        srcImage.save('pic.png')
        print("截图已保存……")
    return np.array(srcImage)
