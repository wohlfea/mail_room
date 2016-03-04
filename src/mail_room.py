import sys
import string

donor_list = {
    u'Carl D.': [1.25, 3.50, 7.20, 9.90, 10.00],
    u'Manuel R.': [75.00, 9999.50, 25.00, 80.00],
    u'Eddie T.': [20.00, 40.50, 75.00, 99.00],
    u'Ronaldo V.': [25.00, 25.00, 25.00, 25.00, 25.00, 25.00, 25.00, 25.00]
}

REPORT_STR = u'''
----------
{}:
    Total Donated: ${:,.2f}
    Number of Donations: {}
    Average Donation: ${:,.2f}'''

THANK_YOU_STR = u'''
Dear {},
    Thank you very much for your donation of ${}

    Sincerely,
    AJ & Kyle'''

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


def send():
    while True:
        user_input = raw_input(u'Who are we thanking?'
                               '(type "[L]ist" for current donors)\n')
        if user_input.lower() == u'r':
            break
        elif user_input.lower() == u'q':
            sys.exit()
        elif user_input.lower() == u'l':
            for person in donor_list:
                print(person)
        else:
            print(thank_you(user_input, valid_float(), donor_list))
            break


def thank_you(name, donation, donor_list):
    if donation == '':
        return ''
    else:
        donor_list.setdefault(name, []).append(float(donation))
        return THANK_YOU_STR.format(name, donation)


def valid_float():
    while True:
        user_input = raw_input(u'Enter the donation ammount.\n')
        try:
            rtn_float = '{:.2f}'.format(float(user_input))
            return rtn_float
        except ValueError:
            if user_input.lower() == 'q':
                sys.exit()
            elif user_input.lower() == 'r':
                return ''

def main(user_input):
    if user_input.lower() == u'c':
        print(create(donor_list))
    elif user_input.lower() == u's':
        return send()
    elif user_input.lower() == u'q':
        return sys.exit()
    else:
        print('Returning to main menu')


def menu():
    user_input = raw_input(u'Would you like to [S]end a Thank-You or [C]reate a report?\n')
    if input_check(user_input, [u's', u'c', u'q', u'r']):
        return main(user_input)
    else:
        print('Please enter valid input.')

if __name__ == '__main__':

    while True:
        menu()
