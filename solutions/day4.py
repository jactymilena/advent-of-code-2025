from utils.reader import read_file


def main():
    file_path = 'input/day4-input.txt'
    file = read_file(file_path)
    rolls_diagram = [[] for _ in range(len(file))]
    
    for i, line in enumerate(file):
        for j, char in  enumerate(line.strip()):
            rolls_diagram[i].append(char)
            print(rolls_diagram[i][j], end='')
        print()

    adjacents_points = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    invalid_rolls = 0
    old_invalid_rolls = -1
    while invalid_rolls != old_invalid_rolls:
        old_invalid_rolls = invalid_rolls
        for i in range(len(rolls_diagram)):
            for j in range(len(rolls_diagram[i])):
                adjacent_count = 0

                if rolls_diagram[i][j] == '@':
                    for adj in adjacents_points:
                        adj_i = i + adj[0]
                        adj_j = j + adj[1]
                        if 0 <= adj_i < len(rolls_diagram) and 0 <= adj_j < len(rolls_diagram[i]):
                            if rolls_diagram[adj_i][adj_j] == '@':
                                adjacent_count += 1

                    if adjacent_count < 4:
                        rolls_diagram[i][j] = '.'
                        invalid_rolls += 1


    print("Final rolls diagram:")
    for i in range(len(rolls_diagram)):
        for j in range(len(rolls_diagram[i])):
            print(rolls_diagram[i][j], end='')
        print()

    print(f"invalid_rolls : {invalid_rolls}")
    
main()