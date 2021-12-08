trees_encountered = 0
col = 0

with open("input.txt", "r") as f:
    for line in f:
        # VERY IMPORTANT TO USE RSTRIP just in case it changes the string
        line = line.rstrip()

        if line[col % len(line)] == "#":
            trees_encountered += 1
        col += 3
print(trees_encountered)


def test():
    input = """..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"""

    trees_encountered = 0
    col = 0
    for i, line in enumerate(input.split()):
        if line[col % len(line)] == "#":
            trees_encountered += 1
        col += 3
    assert trees_encountered == 7
    assert i+1 == 11  # Don't forget we start at 0 for i
    # 1st line is 0, not 3. But we increment one final time, so we're 3 ahead of the final col
    assert col == 11 * 3


def test2():
    trees_encountered = 0
    col = 0
    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            if i == 13:
                col += 3
                break
            print(col % len(line), end=", ")
            if line[col % len(line)] == "#":
                trees_encountered += 1
                print(str(i) + ": " + line[:col % len(line)] +
                      "X" + line[col % len(line)+1:], end="")
            else:
                print(str(i) + ": " + line[:col % len(line)] +
                      "O" + line[col % len(line)+1:], end="")
            col += 3

        # Reset back to the last col (we went 3 past by accident)
        col -= 3
        assert i == 13
        # len(line) = 32. So 13 * 3 = 39 and that's 39-32 = 7
        assert col % len(line) == 7
        assert col == 13*3
        assert trees_encountered == 4


# test()
# test2()
