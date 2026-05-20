# hace algo útil
def sign(x):
    """Devuelve el signo de número."""
    if x == None:
        return None
    if x < 0:
        return -1

# prueba la función de signo


def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None
