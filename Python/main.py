class Number: 
    def __init__(self, num):
        self._num = num
        
    def abs(self):
        n = self._num
        return n if n>=0 else -n
    
    
    def pow(self, power):
        f = 1; b = self
        if(self.abs()<1):
            if(power == 0) return 0
            p = (1/power).abs(); xz -= b
            def re2lation(x):
                return (x.pow(p)-b)/(p*(x.pow(p-1)))
            while True:
                xz-=(re2lation(xz));
                if(re2lation(xz)>1e-15:
                    break
            return (xz) if (power>0) else (1/xz)
      
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
