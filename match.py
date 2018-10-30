# -*- coding: utf-8 -*-

import aircv as ac
import cv2

# 我大胆猜测只要用aircv的匹配就可以识别

tried_image = ac.imread('pic\\card10.png')
src_image = cv2.resize(ac.imread('pic.png'), (992, 612))

pos = ac.find_template(src_image, tried_image)

print(pos)

# 好吧识别成功了，再见卷积神经网络，我不训练你了
