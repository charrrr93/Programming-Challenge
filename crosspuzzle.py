
def test1(vars):
    a = vars[0]
    b = vars[1]
    c = vars[2]
    if (a + b) + c == 15:
        return True
    else:
        return False

def test2(vars):
    a = vars[0]
    d = vars[3]
    g = vars[6]
    if (a + d) - g == 3:
        return True
    else:
        return False

def test3(vars):
    d = vars[3]
    e = vars[4]
    f = vars[5]
    if (d + e) * f == 24:
        return True
    else:
        return False

def test4(vars):
    b = vars[1]
    e = vars[4]
    h = vars[7]
    if (b * e) - h == 12:
        return True
    else:
        return False

def test5(vars):
    i = vars[8]
    g = vars[6]
    h = vars[7]
    if g + h - i == 14:
        return True
    else:
        return False

def test6(vars):
    c = vars[2]
    f = vars[5]
    i = vars[8]
    if c / f / i == 4:
        return True
    else:
        return False

vars = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for a in range(1,10):
    vars[0] = a
    for b in range(1,10):
        if b not in vars:
            vars[1] = b
            for c in range(1,10):
                if c not in vars:
                    vars[2] = c
                    if test1(vars):
                        for d in range(1,10):
                            if d not in vars:
                                vars[3] = d
                                for g in range(1,10):
                                    if g not in vars:
                                        vars[6] = g
                                        if test2(vars):
                                            for e in range(1,10):
                                                if e not in vars:
                                                    vars[4] = e
                                                    for f in range(1,10):
                                                        if f not in vars:
                                                            vars[5] = f
                                                            if test3(vars):
                                                                for h in range(1,10):
                                                                    if h not in vars:
                                                                        vars[7] = h
                                                                        if test4(vars):
                                                                            for i in range(1,10):
                                                                                if i not in vars:
                                                                                    vars[8] = i
                                                                                    if test5(vars) and test6(vars):
                                                                                        print(vars)
                                                                            vars[8] = 0
                                                                vars[7] = 0
                                                    vars[5] = 0
                                            vars[4] = 0
                                vars[6] = 0
                        vars[3] = 0
            vars[2] = 0
    vars[1] = 0
