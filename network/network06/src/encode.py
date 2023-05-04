from PIL import Image
from math import sqrt


def pad(b, l):
    return b + b"\x00"*(len(b) % l)


def encode(filename):
    with open(filename, "rb") as fp:
        data = fp.read()

    bin_data = bytes([int(x)*255 for y in data for x in bin(y)[2:].zfill(8)]) # b'\x00\x00\xff\xff\x00 ...'
    
    size = round(sqrt(len(bin_data)) + 1)
    padded = pad(bin_data, size*size)
    
    image = Image.frombytes("L", (size, size), padded)
    image.save("bits.bmp")

