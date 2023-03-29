from dice import DiceProbability


def main():
    n = int(input("주사위를 굴릴 횟수(n)을 입력: "))
    diceProbability = DiceProbability(n)
    diceProbability.calcProbability()
    diceProbability.printProbability()


if __name__ == '__main__':
    main()