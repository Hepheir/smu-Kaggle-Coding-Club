import random
import typing


class Dice:
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
        pass

    def printProbability(self) -> None:
        """
        1~6 주사위 값이 나타날 수 있는 확률을 화면에 출력
        """
        pass