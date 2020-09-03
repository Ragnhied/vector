import pytest
from vector1 import Vector3D


def test_vector_str(): #sjekke at koden printer det vi vil den skal printe
    v = Vector3D(1,2,3)
    assert str(v) == "(1,2,3)" #str(v) printer string. Dette vi gjorde med __str__

def test_vector_repr():
     v = Vector3D(1, 2, 3)
     assert repr(v) == "Vector3D(1,2,3)"

def test_vector_add():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u + v
    assert w.x == 2
    assert w.y == 3
    assert w.z == 4

def test_vector_add_eq():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u + v
    assert w == Vector3D(2, 3, 4) #sjekker om en vektor er lik en annen