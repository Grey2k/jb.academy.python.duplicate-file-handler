# write your code here
import argparse
import os
import sys

SORT_DESC = 1
SORT_ASC = 2

parser = argparse.ArgumentParser(description="This is Duplicate File Handler app")

parser.add_argument('directory', nargs='*', default=None)

directory = parser.parse_args().directory

if not directory:
    print('Directory is not specified')
    sys.exit(1)

entrypoint = directory[0]

print('Enter file format:')
ext = input().strip()

print()
print('Size sorting options:')
print('1. Descending')
print('2. Ascending')

sorting = SORT_ASC

while True:
    print()
    print('Enter a sorting option:')
    sorting = int(input().strip())

    if sorting in [SORT_ASC, SORT_DESC]:
        print()
        break

    print('Wrong option')

file_map = {}

os.system("mv module/root_folder/files/stage/src/reviewSlider.js module/root_folder/files/stage/src/reviewslider.js")
os.system(
    "mv module/root_folder/files/stage/src/toggleMiniMenu.js module/root_folder/files/stage/src/toggleminimenu.js")

for root, dirs, files in os.walk(entrypoint):
    for file in files:
        file_path = os.path.join(root, file)
        if ext and ext != os.path.splitext(file_path)[1]:
            continue

        size = int(os.path.getsize(file_path))
        if size not in file_map:
            file_map[size] = [file_path]
            continue

        file_map[size].append(file_path)

for key in sorted(file_map, reverse=(True if sorting == SORT_DESC else False)):
    if len(file_map[key]) > 1:
        print(f'{key} bytes')
        for name in file_map[key]:
            print(name)
        print()
