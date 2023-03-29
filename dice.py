import random
import typing


class Dice:
    @classmethod
    def numbers(cls) -> typing.Iterator[int]:
        """
        주사위에서 나올 수 있는 숫자 생성기
        """
        for i in range(1, 7):
            yield i

    def roll(self) -> int:
        """
        [1,6]범위의 정수를 무작위로 생성하여 반환한다.
        """
        return random.randint(1, 6)


class DiceProbability:
    n: int # 주사위를 던질 횟수
    a: typing.List[int] # N번의 주사위 숫자를 저장할 수 있는 배열
    b: typing.List[int] # 6개 주사위 숫자가 나오는 확률을 저장할 수 있는 배열

    def __init__(self, n: int) -> None:
        """
        멤버 변수 초기화

        :param n: 주사위를 던질 횟수
        """
        self.n = n
        self.a = [None] + [0] * 6 # a[i]: 눈금 i가 나온 횟수
        self.b = [None] + [0] * 6 # b[i]: 눈금 i가 나오는 통계적 확률

    def calcProbability(self) -> None:
        """
        각 번호별 확률을 계산해 배열 b에 저장
        """
        dice = Dice()

        # 초기화
        for num in Dice.numbers():
            self.a[num] = 0
            self.b[num] = 0

        # 주사위를 N번 굴려 각 눈금이 나온 횟수를 저장
        for _ in range(self.n):
            num = dice.roll()
            self.a[num] += 1

        # 각 눈금이 나온 확률을 계산하여 저장
        for num in Dice.numbers():
            self.b[num] = self.a[num] / self.n


    def printProbability(self) -> None:
        """
        1~6 주사위 값이 나타날 수 있는 확률을 화면에 출력
        """
        print(f'총 횟수: {self.n}')
        for num in Dice.numbers():
            print(f'주사위 {num}: {self.a[num]} 비율: {self.b[num]:>.3f}')