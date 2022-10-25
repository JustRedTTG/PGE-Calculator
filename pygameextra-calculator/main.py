import pygameextra as pe
import os

pe.init()

pe.display.make((215, 170), 'Calculator')  # makes a display


def title():
    os.system('clear')
    print('Pygame Extra calculator by RedstoneHair')


title()
# rects
multyplyr = (0, 59, 53, 56)
divider = (53, 59, 53, 56)
addr = (0, 115, 53, 56)
subtractr = (53, 115, 53, 56)
enterr = (166 + 19, 149, 30, 21)
dotr = (106 + 19, 149, 30, 21)
deleter = (106, 59, 19, 42)
clearr = (106, 101, 19, 42)
exitr = (106, 143, 19, 28)
numbersr = [
    (136 + 19, 149, 30, 21),
    (106 + 19, 59, 30, 30),
    (136 + 19, 59, 30, 30),
    (166 + 19, 59, 30, 30),
    (106 + 19, 89, 30, 30),
    (136 + 19, 89, 30, 30),
    (166 + 19, 89, 30, 30),
    (106 + 19, 119, 30, 30),
    (136 + 19, 119, 30, 30),
    (166 + 19, 119, 30, 30),
]
# text
multyplyt = pe.text.quick.small('X', pe.math.center(multyplyr))
dividet = pe.text.quick.small('/', pe.math.center(divider))
addt = pe.text.quick.small('+', pe.math.center(addr))
subtractt = pe.text.quick.small('-', pe.math.center(subtractr))
entert = pe.text.quick.small('=', pe.math.center(enterr))
dott = pe.text.quick.small('.', pe.math.center(dotr))
deletet = pe.text.quick.small('<', pe.math.center(deleter))
cleart = pe.text.quick.small('C', pe.math.center(clearr))
exitt = pe.text.quick.small('~', pe.math.center(exitr))
math = pe.text.make('0', 'freesansbold.ttf', 20, pe.math.center((0, 0, 215, 59)), [(255, 255, 255), None])
numberst = [None] * len(numbersr)
i = 0
for x in numbersr:
    numberst[i] = pe.text.quick.small(str(i), pe.math.center(x))
    i = i + 1

# color
highlight = (200, 200, 200)
normal = (180, 180, 180)
background = (50, 50, 50)
math.setup(math)
math.background = background
math.init(math)
valueR = None
updatemath = True
op = None
opdone = True


def mu():  # mu is Math Update aka, it updates the text element!
    global value
    global math
    global updatemath
    updatemath = True
    math.text = str(value)
    math.init(math)


def enter():
    global value
    global valueR
    global math
    global updatemath
    global opdone
    global op
    global dote
    print('calculate')
    if op == None:
        math.text = '= ' + str(value)
        math.init(math)
        updatemath = True
        return
    else:
        if float(value) == 0.0 or float(valueR) == 0.0:
            if False:  # Reserved slot
                math.text = 'Syntax Error ' + str(valueR) + '&' + str(value)
            elif op == 1:
                math.text = 'Syntax Error ' + str(valueR) + '/' + str(value)
            else:
                return
            math.init(math)
            updatemath = True
        if op == 0:
            v = float(valueR) * float(value)
            if not '.0' in str(v):
                dote = True
                value = float(v)
            else:
                dote = False
                value = int(v)
            op = None
            opdone = True
        if op == 1:
            v = float(valueR) / float(value)
            if not '.0' in str(v):
                dote = True
                value = float(v)
            else:
                dote = False
                value = int(v)
            op = None
            opdone = True
        if op == 2:
            v = float(valueR) + float(value)
            if not '.0' in str(v):
                dote = True
                value = float(v)
            else:
                dote = False
                value = int(v)
            op = None
            opdone = True
        if op == 3:
            v = float(valueR) - float(value)
            if not '.0' in str(v):
                dote = True
                value = float(v)
            else:
                dote = False
                value = int(v)
            op = None
            opdone = True
        math.text = '= ' + str(value)
        math.init(math)
        updatemath = True


