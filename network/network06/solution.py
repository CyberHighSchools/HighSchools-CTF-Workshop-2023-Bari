import os
import sys
from PIL import Image


def main():
    filename = input("filename\n> ")
    if not os.path.exists(filename):
        print("File not found")
        sys.exit(1)

    print("Reading data...")
    raw = Image.open(open(filename, "rb")).tobytes()
    bin_str = bytes([(x & 1)+48 for x in raw]).decode()  # '01110011 ...'

    # decoded = long_to_bytes(int(bin_str, 2)) # troppo lento
    decoded = bytes(int(bin_str[i:i+8], 2)
                    for i in range(0, len(bin_str), 8))  # veloce

    print("Writing to file")
    with open("output.zip", "wb") as f:
        f.write(decoded)
    print("Done")


if __name__ == "__main__":
    main()
