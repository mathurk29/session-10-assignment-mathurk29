from polygons import Polygon
from functools import lru_cache


class PolygonSequence():
    ''' A class to create a sequence of type of Polygon.
        It implements lru_cache for faster processing.
        Properties:
            number_of_edges: No. of edges of largest Polygon in the sequence.
            circumradius: Length of common circumradius of all Polygons in the sequence
            '''

    def __init__(self, maxnumber_of_edges: int, circumradius: int) -> None:
        ''' Initializes PolygonSequence with number_of_edges of largest Polygon and common circumradius for all Polygon'''
        
        self.maxnumber_of_edges = self.set_number_of_edges(maxnumber_of_edges)
        self.circumradius = circumradius
        self.initialise_sequence()

    def set_number_of_edges(self,number_of_edges):

        # Validations
        if not isinstance(number_of_edges,int):
            raise TypeError('No. of sides of a Polygon should be integer')
        if number_of_edges < 0:
            raise ValueError('No. of sides cannot be negative.')
        if number_of_edges < 3:
            raise ValueError('Polygon must have at least three sides')

        return number_of_edges

    def __len__(self):
        return self.maxnumber_of_edges
    
    def initialise_sequence(self):
        for i in range(3,self.maxnumber_of_edges):
            PolygonSequence._polygonCache(i,self.circumradius)

    @staticmethod
    @lru_cache(2**10)
    def _polygonCache(number_of_edges: int, circumradius: int) -> Polygon:
        polygon = Polygon(number_of_edges, circumradius)
        return (polygon, polygon.area/polygon.perimeter)

    def __getitem__(self, n: int):
        ''' Returns the nth Polygon in the sequence, starting from 0'''

        if isinstance(n, int):
            if n >= 0:
                # For ease of calculations
                n = n + 3
                if n - 3 < 0:
                    n = n + self.maxnumber_of_edges
                if n < 3 or n >= self.maxnumber_of_edges + 3:
                    raise IndexError
                else:
                    return PolygonSequence._polygonCache(n, self.circumradius)[0]
            else:
                return self.__getitem__(self.maxnumber_of_edges + n + 1 - 3)
        else:
            raise TypeError

    def max_efficient(self):
        max_ratio = edge = 0
        for i in range(3,self.maxnumber_of_edges):
            if max_ratio < PolygonSequence._polygonCache(i,self.circumradius)[1]:
                max_ratio = PolygonSequence._polygonCache(i,self.circumradius)[1]
                edge = i
        return PolygonSequence._polygonCache(edge,self.circumradius)[0]

    def __repr__(self) -> str:
        return f'A sequence of Polygons starting from 3-edge Polygon till  no {self.maxnumber_of_edges}-edge Polygon. All polygons in the sequence have same circumradius of {self.circumradius} units.'
