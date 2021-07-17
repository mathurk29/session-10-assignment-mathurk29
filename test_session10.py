import pytest
from module1 import Polygon
from module2 import PolygonSequence

p = Polygon(10, 10)

def test_attributes_Polygon():
    ''' Test function to check attributes of a Polygon with no. of vertices = 10 and circumradius = 10 units'''
    with pytest.raises(ValueError):
        Polygon(10.2,10)
    assert p.vertices == 10, 'No of edges are set incorrectly'
    assert p.circumradius == 10, 'Circumradius is set incorrectly'


def test_calculation_Polygon():
    assert round(p.edge_length,2) == 6.18, 'Edge length is incorrect'
    assert round(p.interior_angle,2) == 458.37, 'Interior angle is incorrect'
    assert round(p.apothem,2) == 9.51, ' Apothem is incorrect'
    assert round(p.area,2) == 293.89, 'Area is incorrect'
    assert round(p.perimeter,2) == 61.80, 'Perimeter is incorrect'

def test_docstring():
    assert len(Polygon.__doc__) != 0, 'Please provide docstring'
    assert len(PolygonSequence.__doc__) != 0, 'Please provide docstring'

def test_PolygonSequence():
    with pytest.raises(IndexError):
        PolygonSequence(2,10)
    
    poly_seq = PolygonSequence(10,20)
    # 3-6, 4-7, 5-8, 6-9, 7-10
    assert poly_seq.__getitem__(0).vertices == 3, 'Wrong verices'
    assert poly_seq.__getitem__(3).vertices == 6, 'Wrong verices'
    assert poly_seq.__getitem__(7).vertices == 10, 'Wrong -1'