import os
import shutil
import encode


FOLDER_NAME = "important-files"


def main():
    zipname = f"{FOLDER_NAME}.zip"
    shutil.make_archive(FOLDER_NAME, 'zip', FOLDER_NAME)
    encode.encode(zipname)    
    os.remove(zipname)


if __name__ == "__main__":
    main()
