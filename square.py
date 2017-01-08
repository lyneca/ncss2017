from microbit import *
display.clear()

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.b = 0

    def set(self, b):
        self.b = b
        display.set_pixel(self.x, self.y, self.b)

def scale(v, l, h, ol, oh):
    if v > h: v = h
    if v < l: v = l
    return (v - l) / (h - l) * (oh - ol) + ol

class Accel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def update(self):
        self.x = accelerometer.get_x()
        self.y = accelerometer.get_y()
        self.z = accelerometer.get_z()

def get_val(pixel, accel):
    x = accel.x  # 0 - 5

    return round(scale(pixel.x, 0, 4, -4, 4) * )

    return None  # 0 - 9

class Box:
    def __init__(self):
        pass

    def update(self):
        for x in pixels:
            for y in x:
                pixel = y
                pixel.set(get_val(pixel, accel))

    def draw(self):
        pass

box = Box()
accel = Accel()
pixels = []
for i in range(5):
    pixels.append([])
    for j in range(5):
        pixels[i].append(Pixel(i, j))

while True:
    accel.update()
    box.update()
