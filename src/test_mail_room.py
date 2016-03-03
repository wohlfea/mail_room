import pytest

POSSIBLE_INPUT = [
    (('c', ['c', 's']), True),
    (('Q', ['q', 'r']), True),
    (('F', ['f', 'e', 's', 'd']), True),
    (('2', ['a', 'b', 'c']), False)
]

TEST_STR = '''
----------
George T.:
    Total Donated: $147.50
    Number of Donations: 4
    Average Donation: $36.87
----------
Rebecca L.:
    Total Donated: $4253.95
    Number of Donations: 3
    Average Donation: $1417.98
----------
Manny B.:
    Total Donated: $17.35
    Number of Donations: 4
    Average Donation: $4.33
'''
EXAMPLE_DICTS = [
    {'George T.': [12.50, 10.00, 25.00, 100.00],
     'Rebecca L.': [250.00, 1003.00, 3000.95],
     'Manny B.': [1.05, 2.50, 4.00, 9.80]},
    TEST_STR
]


@pytest.mark.parametrize('args, result', POSSIBLE_INPUT)
def test_input_check(args, result):
    from mail_room import input_check
    assert input_check(*args) == result


@pytest.mark.parametrize('dict, result', EXAMPLE_DICTS)
def test_create(dict, result):
    from mail_room import create
    assert create(dict) == result
