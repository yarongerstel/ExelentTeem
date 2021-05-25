def get_election_results():
    f = open("elections.txt", "r")
    elector = {}
    for x in f:
        x = x[:-1]
        if x in elector:
            elector[x] = elector[x] + 1
        else:
            elector[x] = 1
    # print(elector.items())
    f.close()
    return elector


def up_hasima(m):
    pas = {}
    not_pas = {}
    for i in m.items():
        if i[1] < 35340:
            not_pas[i[0]] = i[1]
        else:
            pas[i[0]] = i[1]
    # print("not pass: ", not_pas.items())
    # print("pass: ", pas.items())
    return pas


def sum_up_hasima(m):
    sum = 0
    for i in m.items():
        if i[1] >= 35340:
            sum += i[1]
    return sum


def koalithya(dic, s):
    d = {}
    for i in dic:
        d[i] = round(dic[i] / s)
    return d


def make_option_of_koalizya(dic):
    for i in dic:
        if i == "NilsIsALeader":
            for i in dic:
                if i == "MidgeLandIsUs":
                    pass
                else:
                    print(i, " ", end="")
            print(120 - dic["NilsIsALeader"])
        if i == "MidgeLandIsUs":
            for i in dic:
                if i == "NilsIsALeader":
                    pass
                else:
                    print(i, " ", end="")
            print(120 - dic["MidgeLandIsUs"])


def main():
    print(koalithya(up_hasima(get_election_results()), 2078).items())
    make_option_of_koalizya(koalithya(up_hasima(get_election_results()), 2078))


if __name__ == '__main__':
    main()
