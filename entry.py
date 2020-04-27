import sift




if __name__ == '__main__':
    s = sift.sift()
    finre, scal = s.match("./img/1.png", "./img/2.png")
    for i in finre:
        print(i[0])
        print(i[1])

    print(scal)

