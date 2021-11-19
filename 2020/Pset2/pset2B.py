def test_valid_passwd(potent_index1, potent_index2, given_letter, passwd):
    if passwd[potent_index1] == given_letter:
        if passwd[potent_index2] != given_letter:
            return 1
    elif passwd[potent_index2] == given_letter:
        return 1
    return 0


def tests():
    assert test_valid_passwd(0, 2, "a", "abcde") == 1
    assert test_valid_passwd(0, 2, "b", "cdefg") == 0
    assert test_valid_passwd(0, 4, "c", "ccccc") == 0


tests()
passing = 0
with open("input.txt", "r") as f:
    for line in f:
        policy, given_letter, passwd = line.split()

        given_letter = given_letter.strip(":")
        potent_index1, potent_index2 = [
            int(indx)-1 for indx in policy.split("-")]  # -1 to transform rules into 0-based index

        passing += test_valid_passwd(potent_index1,
                                     potent_index2, given_letter, passwd)
        # print(f"{low}, {high}, {occurences}")

print(passing)
