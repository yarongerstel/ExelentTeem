def fibonachi(num):
    sun, a, b = 0, 0, 1
    while b < num:
        temp = a + b
        a = b
        b = temp
        sun += b
    return b


def main():
    print(fibonachi(4000000))


if __name__ == '__main__':
    main()
