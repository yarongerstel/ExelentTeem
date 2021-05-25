

def group_by(func, iter):
    dic = {}
    for i in iter:
        if func(i) in dic.keys():
            dic[func(i)] = dic[func(i)] + [i]
        else:
            dic[func(i)] = [i]
    print(dic)


group_by(len, ["hi", "bye", "yo", "try"])


###################################################

def zip_with(fun, *itr):
    l = []
    #Creates a list of indexed lists
    for i in range(len(itr[0])):
        b = []
        for j in itr:
            b.append(j[i])
        l.append(b)
    n = list(map(fun, l))
    print(n)
###################################################
from PIL import Image,ImageDraw
def zhofen(text):
    width, height = len(text), 255
    canvas = Image.new('RGB', (width, height), 'yellow')
    img_draw = ImageDraw.Draw(canvas)
    for ch in range(len(text)):
        img_draw.point((ch,ord(text[ch])), fill='black')
        ord(text[ch])

    #canvas.show()

#################################################
def zhofen1():
    canvas = Image.new('RGB', (255, 255), 'yellow')
    img_draw = ImageDraw.Draw(canvas)
    for i in range(255):
        for j in range(255):
            for k in range(255):
                img_draw.point(((j,k)), fill=(i,j,k))

    canvas.show()
zhofen1()
