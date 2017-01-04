import string

class RomanNumeral:
    def __init__(self, i):
        if isinstance(i, int) or i[0] in string.digits:
            self.r = to_roman(int(i))
            self.i = int(i)
        else:
            self.r = i.upper()
            self.i = to_decimal(i.upper())

    def __add__(self, o):
        return RomanNumeral(self.i + o.i)

    def __mul__(self, o):
        return RomanNumeral(self.i * o.i)

    def __str__(self):
        return self.r + ' ({})'.format(self.i)

    def __repr__(self):
        return self.__str__()

numerals = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

r_numerals = {numerals[x]: x for x in numerals}

order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def to_roman(number):
    out = ''
    while number > 0:
        for i in order:
            if i <= number:
                out += numerals[i]
                number -= i
                break
    return out

def to_decimal(r):
    r = r.upper()
    i = 0
    total = 0
    while i < len(r):
        if i + 1 < len(r):
            if r_numerals[r[i]] < r_numerals[r[i+1]]:
                total += r_numerals[r[i]+r[i+1]]
                i += 1
            else:
                total += r_numerals[r[i]]
        else:
            total += r_numerals[r[i]]
        i += 1
    return total

def parse_calculation(e):
    expr = e.split()
    if expr[1] == '+':
        return RomanNumeral(expr[0]) + RomanNumeral(expr[2])
    elif expr[1] == '*':
        return RomanNumeral(expr[0]) * RomanNumeral(expr[2])


if __name__ == '__main__':
    print(parse_calculation(input('Enter the expression: ')).r)
