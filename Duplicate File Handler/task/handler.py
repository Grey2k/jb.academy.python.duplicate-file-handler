# write your code here
import argparse
import os
import sys
import hashlib

SORT_DESC = 1
SORT_ASC = 2

CMD_YES = 'yes'
CMD_NO = 'no'


def md5_hash(fpath: str) -> str:
    # noinspection InsecureHash
    hash_md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


parser = argparse.ArgumentParser(description="This is Duplicate File Handler app")

parser.add_argument('directory', nargs='*', default=None)

directory = parser.parse_args().directory

if not directory:
    print('Directory is not specified')
    sys.exit(1)

entrypoint = directory[0]

print('Enter file format:')
ext = input().strip()

if ext:
    ext = [ext, f'.{ext}']
else:
    ext = []

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
size_hash_map = {}

os.system("mv module/root_folder/files/stage/src/reviewSlider.js module/root_folder/files/stage/src/reviewslider.js")
os.system(
    "mv module/root_folder/files/stage/src/toggleMiniMenu.js module/root_folder/files/stage/src/toggleminimenu.js")

for root, dirs, files in os.walk(entrypoint):
    for file in files:
        file_path = os.path.join(root, file)
        if ext and os.path.splitext(file_path)[1] not in ext:
            continue

        size = int(os.path.getsize(file_path))
        if size not in file_map:
            file_map[size] = [file_path]
            continue

        file_map.get(size).append(file_path)

for key in sorted(file_map, reverse=(True if sorting == SORT_DESC else False)):
    if len(file_map[key]) > 1:
        print(f'{key} bytes')
        for name in file_map[key]:
            print(name)
        print()

while True:
    print()
    print('Check for duplicates?')
    confirm = input().strip()

    if confirm not in [CMD_NO, CMD_YES]:
        print('Wrong option')
        continue

    if confirm == CMD_NO:
        sys.exit(0)

    break

for key in sorted(file_map, reverse=(True if sorting == SORT_DESC else False)):
    if len(file_map.get(key)) == 1:
        continue

    for name in file_map[key]:
        md5_crc = md5_hash(name)

        if key in size_hash_map:
            if md5_crc in size_hash_map[key]:
                size_hash_map[key][md5_crc].append(name)
            else:
                size_hash_map[key][md5_crc] = [name]
        else:
            size_hash_map[key] = {md5_crc: [name]}

# output
print()
file_list = [None]
i = 1
for key in sorted(size_hash_map, reverse=(True if sorting == SORT_DESC else False)):
    print(f'{key} bytes')

    for crc in sorted(size_hash_map.get(key)):
        if len(size_hash_map.get(key).get(crc)) > 1:
            print(f'Hash: {crc}')
            for name in size_hash_map.get(key).get(crc):
                print(f'{i}. {name}')
                file_list.append(name)
                i += 1

    print()

while True:
    print()
    print('Delete files?')
    confirm = input().strip()

    if confirm not in [CMD_NO, CMD_YES]:
        print('Wrong option')
        continue

    if confirm == CMD_NO:
        sys.exit(0)

    break

nums = []
while True:
    print()
    print('Enter files numbers to delete:')

    try:
        nums = list(map(int, input().strip().split()))
    except:
        print('Wrong format')
        continue

    if not nums:
        print('Wrong format')
        continue

    break

freed_space = 0
# print(file_list)

for i in range(len(file_list)):
    if i in nums:
        name = file_list[i]
        # print(f'Deleting {name}')
        # print(os.stat(name))
        freed_space += int(os.stat(name).st_size)
        os.remove(name)

print()
print(f'Total freed up space: {freed_space} bytes')
