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
        if number_of_edges < 3:
            return TypeError("Polygon cant have less than 3 sides"), ValueError('Polygon cant have less than 3 sides')
        polygon = Polygon(number_of_edges, circumradius)
        return (polygon, polygon.area/polygon.perimeter)

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.maxnumber_of_edges + s + 1
            if s < 0 or s >self.maxnumber_of_edges:
                raise IndexError
            else:
                return PolygonSequence._polygonCache(s,self.circumradius)[0]
        else:
            start, stop, step = s.indices(self.maxnumber_of_edges)
            rng = range(start, stop, step)
            return [PolygonSequence._polygonCache(i,self.circumradius) for i in rng]

    def max_efficient(self):
        max_ratio = edge = 0
        for i in range(3,self.maxnumber_of_edges):
            if max_ratio < PolygonSequence._polygonCache(i,self.circumradius)[1]:
                max_ratio = PolygonSequence._polygonCache(i,self.circumradius)[1]
                edge = i
        return PolygonSequence._polygonCache(edge,self.circumradius)[0]

    def __repr__(self) -> str:
        return f'A sequence of Polygons starting from 3-edge Polygon till  no {self.maxnumber_of_edges}-edge Polygon. All polygons in the sequence have same circumradius of {self.circumradius} units.'
