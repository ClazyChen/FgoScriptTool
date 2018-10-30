# -*- coding: utf-8 -*-

# 每次将模拟器滑到适当的位置，然后cmd里敲回车
# 完成截图之后继续下一次操作

from cut import cut
from processor import process_cut
from pywinauto.win32functions import SetForegroundWindow, GetForegroundWindow

print('截图助手已启动')
print('输入已进行的次数：')
op = input()
try:
    op = int(op)
except ValueError:
    op = 0

while True:
    print('已完成%d次截图，回车以开始下一次……' % op)
    input()
    original_window = GetForegroundWindow()
    cut()
    process_cut(start_index=op*5)
    SetForegroundWindow(original_window)
    op += 1
