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
    tap_key(' ', 进本时间)
    脚本()
    tap_key('D', 点掉羁绊结算窗口时间)
    tap_key('D', 点掉经验结算窗口时间)
    tap_key(' ', 出本时间)
    tap_key('1', 普通操作时间)
    op += 1
    print('等待操作，当前完成次数：%d' % op)
    SetForegroundWindow(find_window(title=FGO窗口名))
    input()
