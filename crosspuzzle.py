import itertools

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


count = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vars = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0}


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
                                    print(vars)
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
