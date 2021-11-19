import re


def challenge():
    with open("input.txt", "r") as f:
        passports_data = [batch.strip() for batch in f.read().split("\n\n")]
        valid_passports = 0
        field_tags = (
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        )
        for passport in passports_data:
            sep_fields = [sep_field.split(":")
                          for sep_field in passport.split()]
            passport_values = {fieldval[0]: fieldval[1] for fieldval in
                               sep_fields}
            if not all(field_tag in passport_values.keys() for field_tag in field_tags):
                continue

            if all(
                (validateBirthYear(passport_values["byr"]), validateIssueYear(passport_values["iyr"]), validateExpYear(passport_values["eyr"]), validateHeight(
                    passport_values["hgt"]), validateHairColour(passport_values["hcl"]), validateEyeColour(passport_values["ecl"]), validatePassID(passport_values["pid"])
                 )):
                valid_passports += 1
        return valid_passports


def validateBirthYear(byr: str):
    return re.search("^\d{4}$", byr) and 1920 <= int(byr) <= 2002


def validateIssueYear(iyr: str):
    return re.search("^\d{4}$", iyr) and 2010 <= int(iyr) <= 2020


def validateExpYear(eyr: str):
    return re.search("^\d{4}$", eyr) and 2020 <= int(eyr) <= 2030


def validateHeight(hgt: str):
    if re.search("^\d+cm|in$", hgt):
        return ("cm" in hgt and 150 <= int(hgt[:-2]) <= 193) or ("in" in hgt and 59 <= int(hgt[:-2]) <= 76)


def validateHairColour(hcl: str):
    return re.search("^\#[0-9|a-f]{6}$", hcl)


def validateEyeColour(ecl: str):
    return re.search("^(amb|blu|brn|gry|grn|hzl|oth){1}$", ecl)


def validatePassID(pid: str):
    return re.search("^\d{9}$", pid)


def testValidations():
    assert validateBirthYear("1990")
    assert not validateBirthYear("199a")

    assert validateHeight("150cm")
    assert validateHeight("70in")
    assert not validateHeight("150")
    assert not validateHeight("150 cm")

    assert validateHairColour("#aaa000")
    assert not validateHairColour("# aaa000")
    assert not validateHairColour("#aaa000a")

    assert validateEyeColour("brn")
    assert not validateEyeColour("brnamb")
    assert not validateEyeColour("wat")

    assert validatePassID("000000000")
    assert not validatePassID("0000000001")


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
    for passport in passports_data:
        print([sep_field.split(":") for sep_field in passport.split(" ")])
        passport_values = {fieldval[0]: fieldval[1] for fieldval in
                           sep_field.split(":") for sep_field in passport.split(" ")}
        print(passport_values)


if __name__ == "__main__":
    print(challenge())
    testValidations()
    # test()
