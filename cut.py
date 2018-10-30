# -*- coding: utf-8 -*-

from pywinauto.findwindows    import find_window
from pywinauto.win32functions import ShowWindow, SetForegroundWindow, GetForegroundWindow
from win32gui import GetWindowRect
from win32con import SW_RESTORE
from PIL import ImageGrab

from config import *


def cut():
    hwnd = find_window(title=FGO窗口名)
    # ShowWindow(hwnd, SW_RESTORE)
    SetForegroundWindow(hwnd)

    # 截取FGO主窗口截图
    left, top, right, bottom = GetWindowRect(hwnd)
    src_image = ImageGrab.grab((left, top, right, bottom))

    src_image = src_image.convert('L')
    src_image.save('pic.png')
    print("截图已完成……")
