from utils.reader import read_file


def has_patterns(str_id):
    str_id = str(int(str_id))

    if len(str_id) % 2 != 0:
        return 0
    mid = len(str_id) // 2
    if str_id[:mid] == str_id[mid:]:
        return 1
    return 0

def main():
    file_path = 'input/day2-input.txt'
    file = read_file(file_path)

    sum_patterns = 0
    for line in file:
        line_elements = line.split(',')
        for el in line_elements:
            if el != '\n':
                ids = el.split('-')
                # print(ids)
                for i in range(int(ids[0]), int(ids[1]) + 1):
                    n = has_patterns(i)
                    if n == 1:
                        sum_patterns += int(i)

    print(f"sum patterns : {sum_patterns}")

main()