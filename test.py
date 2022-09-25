from add import Add


def test_add():
    assert 2 + 2 == Add(2, 2)
    assert 2 + 3 == Add(2, 3)