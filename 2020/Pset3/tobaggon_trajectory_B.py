def test_skip(right, down):
    trees_encountered = 0
    col = 0
    skip = 0

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            if skip > 1:
                skip -= 1
            else:
                print(f"enumerating line {i}")
                line = line.rstrip()

                if line[col % len(line)] == "#":
                    trees_encountered += 1
                skip = down
                col += right
    return trees_encountered


def test_skip2(right, down):
    input = """..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"""
    trees_encountered = 0
    col = 0
    skip = 0

    for i, line in enumerate(input.split()):
        if skip > 1:
            skip -= 1
        else:
            print(f"{i}: ({col}) {line}")
            line = line.rstrip()
            if line[col % len(line)] == "#":
                trees_encountered += 1
            skip = down
            col += right
    return trees_encountered


def num_collisions(right, down):
    trees_encountered = 0
    col = 0
    skip = 0  # Start skip at 0 because we want to evaluate the first line

    with open("input.txt", "r") as f:
        for line in f:
            if skip > 1:
                skip -= 1
            else:
                # VERY IMPORTANT TO USE RSTRIP just in case it changes the string
                line = line.rstrip()

                if line[col % len(line)] == "#":
                    trees_encountered += 1
                skip = down  # Reset so we can count how many "loop continues" we need to do
                col += right  # Important to only do if you enumerate!
    print(
        f"with r {right} and d {down}, you encounter {trees_encountered} trees")
    return trees_encountered


# print(test_skip(1, 2))
print(
    num_collisions(1, 1)
    * num_collisions(3, 1)
    * num_collisions(5, 1)
    * num_collisions(7, 1)
    * num_collisions(1, 2)
)

# 1200429120
