#coding=utf8
from werobot import WeRoBot
robot = WeRoBot(enable_session=False,
                token='sjtuaie.wcrobot',
                APP_ID='wx695d780fda31ff8f',
                APP_SECRET='04ffee7380dc6d87866ecea17ebd960a')

@robot.handler
def hello(message):
    return 'Hello world'

