from icecream import ic
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

user = User('simple user', 'user')
admin = User('root', 'admin')

current_user = admin

def do_admin_work():
    if current_user.role != 'admin':
        raise Exception('Гуляй Вася!')
    return 'Осторожно! Работает админ.'

ic(do_admin_work())