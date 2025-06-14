"""
root-algorithmic-analysis in py
Author: seojun0602
"""

#Number 클래스
class Number:
    def __init__(self, num):
        self._num = num
        
    # 절댓값    
    def abs(self):
        n = self._num
        return Number(n if n >= 0 else -n)
        
    # 매직 메서드 추가.
    # 더하기
    def __add__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num + other)
        
    # 빼기
    def __sub__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num - other)
        
    # 곱하기
    def __mul__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num * other)
        
    # 나누기
    def __truediv__(self, other):
        other = other._num if isinstance(other, Number) else other
        return Number(self._num / other)
        
    # less then
    def __lt__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num < other
        
    # greater then
    def __gt__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num > other
        
    # equal
    def __eq__(self, other):
        other = other._num if isinstance(other, Number) else other
        return self._num == other
        
    # toString
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
        