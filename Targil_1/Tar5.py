import math


def smalldiv(num):
    ans = 1
    for i in range(1, num + 1):
        ans = int((ans * i) / math.gcd(ans, i))
    return ans


def main():
    print(smalldiv(5))


if __name__ == '__main__':
    main()
