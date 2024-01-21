from sample.view import console

DEFAULT_ROBOT_NAME = '11-O'

class Robot:
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color
    
    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)