# from mygeopy.triangle import hypot

# def test_hypot():
#     assert hypot(3,4) == 5


from mygeopy.triangle import hypot

def test_hypot():
    assert hypot(3,4) == 5


if __name__ == "__main__":
    import doctest
    doctest.testmod()