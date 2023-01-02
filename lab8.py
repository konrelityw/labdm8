# G = ["V", "T", "S", "P"]   граматика
# v = [0, 1, "S", "A", "B"]   скінченна множина нетермінальних символів
# T = [0, 1]   скінченна множина термінальних символів
# P = ["S->111S,S->Λ"]   множина продукції


def taskB():
    s = ["111S"]
    t = [" "]
    res = []

    def taskB1():
        elem = ""
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == "S":
                    print("Рекурсивно зліченна граматика (тип 0)")
                    while len(res) < 10:
                        elem = elem + s[i].replace('S', t[i])
                        res.append(elem)
                elif s[i][j] == "A":
                    elem = s[i].replace('A', t[i])
                    res.append(elem)
                elif s[i][j] == "B":
                    elem = s[i].replace('B', t[i])
                    res.append(elem)
        res.insert(0, 0)
        print(res)

    def taskB2():
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] != "A" and t[i][j] != "B" and t[i][j] != " ":
                    print("Контекстно-залежна граматика (тип 1)")
                elif t[i][j] == "A" or t[i][j] == "B" or t[i] == "0A" or t[i] == "0B" or t[i] == "1A" or t[i] == "1B" or \
                        t[i] == "A0" or t[i] == "B0" or t[i] == "A1" or t[i] == "B1":
                    print("Регулярна граматика (тип3)")
                else:
                    print("Контекстно-вільна граматика (тип 2)")

    def taskB3():
        stan = [["S0,S1", "S0,S1"], ["S0,S1", "S0,S1"]]
        print("          f")
        print("Стан    Вхід")
        print("         0      1")
        for i in range(0, len(stan)):
            print("S{}".format(i), end="     ")
            for j in stan[i]:
                print(j, end="  ")
            print()

    taskB1()
    taskB2()
    taskB3()


taskB()


def taskC():
    for n in range(3):
        res = "Λ"
        print("n =", n)
        for i in range(n):
            res = 3 * n * "A" + 2 * n * "B"
        print("S=" + res)
        if res.count("A") != 0 or res.count("B") != 0:
            print(("S=" + res).replace("A", "1").replace("B", "2"))


taskC()


def taskD(str):
    str = input("Введіть рядок ")
    print("Вхід: " + str + " Вихід: ", end="")
    check = str[4]
    if check == '0':
        print(1)
    elif check == '1':
        print(2)
    else:
        print(0)

    def task_d():
        stan = [["S2", "S1"], ["-", "-"], ["-", "-"]]
        print("          f")
        print("Стан    Вхід")
        print("       0    1")
        for i in range(0, len(stan)):
            print("S{}".format(i), end="     ")
            for j in stan[i]:
                print(j, end="  ")
            print()

    task_d()


taskD(str)


def taskE():
    print("Таблиця переходів")
    stan = [["S2", "S1"], ["S2", "S2"], ["S2", "S2"]]
    print("          f")
    print("Стан    Вхід")
    print("        0   1")
    for i in range(0, len(stan)):
        print("S{}".format(i), end="     ")
        for j in stan[i]:
            print(j, end="  ")
        print()
    print("Q (Стани автомата): " + "{S0, S1, S2}")
    print("Σ (алфавіт): " + "{0, 1}")
    print("q0 (Початковий стан): " + "{S0}")
    print("F (Кінцевий стан): " + "{S2}")
    print("Мова породжена автоматом: " + "L(G) = {0b^n, 1bb^n |n = 0, 1, 2,...; b — довільний ланцюжок}")


taskE()
