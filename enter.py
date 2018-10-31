from pykeyboard import PyKeyboard
from pywinauto.win32functions import SetForegroundWindow
from config import *
from auto import *
from play import *

k = PyKeyboard()
op = 0

while True:
    print('开始脚本，当前完成次数：%d' % op)
    SetForegroundWindow(find_window(title=FGO窗口名))
    if 自动选卡策略:
        tap_key(' ', 普通操作时间)
        wait_until_next_phase()
    else:
        tap_key(' ', 进本时间)
    脚本()
    tap_key('D', 点掉羁绊结算窗口时间)
    tap_key('D', 点掉经验结算窗口时间)
    tap_key(' ', 出本时间)
    tap_key('1', 普通操作时间)
    if 自动选卡策略:
        src_image = cut(save_picture=False)
        if 自动吃苹果:
            pos = ac.find_template(src_image, apple_image)
            if pos is not None and pos['confidence'] > 0.95:
                tap_key('Q', 普通操作时间)
                tap_key('Y', 普通操作时间)
            elif 自动碎石:
                pos = ac.find_template(src_image, stone_image)
                if pos is not None and pos['confidence'] > 0.95:
                    tap_key('E', 普通操作时间)
                    tap_key('Y', 普通操作时间)
    op += 1
    print('等待操作，当前完成次数：%d' % op)
    SetForegroundWindow(find_window(title=FGO窗口名))
    input()
