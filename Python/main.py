# root-algorithmic-analysis in py
# Author: seojun0602

# Number 클래스
class Number:
    def __init__(self, num):
        self._num = num
        
    # 절댓값    
    def abs(self):
        n = self._num
        return Number(n if n >= 0 else -n)
        
    # 매직 메서드 추가.
    #  더하기
    def __add__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num + other)
        
    #  빼기
    def __sub__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num - other)
        
    #  곱하기
    def __mul__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num * other)
        
    #  나누기
    def __truediv__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num / other)
        
    #  less then
    def __lt__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num < other
        
    #  greater then
    def __gt__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num > other
        
    #  equal
    def __eq__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num == other
        
    #  toString
    def __str__(self):
        return str(self._num)
        
    def toFrac(self):
        return "WIP"
    
    # Fast-Exponentiation-Algotitm (power < 1)
    # Newton-Raphson method (power >= 1)
    # Reference: https://me2.kr/JLOQT
    def pow(self, power):
        f = Number(1)
        b = self

        if self.abs()._num < 1:
            if power == 0:
                return Number(1)
            p = Number(1 / power).abs()
            xz = b

            def rel(x):
                return (x.pow(p) - b) / (p * (x.pow(p - 1)))

            while True:
                d = rel(xz)
                xz = xz - d
                if d.abs()._num < 1e-15:
                    break

            return xz if power > 0 else Number(1) / xz

        orig = power
        pv = Number(power).abs()._num

        while int(pv) > 0:
            if int(pv) % 2 == 1:
                f = f * b
            b = b * b
            pv = pv // 2

        return f if orig > 0 else Number(1) / f
    
    # Factorial
    # Reference: cafe.naver.com/nameyee/38284
    def fac(self):
        num, result = self._num, 1
        if (num == 0 or num == 1): return 1
        for i in range(num): result *= (i + 1)
        return float('nan') if result == 1 else result


# Array 클래스
class Array:
    def __init__(self, list_):
        self._list = list_
    
    # 정적 메서드
    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
        
    # 최대공약수 구하기
    def gcd(self):
        if not self._list:
            return 0

        r = self._list[0]
        if isinstance(r, Number):
            r = r._num

        for n in self._list[1:]:
            if isinstance(n, Number):
                n = n._num
            r = self._gcd(r, n)

        return Number(r if r >= 0 else -r)

# PI
# Reference: cafe.naver.com/nameyee/38284
# lamda is insane
π = (lambda: (
    lambda stand: Number(1) / (stand * (
        lambda: (
            lambda recur: (
                lambda acc, k: (
                    (lambda loop:
                        loop(loop, acc, k)
                    )(lambda loop, acc, k:
                        acc if recur(k).abs()._num < 1e-15 else loop(loop, acc + recur(k), k + 1)
                    )
                )
            )(Number(0), 0)
        )
    )(lambda k:
        Number(4 * k).fac() * (Number(1103) + Number(26390) * k) /
        (Number(k).fac().pow(4) * Number(396).pow(4 * k))
    ))
)(Number(2) * Number(2).pow(0.5) / Number(9801)))()

# 테일러 급수를 통한 삼각함수 계산.
#  사인 함수
def sints(r):
    return "WIP"

#  코사인 함수
def costs(r):
    return "WIP"

#  아크탄젠트 함수
def atan(x):
    return "WIP"

# 복소수의 극형식을 이용한 거듭제곱근 계산
def rootCplx(cplxNum, index, mxdecp=3, frac=False):
    return "WIP"
        