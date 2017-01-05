a = ord('a')
A = ord('A')
def shift_letter(l, o):
    if l.isupper():
        return chr((ord(l) - A + o) % 26 + A)
    else:
        return chr((ord(l) - a + o) % 26 + a)


def get_letter_index(l):
    if l.isupper():
        return ord(l) - A
    else:
        return ord(l) - a
while True:
    plaintext = input('Enter encrypted message: ')
    out = []
    shift = 0
    for character in plaintext:
        if not character.isalpha():
            out.append(character)
        else:
            out.append(shift_letter(character, -shift))
            print(character, '-', shift, '=', shift_letter(character, -shift),)
            shift = get_letter_index(shift_letter(character, -shift))
    out = ''.join(out)
    print(out)
