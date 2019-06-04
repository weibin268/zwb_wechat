import os
import sys
import itchat
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply2(msg):
    print(msg.text)
    os.system(msg.text)
    msg.user.send('%s: %s' % (msg.type, msg.text))

itchat.auto_login()
itchat.run()