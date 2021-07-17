from module1 import Polygon
from functools import lru_cache
from fractions import Fraction


class PolygonSequence():
    def __init__(self, n: int, circumradius: int) -> None:
        if n < 3:
            raise IndexError('Polygon must have at least three sides')
        self.n = n
        self.circumradius = circumradius
        self.cache = list()
        self._polygon(n)

    def __len__(self):
        return self.n

    # @staticmethod
    # @lru_cache(2**10)
    def _polygon(self, s):
        for i in range(3, s+1):
            self.cache.append((Polygon(i, self.circumradius)))

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = s + (self.n -3)
            if s < 0 or s >= (self.n - 3 + 1):
                raise IndexError("Ye kya hua")
            else:
                return self.cache[s]

    def max_efficient(self):
        max = 0
        result = 0
        for poly in self.cache:
            if Fraction(poly.area/poly.perimeter) > max:
                max = Fraction(poly.area/poly.perimeter)
                result = poly.vertices
        return result

    def __repr__(self) -> str:
        return f'Coming from PolygonSeq of max as {self.n}'
