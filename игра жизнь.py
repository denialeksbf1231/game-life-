import random
import time
import sys
fq = 2
while fq != 0:
    print("вы хотите ввести поле или случайно сгенерировать его?(1 - хочу ввести,2 - хочу сгенерировать")
    r = ["1", "2"]
    v = list()
    h = [" ", "*"]
    t = input()
    while True:
        if t not in r:
            print("1 - хочу ввести,2 - хочу сгенерировать")
            t = input()
        else:
            break
    t = int(t)
    b = list()
    if t == 2:
        print("введите длину списка")
        a = input()
        while True:
            if a.isdigit():
                break
            else:
                print("введите длину списка")
                a = input()
        a = int(a)
        p = a
        while p != 0:
            g = random.randint(1, 2)
            if g == 1:
                b.append("*")
            if g == 2:
                b.append(" ")
            p = p - 1
    else:
        print("введите список,в качестве мертвой клетки используйте пробел, а в качестве живой используйте *")
        b = input()
        for i in b:
            v.append(i)
        b = v
        while True:
            for i in b:
                if i not in h:
                    print("в качестве мертвой клетки используйте пробел, а в качестве живой используйте *")
                    b = input()
                    v.clear
                    for i in b:
                        v.append(i)
                    b = v
                    break
            a = len(b)
            break
    print("введите количество генераций")
    s = input()
    while True:
        if s.isdigit():
            break
        else:
            print("введите количество генераций")
            s = input()
    s = int(s)
    for i in b:
        print(i, end="")
    print()
    b.append(b[0])
    d = b
    b = d[:-1]
    for i in range(s):
        time.sleep(0.5)
        for j in range(a):
            f = 0
            if b[j - 1] == "*":
                f = f + 1
            if d[j + 1] == "*":
                f = f + 1
            if d[j] == "*":
                if f != 1:
                    d[j] = " "
            else:
                if f == 1:
                    d[j] = "*"
        b = d[:-1]
        d[-1] = d[0]
        for j in b:
            print(j, end="")
        print()
    print("желаете продолжить?1 - да,2 - нет")
    fq = input()
    while True:
            if fq not in r:
                print("1 - да,2 - нет")
                fq = input()
            else:
                break
    if fq == "2":
        sys.exit()
