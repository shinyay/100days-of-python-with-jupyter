from sample.view import console
from sample.model import ranking

DEFAULT_ROBOT_NAME = '11-O'

class Robot:
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color
    
    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute(
                {'robot_name': self.name}
            ))
            if user_name:
                self.user_name = user_name.title()
                break

class RestaurantRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name = name)
        self.ranking_model = ranking.RankingModel()
    
    def _hello_decorator(func):
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper