def double_char(str):
    double = ""
    for i in str:
        double = double + i * 2;
    return double


def count_hi(str):
    return str.count("hi")


def cat_dog(str):
    return str.count("cat") == str.count("dog")


def count_code(str):
    c = 0
    if len(str) > 4 and str[-2] == "o" and str[-3] == "c":
        c -= 1
    l = str.split("e")
    for i in l:
        if (len(i) > 2 and i[-3] == "c" and i[-2] == "o"):
            c += 1
    return c


def end_other(a, b):
    r = ""
    a = a.lower()
    b = b.lower()
    if (((a in b) or (b in a)) and (a[0] == b[0] or a[-1] == b[-1])):
        return True
    else:
        return False


def xyz_there(str):
    if (str.count(".xyz") == str.count("xyz")) or str.find("xyz") == -1:
        return False
    else:
        return True
