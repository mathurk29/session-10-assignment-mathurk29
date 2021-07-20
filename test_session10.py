import pytest
from polygons import Polygon
from sequences import PolygonSequence

p = Polygon(10, 10)


def test_docstring_Polygon():

    assert len(Polygon.__doc__) != 0, 'Please provide docstring'
    assert len(PolygonSequence.__doc__) != 0, 'Please provide docstring'


def test_attributes_Polygon():
    ''' Test function to check attributes of a Polygon with no. of vertices = 10 and circumradius = 10 units'''

    with pytest.raises(ValueError):
        Polygon(10.2, 10)
    assert p.vertices == 10, 'No of edges are set incorrectly'
    assert p.circumradius == 10, 'Circumradius is set incorrectly'


def test_equality_Polygon():
    
    p1 = Polygon(3, 4)
    p2 = Polygon(3, 4)
    assert p1 == p2, 'Equals to operator is not working properly.'


def test_comparison_Polygon():

    p3 = Polygon(4, 5)
    p4 = Polygon(5, 6)

    assert p3 < p4, 'Comaprison operators are not working properly.'
    assert p4 > p3, 'Comaprison operators are not working properly.'


def test_calculation_Polygon():
    ''' Cross-check calculations with pre-calculated values of a Polygon with vertices = 10 and edge_length=10'''

    assert round(p.edge_length, 2) == 6.18, 'Edge length is incorrect'
    assert round(p._interior_angle, 2) == 458.37, 'Interior angle is incorrect'
    assert round(p.apothem, 2) == 9.51, ' Apothem is incorrect'
    assert round(p.area, 2) == 293.89, 'Area is incorrect'
    assert round(p.perimeter, 2) == 61.80, 'Perimeter is incorrect'


def test_validation_PolgonSequence():

    with pytest.raises(ValueError):
        PolygonSequence(2, 100)


def test_PolygonSequence__getItem__():

    poly_seq = PolygonSequence(10, 20)
    assert poly_seq.__getitem__(
        3).vertices == 3, '0th element is supposed to be a Polygon of 3 sides'
    assert poly_seq.__getitem__(
        6).vertices == 6, 'The nth element is supposed to give a Polygon of n+3 sides'
    assert poly_seq.__getitem__(
        10).vertices == 10, 'The nth element is supposed to give a Polygon of n+3 sides'
    assert poly_seq.__getitem__(
        -1).vertices == 10, 'The nth element is supposed to give a Polygon of n+3 sides'
    assert poly_seq.__getitem__(
        -2).vertices == 9, 'The -nth element is supposd to give Polygon of -n+max_edge-3+1 sides'

    poly_seq = PolygonSequence(50, 20)
    assert poly_seq.__getitem__(
        3).vertices == 3, '0th element is supposed to be a Polygon of 3 sides'
    assert poly_seq.__getitem__(
        10).vertices == 10, 'The nth element is supposed to give a Polygon of n+3 sides'
    assert poly_seq.__getitem__(
        50).vertices == 50, 'The nth element is supposed to give a Polygon of n+3 sides'
    assert poly_seq.__getitem__(
        -1).vertices == 50, 'The -ve nth element is supposed to give a Polygon of (n+3) sides'


def test_PolygonSequence_max():
    pass
