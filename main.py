
roman_digits = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_dict = {val: dig for val, dig in zip(roman_values, roman_digits)}


def integer_2_roman(digit):
    def convert_2_roman(digit):
        for r in roman_values:
            x, y = divmod(digit, r)
            yield roman_dict[r] * x
            digit -= (r * x)
            if digit <= 0:
                break

    return "".join([a for a in convert_2_roman(digit)])


if __name__ == '__main__':
    print(integer_2_roman(35))