def multyply():
    global value
    global valueR
    global math
    global updatemath
    global dote
    global op
    global opdone
    updatemath = True
    print('multyply')
    if valueR == None:
        print('math ok')
        math.text = 'X'
        math.init(math)
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' X'
            math.init(math)
        else:
            math.text = 'X'
            math.init(math)
    if opdone:
        valueR = value
        value = '0'
        dote = False
        op = 0
        opdone = False


def divide():
    global value
    global valueR
    global math
    global updatemath
    global dote
    global op
    global opdone
    updatemath = True
    print('divide')
    if valueR == None:
        print('math ok')
        math.text = '/'
        math.init(math)
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' /'
            math.init(math)
        else:
            math.text = '/'
            math.init(math)
    if opdone:
        valueR = value
        value = '0'
        dote = False
        op = 1
        opdone = False


def add():
    global value
    global valueR
    global math
    global updatemath
    global dote
    global op
    global opdone
    updatemath = True
    print('add')
    if valueR == None:
        print('math ok')
        math.text = '+'
        math.init(math)
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' +'
            math.init(math)
        else:
            math.text = '+'
            math.init(math)
    if opdone:
        valueR = value
        value = '0'
        dote = False
        op = 2
        opdone = False


def subtract():
    global value
    global valueR
    global math
    global updatemath
    global dote
    global op
    global opdone
    updatemath = True
    print('subtract')
    if valueR == None:
        print('math ok')
        math.text = '-'
        math.init(math)
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' -'
            math.init(math)
        else:
            math.text = '-'
            math.init(math)
    if opdone:
        valueR = value
        value = '0'
        dote = False
        op = 3
        opdone = False


def number(num):
    global value
    global dote
    global opdone
    opdone = True
    print(num)
    if value == 0:
        value = num
    else:
        if dote:
            value = float(str(value) + str(num))
        else:
            value = int(str(value) + str(num))
    mu()


def dot():
    global value
    global dote
    print('dot')
    value = str(value) + '.'
    dote = True
    mu()


def delete():
    global value
    global valueR
    global math
    global updatemath
    global dote
    strv = str(value)
    value = strv[0:len(strv) - 1]
    if '.' in value:
        dote = True
    else:
        dote = False
    mu()


def clear():
    global math
    global updatemath
    global value
    global op
    global opdone
    global valueR
    valueR = None
    updatemath = True
    op = None
    opdone = True
    math.text = '0'
    math.init(math)
    title()

pe.fill.full(background)  # fills the screen with white
value = 0
dote = False
run = True

def exit_calc():
    global run
    run = False

while run:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    if updatemath:
        pe.draw.rect(background, (0, 0, 170, 59), 0)
        pe.text.display(math)
        updatemath = False
    pe.button.rect(multyplyr, normal, highlight, multyplyt, multyply)
    pe.button.rect(divider, normal, highlight, dividet, divide)
    pe.button.rect(addr, normal, highlight, addt, add)
    pe.button.rect(subtractr, normal, highlight, subtractt, subtract)
    pe.button.rect(enterr, (50, 255, 50), (150, 255, 150), entert, enter)
    pe.button.rect(dotr, normal, highlight, dott, dot)
    pe.button.rect(deleter, (255, 128, 0), (255, 155, 0), deletet, delete)
    pe.button.rect(clearr, (255, 128, 0), (255, 155, 0), cleart, clear)
    pe.button.rect(exitr, (255, 0, 0), (255, 100, 100), exitt, exit_calc)
    i = 0
    for x in numberst:
        pe.button.rect(numbersr[i], normal, highlight, x, number, i)
        i = i + 1
    # pe.sleep(10)
    pe.pygame.time.Clock().tick(60)
    pe.display.update()
pe.Pquit()
exit()
