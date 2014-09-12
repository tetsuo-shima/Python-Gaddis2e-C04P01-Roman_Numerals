__author__ = 'dwight'

# Write a program that prompts the user to enter a number within the range of 1 through 10. The program should display
# the Roman numeral version of that number. If the number is outside the range of 1 through 10, the program should
# display an error message.



def main():
    number = int(input("Enter an integer between 1 and 10 (inclusive): "))
    if not between_one_and_ten(number):
        print('Error: number out of range')
    else:
        print('Equivalent Roman Numeral:', convert_arabic_num_to_roman(number))


def convert_arabic_num_to_roman(number):
    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return  'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    elif number == 6:
        return 'VI'
    elif number == 7:
        return 'VII'
    elif number == 8:
        return 'VIII'
    elif number == 9:
        return 'IX'
    else:
        return 'X'


def between_one_and_ten(number):
    if number >= 1 and number <= 10:
        return True
    return False


main()

