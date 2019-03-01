from play import *
from auto import *
from click import Click, Tap, drug

ScriptCount = 0
# 菜单字样的图片
outerImage = ac.imread('out_anchor.png')
# 期望的助战
helperImage = ac.imread('%s.png' % 期望的助战)


# 自动选择助战
def FindHelper():
    if helperImage is not None:
        while True:
            for i in range(6):
                srcImage = cut(savePicture=False)
                pos = ac.find_template(srcImage, helperImage)
                if pos is not None and pos['confidence'] > 0.9:
                    pos_r = pos['rectangle']
                    pos_y = (pos_r[0][1] + pos_r[1][1])//4
                    pos_x = pos_r[-1][0]//2 + 200
                    Click((pos_x, pos_y), 1.0)
                    return
                drug()
                Delay(0.5)
            Delay(3.0)
            Tap('\\', 普通操作时间)
            Tap('\'', 刷新助战时间)


while True:
    print('开始脚本，当前完成次数:%d' % ScriptCount)
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

