from solution import total_score

test_data = 'test_data.txt'


def test_total_score():
    assert total_score(test_data) == 15


def test_p2_total_score():
    assert total_score(test_data, part=2) == 12