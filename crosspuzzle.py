tests = [['a', '+', 'b', '+', 'c', 15],
         ['a', '+', 'd', '-', 'g', 3],
         ['d', '+', 'e', '*', 'f', 24],
         ['b', '*', 'e', '-', 'h', 12],
         ['g', '+', 'h', '-', 'i', 14],
         ['c', '/', 'f', '/', 'i', 4]]


def test(vars, tests, number):
    test = tests[number]
    test_string = '(' + str(vars[test[0]]) + test[1] + str(vars[test[2]]) + ')' + test[3] + str(vars[test[4]])
    if eval(test_string) == test[5]:
        return True
    else:
        return False


vars = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}

for a in range(1,10):
    vars['a'] = a
    for b in range(1,10):
        if b not in vars.values():
            vars['b'] = b
            for c in range(1,10):
                if c not in vars.values():
                    vars['c'] = c
                    if test(vars, tests, 0):
                        for d in range(1,10):
                            if d not in vars.values():
                                vars['d'] = d
                                for g in range(1,10):
                                    if g not in vars.values():
                                        vars['g'] = g
                                        if test(vars, tests, 1):
                                            for e in range(1,10):
                                                if e not in vars.values():
                                                    vars['e'] = e
                                                    for f in range(1,10):
                                                        if f not in vars.values():
                                                            vars['f'] = f
                                                            if test(vars, tests, 2):
                                                                for h in range(1,10):
                                                                    if h not in vars.values():
                                                                        vars['h'] = h
                                                                        if test(vars, tests, 3):
                                                                            for i in range(1,10):
                                                                                if i not in vars.values():
                                                                                    vars['i'] = i
                                                                                    if test(vars, tests, 4) and test(vars, tests, 5):
                                                                                        print(vars)
                                                                            vars['i'] = 0
                                                                vars['h'] = 0
                                                    vars['f'] = 0
                                            vars['e'] = 0
                                vars['g'] = 0
                        vars['d'] = 0
            vars['c'] = 0
    vars['b'] = 0
