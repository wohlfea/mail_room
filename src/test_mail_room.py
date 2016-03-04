import pytest

POSSIBLE_INPUT = [
    (('c', ['c', 's']), True),
    (('Q', ['q', 'r']), True),
    (('F', ['f', 'e', 's', 'd']), True),
    (('2', ['a', 'b', 'c']), False)
]

TEST_STR = u'''
----------
George T.:
    Total Donated: $147.50
    Number of Donations: 4
    Average Donation: $36.88'''

EXAMPLE_DICTS = [({'George T.': [12.50, 10.00, 25.00, 100.00]}, TEST_STR)]


@pytest.mark.parametrize('args, result', POSSIBLE_INPUT)
def test_input_check(args, result):
    from mail_room import input_check
    assert input_check(*args) == result

def test_valid_float():
    from mail_room import valid_float
    assert type(valid_float()) is str

@pytest.mark.parametrize('dict, result', EXAMPLE_DICTS)
def test_create(dict, result):
    from mail_room import create
    print(create(dict))
    assert create(dict) == result
