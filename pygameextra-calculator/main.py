import pygameextra as pe
import os
from math import ceil

pe.init((0, 0))
pe.display.make((215, 170), 'Calculator', pe.display.DISPLAY_MODE_RESIZABLE)  # makes a display
w, h = pe.display.get_size()


def title():
    os.system('clear')
    print('Pygame Extra calculator by RedTTG')


title()
mm: float
mm2: float
def init1():
	global mm, mm2
	mm = w / 215
	mm2 = h / 170
# rects
multyplyr: tuple = None
divider: tuple= None
addr: tuple= None
subtractr: tuple= None
enterr: tuple= None
dotr: tuple= None
deleter: tuple= None
clerr: tuple= None
exitr: tuple= None
numbersr: list= None
def init2():
	global multyplyr, divider, addr, subtractr, enterr, dotr, deleter, clearr, exitr, numbersr
	multyplyr = (0, ceil(59*mm2), ceil(53*mm), ceil(56*mm2))
	divider = (ceil(53*mm), ceil(59*mm2), ceil(53*mm), ceil(56*mm2))
	addr = (0, ceil(115*mm2), ceil(53*mm), ceil(56*mm2))
	subtractr = (ceil(53*mm), ceil(115*mm2), ceil(53*mm), ceil(56*mm2))
	enterr = (ceil(185*mm), ceil(149*mm2), ceil(30*mm), ceil(21*mm2))
	dotr = (ceil(125*mm), ceil(149*mm2), ceil(30*mm), ceil(21*mm2))
	deleter = (ceil(106*mm), ceil(59*mm2), ceil(19*mm), ceil(42*mm2))
	clearr = (ceil(106*mm), ceil(101*mm2), ceil(19*mm), ceil(42*mm2))
	exitr = (ceil(106*mm), ceil(143*mm2), ceil(19*mm), ceil(28*mm2))
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
	numbersr = [(ceil(x[0]*mm), ceil(x[1]*mm2), ceil(x[2]*mm), ceil(x[3]*mm2)) for x in numbersr]
# text
multyplyt: pe.text.Text = None
dividet: pe.text.Text = None
addt: pe.text.Text = None
subtractt: pe.text.Text = None
entert: pe.text.Text = None
dott: pe.text.Text = None
deletet: pe.text.Text = None
cleart: pe.text.Text = None
exitt: pe.text.Text = None
math: pe.text.Text = None
numberst: list = None
def init3(v='0'):
	global multyplyt, dividet, addt, subtractt, entert, dott, deletet, cleart, exitt, math, numberst
	font_size = int((20 * mm * mm2)/mm2)
	
	multyplyt = pe.text.quick('X', font_size, pe.math.center(multyplyr))
	dividet = pe.text.quick('/', font_size, pe.math.center(divider))
	addt = pe.text.quick('+', font_size, pe.math.center(addr))
	subtractt = pe.text.quick('-', font_size, pe.math.center(subtractr))
	entert = pe.text.quick('=', font_size, pe.math.center(enterr))
	dott = pe.text.quick('.', font_size, pe.math.center(dotr))
	deletet = pe.text.quick('<', font_size, pe.math.center(deleter))
	cleart = pe.text.quick('C', font_size, pe.math.center(clearr))
	exitt = pe.text.quick('~', font_size, pe.math.center(exitr))
	math = pe.text.Text(v, 'freesansbold.ttf', font_size, pe.math.center((0, 0, 215*mm, 59*mm2)), [(255, 255, 255), None])
	numberst = [None] * len(numbersr)
	for i, x in enumerate(numbersr):
	    numberst[i] = pe.text.quick(str(i), font_size, pe.math.center(x))

init1()
init2()
init3()

# color
highlight = (200, 200, 200)
normal = (180, 180, 180)
background = (50, 50, 50)
math.background = background
math.init()
valueR = None
updatemath = True
op = None
opdone = True


def mu():  # mu is Math Update aka, it updates the text element!
    global value
    global math
    global updatemath
    updatemath = True
    if op != None:
    	opc = '×' if op == 0 else '÷' if op == 1 else '+' if op == 2 else '-'
    	math.text = f'{valueR} {opc} {value}'
    else:
    	math.text = str(value)
    math.init()


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
        math.init()
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
            math.init()
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
        math.init()
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
    if op == 0: return
    print('multyply')
    if valueR == None:
        print('math ok')
        math.text = str(value) + ' ×'
        math.init()
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' ×'
            math.init()
        else:
            math.text = '×'
            math.init()
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
    if op == 1: return
    print('divide')
    if valueR == None:
        print('math ok')
        math.text = str(value) + ' ÷'
        math.init()
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' ÷'
            math.init()
        else:
            math.text = '÷'
            math.init()
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
    if op == 2: return
    print('add')
    if valueR == None:
        print('math ok')
        math.text = str(value) + ' +'
        math.init()
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' +'
            math.init()
        else:
            math.text = '+'
            math.init()
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
    if op == 3: return
    print('subtract')
    if valueR == None:
        print('math ok')
        math.text = str(value) + ' -'
        math.init()
    else:
        print('math not ok')
        if opdone:
            enter()
            math.text = str(value) + ' -'
            math.init()
        else:
            math.text = str(value) + ' -'
            math.init()
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
    value = 0
    valueR = None
    updatemath = True
    op = None
    opdone = True
    math.text = '0'
    math.init()
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
        if pe.event.resizeCheck():
        	pe.event.rundown()
        	w, h = pe.display.get_size()
        	init1()
        	init2()
        	init3(math.text)
        	updatemath = True
    if updatemath:
        pe.draw.rect(background, (0, 0, w, 59*mm2), 0)
        math.display()
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