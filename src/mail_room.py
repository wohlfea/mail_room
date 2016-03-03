import sys


donor_list = {
    'Carl D.': [1.25, 3.50, 7.20, 9.90, 10.00],
    'Manuel R.': [75.00, 99.50, 25.00, 80.00],
    'Eddie T.': [20.00, 40.50, 75.00, 99.00],
    'Ronaldo V.': [25.00, 25.00, 25.00, 25.00, 25.00, 25.00, 25.00, 25.00]
}

REPORT_STR = '''
----------
{}:
Total Donated: ${}
Number of Donations: {}
Average Donation: ${}
'''


def input_check(user_input, valid_opts):
    if user_input.lower() in valid_opts:
        return True
    else:
        return False


def create(donor_list):
    results = ''''''
    for person in donor_list:
        total = sum(donor_list[person])
        how_many = len(donor_list[person])
        results += REPORT_STR.format(person, total, how_many, total / how_many)
    return results

def main(user_input):
    if user_input.lower() == 'c':
        print(create(donor_list))
    elif user_input.lower() == 's':
        return send()
    elif user_input.lower() == 'q':
        return sys.exit()
    else:
        print('Returning to main menu')


def menu():
    user_input = raw_input('Would you like to [S]end a Thank-You or [C]reate a report?')
    if input_check(user_input, ['s', 'c', 'q', 'r']):
        return main(user_input)
    else:
        print('Please enter valid input.')

if __name__ == '__main__':

    while True:
        menu()
