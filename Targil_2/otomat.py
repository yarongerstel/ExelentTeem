def oto():
    f = open("otomatfile.txt", "r")
    f.readline()
    states = f.readline()
    states = states[states.find('q'):].split(", ")
    states[len(states) - 1] = states[len(states) - 1][:-1]  # [q0, q1..]
    # print(states)
    start = f.readline()  # [7:]
    start = start[start.find('q'):]
    # print(start)
    accepting = f.readline()
    accepting = accepting[accepting.find('q'):].split(", ")
    accepting[len(accepting) - 1] = accepting[len(accepting) - 1][:-1]
    # print(accepting)
    f.readline()
    f.readline()
    q0 = []
    q1 = []
    # צריך לחפש דרך שמסווגת לכל מצב לאן הוא הולך, ואני לא יודע מראש לכמה מקומות הוא הולך בכללי..
    for i in range(len(states) ** 2):
        line = f.readline()
        if line.startswith('q0'):
            line = line[4:]
            ed = line[-3:-1]
            line = line[:-7]
            nums = line.split(", ")
            q0.append((nums, ed))
        if line.startswith('q1'):
            line = line[4:-1]
            ed = line[-2:]
            line = line[:-6]
            nums = line.split(", ")
            q1.append((nums, ed))
    print(q0)
    print(q1)


oto()
