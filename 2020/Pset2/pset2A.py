passing = 0
with open("input.txt", "r") as f:
    for line in f:
        policy, given_letter, passwd = line.split()

        given_letter = given_letter.strip(":")
        low, high = [int(bound) for bound in policy.split("-")]
        occurences = passwd.count(given_letter)

        if low <= occurences and occurences <= high:
            passing += 1
        # print(f"{low}, {high}, {occurences}")

print(passing)
