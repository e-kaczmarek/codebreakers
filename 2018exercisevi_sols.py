#
# exercisevi_sols.py
#
#

# Problem 1

def string_to_ASCII(string):
    # takes a string as an input
    # returns a list of integers representing each character's decimal ASCII code
    ret = list(string)
    for index in range(len(ret)):
        ret[index] = ord(ret[index])
    return ret

# Problem 2

def ASCII_to_string(list_of_ASCII):
    # takes as input a list of integers representing decimal ASCII codes
    # returns the string the input represents
    # essentially reverses string_to_ASCII()
    ret = ''
    for num in list_of_ASCII:
        ret += chr(num)
    return ret

# Problem 3

def binary_to_decimal(bin_str):
    # takes as input a string representing a binary number
    # returns its decimal equivalent
    exp = 0
    ret = 0
    for digit in bin_str[::-1]:
        if digit == '1':
            ret += (2 ** exp)
        exp += 1
    return ret

# Problem 4

def decimal_to_binary(decimal_num):
    # takes as input a decimal number (of type int)
    # returns its binary equivalent (of type str)
    ret = ''
    while (decimal_num != 0):
        ret += str(decimal_num % 2)
        decimal_num //= 2
    return ret[::-1]
