from main import soma, sub, mult


def test_soma():
    assert soma(3, 3) == 6


def test_sub():
    assert sub(10, 5) == 5


def test_mult():
    assert mult(5, 5) == 25.0
