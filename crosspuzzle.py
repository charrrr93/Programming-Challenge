import itertools
from tkinter import *


def test(vars, tests, number):
    test = tests[number]
    test_string = '(' + str(vars[test[0]]) + test[1] + str(vars[test[2]]) + ')' + test[3] + str(vars[test[4]])
    if eval(test_string) == int(test[5]):
        return True
    else:
        return False


def helppopup():
    windowpopup = Tk()
    windowpopup.title("Help")
    Label(windowpopup, text="Enter the cross maths puzzle into the white squares and click\n"
          "\"Solve Puzzle\" to fill in the yellow squares with the answers.", 
          font=("Arial Bold", 10)).pack()


def clicked():
    for entry in squareEntries:
        squareVars.append(entry.get())

    tests = createtests(squareVars)

    print(tests)

    results = solvepuzzle(tests)

    Label(window, text=results['a'], font=("Arial Bold", 50), width=2).grid(column=1, row=1)
    Label(window, text=results['b'], font=("Arial Bold", 50), width=2).grid(column=3, row=1)
    Label(window, text=results['c'], font=("Arial Bold", 50), width=2).grid(column=5, row=1)
    Label(window, text=results['d'], font=("Arial Bold", 50), width=2).grid(column=1, row=3)
    Label(window, text=results['e'], font=("Arial Bold", 50), width=2).grid(column=3, row=3)
    Label(window, text=results['f'], font=("Arial Bold", 50), width=2).grid(column=5, row=3)
    Label(window, text=results['g'], font=("Arial Bold", 50), width=2).grid(column=1, row=5)
    Label(window, text=results['h'], font=("Arial Bold", 50), width=2).grid(column=3, row=5)
    Label(window, text=results['i'], font=("Arial Bold", 50), width=2).grid(column=5, row=5)



def createtests(symbols):
    tests = [['a', symbols[3], 'b', symbols[9], 'c', symbols[15]],
             ['a', symbols[0], 'd', symbols[1], 'g', symbols[2]],
             ['d', symbols[4], 'e', symbols[10], 'f', symbols[16]],
             ['b', symbols[6], 'e', symbols[7], 'h', symbols[8]],
             ['g', symbols[5], 'h', symbols[11], 'i', symbols[17]],
             ['c', symbols[12], 'f', symbols[13], 'i', symbols[14]]]
    return tests


def solvepuzzle(tests):
    for item in list(itertools.product(count, count, count)):
        if len(item) == len(dict.fromkeys(item)):
            vars['a'] = item[0]
            vars['b'] = item[1]
            vars['c'] = item[2]
            if test(vars, tests, 0):
                for item2 in list(itertools.product(count, count)):
                    if len(item + item2) == len(dict.fromkeys(item + item2)):
                        vars['d'] = item2[0]
                        vars['g'] = item2[1]
                        if test(vars, tests, 1):
                            for item3 in list(itertools.product(count, count, count, count)):
                                if len(item + item2 + item3) == len(dict.fromkeys(item + item2 + item3)):
                                    vars['e'] = item3[0]
                                    vars['f'] = item3[1]
                                    vars['h'] = item3[2]
                                    vars['i'] = item3[3]
                                    if test(vars, tests, 2) and test(vars, tests, 3) and test(vars, tests, 4) and test(vars, tests, 5):
                                        return vars
                                    else:
                                        vars['e'] = 0
                                        vars['f'] = 0
                                        vars['h'] = 0
                                        vars['i'] = 0
                        else:
                            vars['d'] = 0
                            vars['g'] = 0
            else:
                vars['a'] = 0
                vars['b'] = 0
                vars['c'] = 0

count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vars = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}

squareEntries = []
squareResults = []
squareVars = []
equalSquares = [5, 19, 33, 35, 37, 39]
greySquares = [8, 10, 12, 13, 22, 24, 26, 27, 36, 38, 40, 41, 43, 45, 47, 48]
colouredSquares = [1, 3, 6, 7, 9, 11, 15, 17, 20, 21, 23, 25, 29, 31, 34, 42, 44, 46]

window = Tk()
window.title("Cross Maths Puzzle")
squareCount = 0
for i in range(1, 8):
    for j in range(1, 8):
        if squareCount in equalSquares:
            Label(window, text="=", font=("Arial Bold", 50), width=1, justify=CENTER).grid(column=i, row=j) 
        elif squareCount in greySquares:
            Entry(window, font=("Arial Bold", 50), width=2, state='disabled').grid(column=i, row=j)
        elif squareCount in colouredSquares:
            entry = Entry(window, font=("Arial Bold", 50), width=2, justify=CENTER)
            squareEntries.append(entry)
            entry.grid(column=i, row=j)
        else:
            entry = Entry(window, font=("Arial Bold", 50), width=2, bg="old lace", justify=CENTER)
            squareResults.append(entry)
            entry.grid(column=i, row=j)
        squareCount += 1
button = Button(window, text="Solve Puzzle", command=clicked, font=("Arial Bold", 30), justify=CENTER)
button.grid(column=4, row=8, columnspan=4)
button = Button(window, text="Help", command=helppopup, font=("Arial Bold", 30), justify=CENTER)
button.grid(column=1, row=8, columnspan=2)
mainloop()
