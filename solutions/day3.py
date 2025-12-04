from utils.reader import read_file

def main():
    file_path = 'input/day3-input.txt'
    file = read_file(file_path)
    max_joltage = ''
    joltages_sum = 0
    max1_setted = False
    
    for i, bank in enumerate(file):
        batteries = [int(i) for i in bank.strip()]
        max1 = -1
        max2 = -1
        for i, joltage in enumerate(batteries):
            if i < len(batteries) - 1:
                new_max1 = max(joltage, max1)
                if new_max1 > max1:
                    max1 = new_max1
                    max2 = batteries[i + 1]
                    max1_setted = True
            if i > 0 and not max1_setted:
                max2 = max(joltage, max2)

            max1_setted = False
        
        max_joltage = str(max1) + str(max2)
        joltages_sum += int(max_joltage)
    print(f"sum joltags : {joltages_sum}")

main()