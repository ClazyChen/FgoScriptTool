# -*- coding: utf-8 -*-

import aircv as ac
import cv2
import numpy as np
import cut

# 我大胆猜测只要用aircv的匹配就可以识别

tried_image = cv2.imdecode(np.fromfile("cardset\\孔明-R-3.png",
                                       dtype=np.uint8), -1)
# master_image = ac.imread('master_anchor.png')
src_image = cv2.resize(ac.imread('pic.png'), (992, 611))[300:520, 10:190]
# src_image = np.array(cut.cut(False))
# print(src_image)

pos = ac.find_template(src_image, tried_image)

print(pos)

# 好吧识别成功了，再见卷积神经网络，我不训练你了
