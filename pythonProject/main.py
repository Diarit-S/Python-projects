


def casttonumber(mystring):
    char_index = len(mystring) - 1
    power_weight = 0
    dec_value = 0
    while char_index >= 0:
        column_value = ord(mystring[char_index]) - ord("0")
        dec_value += column_value * 10 ** power_weight
        power_weight += 1
        char_index -= 1

    return dec_value


def not_trival(num_string):
    dec_value = 0
    for current_char in num_string:
        dec_value *= 10
        dec_value += ord(current_char) - ord("0")

    return dec_value

def binary_to_decimal(bites):
    char_index = len(bites) - 1
    power_weight = 0
    dec_value = 0
    while char_index >= 0:
        dec_value += bites[char_index] * 2 ** power_weight
        power_weight += 1
        char_index -= 1

    return dec_value

def binary_to_decimal_not_trival(bites):
    dec_value = 0
    for current_char in bites:
        dec_value *= 2
        dec_value += current_char

    return dec_value


print(binary_to_decimal_not_trival([1, 1, 1, 1, 1, 1, 1, 1]))
