def make_bricks(small, big, goal):
    if goal / 5 <= big and goal % 5 > small:
        return False
    elif goal - big * 5 <= small:
        return True
    else:
        return False


################################
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if (a == b):
        return c
    if (c == b):
        return a
    if (a == c):
        return b
    else:
        return a + b + c


####################################
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    else:
        return a + b + c


################################################
def no_teen_sum(a, b, c):
    if fix_teen(a) and fix_teen(b) and fix_teen(c):
        return a + b + c
    elif fix_teen(a) and fix_teen(b):
        return a + b
    elif fix_teen(a) and fix_teen(c):
        return a + c
    elif fix_teen(c) and fix_teen(b):
        return c + b
    elif fix_teen(a):
        return a
    elif fix_teen(b):
        return b
    elif fix_teen(c):
        return c
    else:
        return 0


def fix_teen(n):
    if n != 13 and n != 14 and n != 17 and n != 18 and n != 19:
        return True
    else:
        return False


###################################################3
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if num == 0:
        return 0
    if num % 10 >= 5:
        return num + 10 - num % 10
    if num % 10 < 5:
        return num - num % 10


###################################################
def close_far(a, b, c):
    if (((abs(a - b) == 1 or abs(a - b) == 0) and abs(a - c) != 1) or (
            (abs(a - c) == 1 or abs(a - c) == 0) and abs(a - b) != 1)) and abs(b - c) != 1:
        return True
    else:
        return False


#####################################################
def make_chocolate(small, big, goal):
    if goal / 5 <= big and goal % 5 > small:
        return -1
    elif goal - big * 5 >= 0 and goal - big * 5 <= small:
        return goal - big * 5
    elif goal - big * 5 < 0 and goal % 5 <= small:
        return goal % 5
    else:
        return -1
