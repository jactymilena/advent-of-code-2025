from utils.reader import read_file

file_path = 'input/day1-input.txt'

rots = read_file(file_path, True)

dial = 50
num_zero = 0

for rot in rots:
    rot_num = rot[1:]
    if rot[0] == "R":
        dial += int(rot_num)
    elif rot[0] == "L":
        dial -= int(rot_num)
    
    dial = dial % 100

    if dial == 0:
        num_zero += 1 
    print(dial)

print(f"final {dial} num_zero {num_zero}")