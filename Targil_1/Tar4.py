def ispol(num):
    st = str(num)
    l = len(st) / 2
    for i in range(int(l)):
        if st[i] is not st[len(st) - 1 - i]:
            return False
    return True


def polindrom():
    a, b = 999, 999
    while True:
        if ispol(a * b):
            return a * b
        if b > 900:
            b -= 1
        else:
            b = a - 1
            a -= 1


def main():
    print(polindrom())


if __name__ == '__main__':
    main()
