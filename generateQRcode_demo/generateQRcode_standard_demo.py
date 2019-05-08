#author: hanshiqiang365 （微信公众号：韩思工作室）

import qrcode

words='http://weixin.qq.com/r/DkyxqYPE_96ErcfK9xkc'

img = qrcode.make(words)
img.save('qrcode.png')
img.show()

