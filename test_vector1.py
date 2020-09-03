import pytest
from vector1 import Vector3D


def test_vector_str():
    v = Vector3D(1,2,3)
    assert str(v) == "(1,2,3)" #str(v) printer string. Dette vi gjorde med __str__

# def test_vector_repr():
#     v = Vector3D(1,2,3)
#     assert repr(v) == "Vector3D(1,2,3)"