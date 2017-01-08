import random
box_dict = {}

def open_box(prisoner, box, iteration):
    if prisoner == box_dict[box]:
        return True
    else:
        if iteration < 50:
            iteration += 1
            return open_box(prisoner, box_dict[box], iteration)
        else:
            return False


def round():
    global box_dict
    prisoner_dict = list(range(100))
    random.shuffle(prisoner_dict)
    box_dict = {i: j for i, j in enumerate(random.sample(list(range(100)), 100))}
    free = 0
    for prisoner in prisoner_dict:
        if open_box(prisoner, prisoner, 0):
            free += 1
    if free == 100:
        return True
    else:
        return False

n = 10000

rounds = []
for i in range(n):
    rounds.append(round())
print(rounds.count(True) / n)
