
def test1(vars):
    a = vars['a']
    b = vars['b']
    c = vars['c']
    if (a + b) + c == 15:
        return True
    else:
        return False

def test2(vars):
    a = vars['a']
    d = vars['d']
    g = vars['g']
    if (a + d) - g == 3:
        return True
    else:
        return False

def test3(vars):
    d = vars['d']
    e = vars['e']
    f = vars['f']
    if (d + e) * f == 24:
        return True
    else:
        return False

def test4(vars):
    b = vars['b']
    e = vars['e']
    h = vars['h']
    if (b * e) - h == 12:
        return True
    else:
        return False

def test5(vars):
    i = vars['i']
    g = vars['g']
    h = vars['h']
    if g + h - i == 14:
        return True
    else:
        return False

def test6(vars):
    c = vars['c']
    f = vars['f']
    i = vars['i']
    if c / f / i == 4:
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
                    if test1(vars):
                        for d in range(1,10):
                            if d not in vars.values():
                                vars['d'] = d
                                for g in range(1,10):
                                    if g not in vars.values():
                                        vars['g'] = g
                                        if test2(vars):
                                            for e in range(1,10):
                                                if e not in vars.values():
                                                    vars['e'] = e
                                                    for f in range(1,10):
                                                        if f not in vars.values():
                                                            vars['f'] = f
                                                            if test3(vars):
                                                                for h in range(1,10):
                                                                    if h not in vars.values():
                                                                        vars['h'] = h
                                                                        if test4(vars):
                                                                            for i in range(1,10):
                                                                                if i not in vars.values():
                                                                                    vars['i'] = i
                                                                                    if test5(vars) and test6(vars):
                                                                                        print(vars)
                                                                            vars['i'] = 0
                                                                vars['h'] = 0
                                                    vars['f'] = 0
                                            vars['e'] = 0
                                vars['g'] = 0
                        vars['d'] = 0
            vars['c'] = 0
    vars['b'] = 0
