#author: hanshiqiang365 （微信公众号：韩思工作室）

from MyQR import myqr
import os
words='http://weixin.qq.com/r/DkyxqYPE_96ErcfK9xkc'
version, level, qr_name = myqr.run(
    words,
    version=1,
    level='H',
    picture="reversed_Ironman.gif",
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
)

