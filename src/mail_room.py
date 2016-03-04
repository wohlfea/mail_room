import sys
from builtins import input


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
    Thank you very much for your donation of ${:,.2f}.
    This means you have donated a total amount of ${:,.2f}!
    Your money goes a long way to funding the Code Fellows Tuition.

    Sincerely,
    AJ & Kyle'''


def input_check(user_input, valid_opts):
    """Validate the user input."""
    if user_input.lower() in valid_opts:
        return True
    else:
        return False


def ordered_names(donor_list):
    """Order donors by total donation amount."""
    ordered = []
    for p in donor_list:
        ordered.append((sum(donor_list[p]), p))
    ordered.sort(reverse=True)
    return [p[1] for p in ordered]


def create(donor_list):
    """Generate a completed report of all donors ordered by donation amount."""
    results = ''''''
    for person in ordered_names(donor_list):
        total = sum(donor_list[person])
        how_many = len(donor_list[person])
        results += REPORT_STR.format(person, total, how_many, total / how_many)
    return results


def send():
    """Gather information about who we are thanking, print donor list
    if requested, or print the completed thank you letter to the screen."""
    while True:
        user_input = input(u'Who are we thanking?'
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
    """Return either an empty string or the completed Thank You letter."""
    if donation == '':
        return ''
    else:
        donor_list.setdefault(name, []).append(float(donation))
        return THANK_YOU_STR.format(name, float(donation),
                                    float(sum(donor_list[name])))


def valid_float():
    """Verify that user input is a valid donation amount."""
    while True:
        user_input = input(u'Enter the donation ammount.\n')
        try:
            rtn_float = '{:.2f}'.format(float(user_input))
            return rtn_float
        except ValueError:
            if user_input.lower() == 'q':
                sys.exit()
            elif user_input.lower() == 'r':
                return ''
            else:
                print('"{}" is an invalid donation amount.'.format(user_input))


def main(user_input):
    """Route user appropriately based on input."""
    if user_input.lower() == u'c':
        print(create(donor_list))
    elif user_input.lower() == u's':
        return send()
    elif user_input.lower() == u'q':
        return sys.exit()
    else:
        print('Returning to main menu')


def menu():
    """Take user input, validate it, and either prompt again or move on."""
    user_input = input(u'Would you like to [S]end a Thank-You or '
                       '[C]reate a report?\nPress [Q] At any time to quit.'
                       ' Press [R] at any time to return to this menu.\n')
    if input_check(user_input, [u's', u'c', u'q', u'r']):
        return main(user_input)
    else:
        print('Please enter valid input.')


if __name__ == '__main__':

    while True:
        menu()
