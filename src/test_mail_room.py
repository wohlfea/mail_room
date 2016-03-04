import pytest


SAMPLE_LIST = {
    u'Tommy C.': [4.25, 3.50, 72.20, 19.90, 10.00],
    u'Bobby B.': [9.00, 20.50, 25.00, 40.00],
}

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

TEST_LETTER = u'''
Dear George T.,
    Thank you very much for your donation of $2.50.
    This means you have donated a total amount of $2.50!
    Your money goes a long way to funding the Code Fellows Tuition.

    Sincerely,
    AJ & Kyle'''

EXAMPLE_DICTS = [({'George T.': [12.50, 10.00, 25.00, 100.00]}, TEST_STR)]
THANK_YOUS = [(('George T.', '2.50', SAMPLE_LIST), TEST_LETTER)]


@pytest.mark.parametrize('args, result', POSSIBLE_INPUT)
def test_input_check(args, result):
    from mail_room import input_check
    assert input_check(*args) == result


@pytest.mark.parametrize('args, result', THANK_YOUS)
def test_thank_you(args, result):
    from mail_room import thank_you
    try:
        old = len(SAMPLE_LIST[args[0]])
    except KeyError:
        old = 0
    assert thank_you(*args) == result
    assert len(SAMPLE_LIST[args[0]]) > old


@pytest.mark.parametrize('dict, result', EXAMPLE_DICTS)
def test_create(dict, result):
    from mail_room import create
    print(create(dict))
    assert create(dict) == result
