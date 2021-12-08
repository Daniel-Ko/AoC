def find_row(partitions: str, low: int, high: int) -> int:
    # print(f"{partitions}, {low}-{high}")
    if not partitions:
        return low
    if partitions[0] == "F":
        return find_row(partitions[1:], low, low+(high-low)//2)
    return find_row(partitions[1:], (low+(high-low)//2)+1, high)


def find_seat(row: str, low: int, high: int) -> int:
    if not row:
        return low
    if row[0] == "L":
        return find_seat(row[1:], low, low+(high-low)//2)
    return find_seat(row[1:], (low+(high-low)//2)+1, high)


def get_seatID(row, seat):
    return row*8 + seat


with open("input.txt", "r") as f:
    max_seatID = 0
    for line in f:
        line = line.strip()
        row = find_row(line[:7], 0, 127)
        seat = find_seat(line[7:], 0, 7)
        max_seatID = max(max_seatID, get_seatID(row, seat))
    print(max_seatID)


def test():
    inputs = ("FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL")
    for inp in inputs:
        row = find_row(inp[:7], 0, 127)
        seat = find_seat(inp[7:], 0, 7)
        seatID = get_seatID(row, seat)
        print(f"{row}, {seat}: {seatID}")


# test()
