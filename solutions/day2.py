from utils.reader import read_file


def has_patterns(str_id):
    str_id = str(int(str_id))
    str_len = len(str_id)

    for i in range(1, str_len):
        if str_len % i == 0:
            pattern = str_id[0:i]
            if pattern * (str_len // i) == str_id:
                return True   
    return False


def main():
    file_path = 'input/day2-input.txt'
    file = read_file(file_path)

    sum_patterns = 0
    for line in file:
        line_elements = line.split(',')
        for el in line_elements:
            if el != '\n':
                ids = el.split('-')
                for i in range(int(ids[0]), int(ids[1]) + 1):
                    n = has_patterns(i)
                    if n == 1:
                        sum_patterns += int(i)

    print(f"sum patterns : {sum_patterns}")

main()