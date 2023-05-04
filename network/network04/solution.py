from PIL import Image
import sys
import os

im = Image.open("banana.jpg")

# Part 1
os.system("exiftool split.png | grep ^Artist")
# Part 2
px = im.load()
data = []
for j in range(im.height):
    for i in range(im.width):
        for x in range(3):  # R, G, B
            data.append(px[i, j][x] % 2)


def get_byte(bitarray):
    sum = 0
    for x in range(8):
        sum += bitarray[x]*(2**(7-x))
    return sum


for _ in range(50):  # Print only the first 50 characters for speed
    c = get_byte(data[:8])
    print(chr(c), end="")
    data = data[8:]
