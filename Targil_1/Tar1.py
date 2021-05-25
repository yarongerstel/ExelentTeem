def mehalec35(num):
    run = 1
    s = 0
    while run < num:
        if run % 3 == 0 or run % 5 == 0:
            s = s+run
        run += 1
    return s


def main():
    print(mehalec35(1000))


if __name__ == '__main__':
    main()
