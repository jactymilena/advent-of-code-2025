from utils.reader import read_file

def is_in_range(n, fresh_range):
    return n >= fresh_range[0] and n <= fresh_range[1]


def main():
    file_path = 'input/day5-input.txt'
    file = read_file(file_path)
    start_id_index = 0
    ranges = []

    for i, line in enumerate(file):
        if line == '\n':
            start_id_index = i + 1
            break
        a, b = line.replace('\n', '').split('-')
        ranges.append([int(a), int(b)])

    fresh_ingrs = []
    for ingr_id in file[start_id_index:]:
        for fresh_range in ranges:
            ingr_id = int(ingr_id)
            if is_in_range(ingr_id, fresh_range):
                fresh_ingrs.append(ingr_id)
                break
    print(len(fresh_ingrs))

main()