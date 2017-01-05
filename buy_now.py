def count_collisions(text, keypad):
    numbers = [translate_word(word, keypad) for word in text.lower().split()]
    for word in numbers:
        if numbers.count(word) > 1:
            return numbers.count(word)
    return 0


def translate_word(w, m):
    return ''.join([str(m[c]) for c in w])

def remove_all(e, l):
    while e in l:
        l.remove(e)

def make_mapping(l):
    mapping = {}
    for i in range(len(l)):
        for letter in l[i]:
            mapping[letter] = i
    return mapping
