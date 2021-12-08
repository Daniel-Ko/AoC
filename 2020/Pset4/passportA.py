with open("input.txt", "r") as f:
    passport_data = [batch.strip() for batch in f.read().split("\n\n")]
    valid_passports = 0
    fields = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    )
    for passport in passport_data:
        if all(field in passport for field in fields):
            valid_passports += 1
    print(valid_passports)


def test():
    input = """ecl: gry pid: 860033327 eyr: 2020 hcl:  # fffffd
            byr: 1937 iyr: 2017 cid: 147 hgt: 183cm

            iyr: 2013 ecl: amb cid: 350 eyr: 2023 pid: 028048884
            hcl:  # cfa07d byr:1929

            hcl:  # ae17e1 iyr:2013
            eyr: 2024
            ecl: brn pid: 760753108 byr: 1931
            hgt: 179cm

            hcl:  # cfa07d eyr:2025 pid:166559648
            iyr: 2011 ecl: brn hgt: 59in"""
    passport_data = [batch.strip() for batch in input.split("\n\n")]
    valid_passports = 0
    fields = (
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    )
    for passport in passport_data:
        if all(field in passport for field in fields):
            valid_passports += 1
    assert valid_passports == 2
