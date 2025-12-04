from utils.reader import read_file


def main():
    file_path = 'input/day3-input.txt'
    file = read_file(file_path)
    joltages_sum = 0

    for i, bank in enumerate(file):
        batteries = [int(i) for i in bank.strip()]
        max_12_jolt = [-1] * 12 

        for i, jolt in enumerate(batteries):
            for k in range(len(max_12_jolt)):
                if len(batteries) - i >= 12 - k:
                    if jolt > max_12_jolt[k]:
                        max_12_jolt[k] = jolt
                        max_12_jolt[k + 1:] = [-1] * (11 - k)
                        break

        
        max_joltage = ''.join(str(x) for x in max_12_jolt if x != -1)
        joltages_sum += int(max_joltage)

    print(f"joltages_sum : {joltages_sum}")
                

main()