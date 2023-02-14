import sys
from pathlib import Path
import re

def checkIsDirectory(dirPath: Path):
    if not dirPath.is_dir():
        print(dirPath, "is not a directory")
        sys.exit(2)    

# read args
if len(sys.argv) != 3:
    print("Error: wrong number of arguments")
    print("Usage: python photo_move.py srcdirc destdir")
    sys.exit(1)

srcdirPath = Path(sys.argv[1])
destdirPath = Path(sys.argv[2])

print(f"Will scan {srcdirPath} for photos to store in {destdirPath}")
checkIsDirectory(srcdirPath)
checkIsDirectory(destdirPath)

for photoPath in srcdirPath.glob('*.jpg'):
    # print(photoPath)
    # print(photoPath.name)
    if not re.match(r"IMG_[0-9]{8}", photoPath.name):
        print("Warning: wrong photo name format (skip)", photoPath.name)
        continue
    dateTag = photoPath.name[4:12]
    photoFolderPath = destdirPath / dateTag
    photoFolderPath.mkdir(exist_ok=True)
    # print("Move",photoPath, "to", photoFolderPath / photoPath.name)
    # TODO: check if image is already there (skip or overwrite or rename)
    photoPath.rename(photoFolderPath / photoPath.name)


















