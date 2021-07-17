from math import sin, cos, pi
from typing import Type


class Polygon():
    ''' A class of regular strictly convex polygon. It calcuates interior angles, edge length, apothem, area and perimeter.
        \n Properties:
            vertices / edges
            circumradius
            interior_angle
            edge_length
            apothem
            area
            perimeter
    '''

    def __init__(self, vertices, circumradius):
        if type(vertices) != int:
            raise ValueError
        self.__vertices = vertices  # Private Attributes

        self.__circumradius = circumradius  # Private Attributse
        self.interior_angle = None
        self.edge_length = None
        self.apothem = None
        self.area = None
        self.perimeter = None
        self._run()

    @property
    def vertices(self):
        return self.__vertices

    @property
    def circumradius(self):
        return self.__circumradius

    def _run(self):
        ''' Populate all attributes of the object.'''
        self._calculateInteriorAngle()
        self._calculateEdgeLength()
        self._calculateApothem()
        self._calculateArea()
        self._calculatePerimeter()

    def _calculateInteriorAngle(self):
        self.interior_angle = 0
        self.interior_angle = (self.__vertices - 2) * 180 / pi

    def _calculateEdgeLength(self):
        self.edge_length = (2 * self.__vertices) * sin(pi/self.__vertices)

    def _calculateApothem(self):
        ''' l '''
        self.apothem = (self.__vertices) * cos(pi/self.__vertices)

    def _calculateArea(self):
        if self.edge_length is None:
            self._calculateEdgeLength()
        self.area = (self.__vertices/2) * self.edge_length * self.apothem

    def _calculatePerimeter(self):
        if self.edge_length is None:
            self._calculateEdgeLength()
        self.perimeter = self.__vertices * self.edge_length

    def __repr__(self):
        return f'This is an object of regular strictly convex polygon with {self.vertices} and circumradius of {self.circumradius}'

    def __eq__(self, other):
        if self.__vertices == other.vertices and self.__circumradius == other.circumradius:
            return True
        return False

    def __gt__(self, other):
        if self.__vertices > other.vertices:
            return True
        return False
