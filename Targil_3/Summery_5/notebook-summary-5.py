def most10(my_file):
    my_dict = {}
    my_list = []
    most = []
    # Makes all the marks spaced to split effectively
    my_file = my_file.replace("\n", " ")
    my_file = my_file.replace(",", " ")
    my_file = my_file.replace("?", " ")
    my_file = my_file.replace("!", " ")
    my_file = my_file.replace(".", " ")
    my_file = my_file.replace('"', " ")
    # Converts all letters to uppercase so that two words with uppercase and lowercase letters count together
    my_file = my_file.upper()
    my_list = my_file.split(" ")
    for word in my_list:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    for i in range(11):
        most.append((get_key(max(my_dict.values()), my_dict), max(my_dict.values())))
        del my_dict[most[i][0]]
    print(most[1:])  # agnore from the first, it is ""..


"""
    Gets a key and dictionary entry and returns the key
"""


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


file = open("war-and-peace.txt", 'r').read()
most10(file)


#####################################################
def interleave(*item):
    index = -1
    l = []
    while True:
        index += 1
        for i in item:
            if len(i) > index:
                l.append(i[index])
                flag = 1
        if flag == 0:
            break
        flag = 0
    print(l)


# in generator
def interleaveGen(*item):
    index = -1
    l = []
    while True:
        index += 1
        for i in item:
            if len(i) > index:
                yield i[index]
                flag = 1
        if flag == 0:
            break
        flag = 0


#########################################################################

def add_inventory(dec, **item):
    for k, v in item.items():
        if k in dec.keys():
            dec[k] = dec[k] + v
        else:
            dec[k] = v
    return dec


#########################################################################
import shutil


def order_hary():
    invalid = '<>:"/\|?* '
    for i in range(1, 123):
        file = open('hary\\' + str(i) + '.html', "r", encoding="utf-8")
        chapter = file.read()
        file.close()
        chapter = chapter[chapter.find("Chapter") + 8:chapter.find("</title>")]
        chapter = chapter.split(" ")
        chapter[0] = chapter[0][:-1].zfill(3)
        name = " ".join(chapter)
        for char in invalid:
            name = name.replace(char, '')
        shutil.move('hary\\' + str(i) + '.html', 'hary\\' + name + '.html')


################################################################################
import random
import datetime


def birthdayparadox():
    sum = 0
    for i in range(10000):
        l = []
        for j in range(23):
            date = str(datetime.date.fromordinal(
                random.randint(datetime.date(2000, 1, 1).toordinal(), datetime.date(2020, 1, 1).toordinal())))
            date = date[5:]
            if date in l:
                sum += 1
                yield sum
            else:
                l.append(date)
    result = str(100 * sum / 10000)
    print("the result iz:" + result)


for i in birthdayparadox():
    print(i)
