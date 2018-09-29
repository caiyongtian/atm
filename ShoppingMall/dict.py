def add():
    print('add')

def sub():
    print('sub')

def exit():
    print('exit')

choice = { '1' : add, '2' : sub, '3' : exit}

item = input('please input your number! ')

if item in choice:
    choice[item]()