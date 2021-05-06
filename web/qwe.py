import easygui

def rock_paper_scissors():
    easygui.msgbox('Здесь будет игра "Камень, ножницы, бумага"')


def guess_the_number():
    easygui.msgbox('Здесь будет игра "Угадай число"')


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()