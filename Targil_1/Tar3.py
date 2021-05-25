import math


def bigfactor(num):
    maxprime = 0

    while num % 2 == 0:
        maxprime = 2
        num /= 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            maxprime = i
            num = num / i

    if num > 2:
        maxprime = num

    return int(maxprime)

def main():
    print(bigfactor(600851475143))

if __name__ == '__main__':
    main()