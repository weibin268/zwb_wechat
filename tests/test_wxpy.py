import time
from wxpy import Bot


bot = Bot()
my_friend = bot.friends().search('庄伟斌')[0]

for i in range(100):
    time.sleep(1)
    my_friend.send('Hello WeChat!'+str(i))


print(my_friend)
