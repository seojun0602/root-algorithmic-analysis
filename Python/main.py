class Number: 
    def __init__(self, num):
        self._num = num
    def abs(self):
        n = self._num
        return n if n>=0 else -n
      
class Array:
    def __init__(self, list_):
        self._list = list_

    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcd(self):
        if not self._list:
            return 0 
        result = self._list[0]
        for num in self._list[1:]:
            result = self._gcd(result, num)
        return abs(result)
