# -*- coding: utf-8 -*-

# 将截图转换成csv文件准备训练神经网络

from config import servant_index_map
from PIL import Image
import numpy as np

print('输入开始标注的编号：')
index = input()

try:
    index = int(index)
except ValueError:
    print('输入值非法')
    index = 0

while True:
    print('当前标注的指令卡编号：%d 到 %d' % (index, index+4))
    while True:
        print('输入对应的从者名（简称在config.py里规定）：')
        servant_name = input()
        if servant_name in servant_index_map.keys():
            break
        print("没有找到该从者，请重新输入")
    servant_index = servant_index_map[servant_name]
    while True:
        print('输入配卡：')
        card_array = input()
        if len(card_array) != 5:
            print('需要输入五个字符')
            continue
        for c in card_array:
            if c not in ('a', 'b', 'q'):
                print('只能输入abq')
                break
                continue
        break
    card_indices = [1 if c == 'q' else 2 if c == 'a' else 3 for c in card_array]
    for i in range(index, index+5):
        image = Image.open('pic\\card%d.png' % i)
        image_array = np.array(image)
        f = open('csv\\card%d.csv' % i, 'w', encoding='utf-8')
        f.write('%d,%d' % (servant_index, card_indices[i - index]))
        for row in image_array:
            for pix in row:
                f.write(',%d' % pix[0])
        f.close()

    index += 5
