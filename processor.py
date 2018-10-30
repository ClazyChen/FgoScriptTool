# -*- coding: utf-8 -*-

import aircv as ac
import cv2


def process_cut(start_index=0):
    order_anchor_image = ac.imread('order_anchor.png')
    src_image = ac.imread('pic.png')

    # 标准截图左上角应该是(668, X)
    # 最左边的Quick卡是这个截图位置加一个截距(34, 72)
    # 一张卡的大小是121 × 156
    # 两张卡的距离为178

    pos = ac.find_template(src_image, order_anchor_image)
    pos_x, pos_y = pos['rectangle'][0]

    delta_x = 34
    delta_y = 72
    card_w = 121
    card_h = 156
    delta_card = 178

    for i in range(5):
        crop_image = src_image[pos_y+delta_y:pos_y+delta_y+card_h,
                     pos_x+delta_x+delta_card*i:pos_x+delta_x+delta_card*i+card_w]
        cv2.imwrite("pic\\card%d.png" % (i + start_index), crop_image)

    print('已保存指令卡截图……')