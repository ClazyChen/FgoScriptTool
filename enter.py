from play import *
from auto import *
from click import Click, Tap, drug
from cut import match

ScriptCount = 0
# 菜单字样的图片
outerImage = ac.imread('out_anchor.png')
# 期望的助战
helperImage = ac.imread('%s.png' % 期望的助战)
# AP回复界面
apImage = ac.imread('ap_anchor.png')
# 金银铜苹果
goldImage = ac.imread('gold_apple_anchor.png')
sliverImage = ac.imread('silver_apple_anchor.png')
copperImage = ac.imread('copper_apple_anchor.png')


# 自动选择助战
def FindHelper():
    if helperImage is not None:
        while True:
            for i in range(6):
                srcImage = cut(savePicture=False)
                pos = ac.find_template(srcImage, helperImage)
                if pos is not None and pos['confidence'] > 0.9:
                    pos_r = pos['rectangle']
                    pos_y = int((pos_r[0][1] + pos_r[1][1])/2/缩放倍率)
                    pos_x = int((pos_r[-1][0] + 400)/缩放倍率)
                    Click((pos_x, pos_y), 1.0)
                    return
                drug()
                Delay(0.5)
            Delay(3.0)
            Tap('\\', 普通操作时间)
            Tap('\'', 刷新助战时间)


# 自动吃苹果
def EatApple():
    if match(apImage):
        drug()
        Delay(1.0)
        if 允许食用铜苹果 and match(copperImage):
            Tap('D', 普通操作时间)
            Tap('\'', 普通操作时间)
            return
        if 允许食用银苹果 and match(sliverImage):
            Tap('8', 普通操作时间)
            Tap('\'', 普通操作时间)
            return
        if 允许食用金苹果 and match(goldImage):
            Tap('E', 普通操作时间)
            Tap('\'', 普通操作时间)
            return
        if 允许食用圣晶石:
            pos_x = int(800/缩放倍率)
            pos_y = int(135/缩放倍率)
            Click((pos_x, pos_y), 普通操作时间)
            Tap('\'', 普通操作时间)
            return


while True:
    print('开始脚本，当前完成次数:%d' % ScriptCount)
    EatApple()
    Delay(1.0)
    FindHelper()
    Delay(1.0)
    Tap(' ', 普通操作时间)
    WaitUntilNext()
    脚本()
    Tap('D', 点掉羁绊结算窗口时间)
    Tap('D', 点掉经验结算窗口时间)
    Tap(' ', 普通操作时间)
    WaitUntil(outerImage, 1.0, 1.0)
    Tap('1', 普通操作时间)
    ScriptCount += 1

