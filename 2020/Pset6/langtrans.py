def partA():
    with open("input.txt", "r") as fp:
        grp_uniq_q = set()
        final_sum = 0
        for line in fp:
            if line == "\n":
                final_sum += len(grp_uniq_q)
                grp_uniq_q.clear()
            else:
                grp_uniq_q.update(line.strip())
                # print(grp_uniq_q)
        print(final_sum + len(grp_uniq_q))


def partB():
    with open("input.txt", "r") as fp:
        grp_uniq_q = set()
        final_sum = 0
        no_common = False

        for line in fp:
            # Check this is the end of the group
            if line == "\n":
                # print(len(grp_uniq_q))
                final_sum += len(grp_uniq_q)

                grp_uniq_q.clear()
                no_common = False

            # Skip the group as we found nothing in common between the first 2 people
            elif no_common:
                continue

            # Check if set is empty (we're starting a new group)
            elif not grp_uniq_q:
                grp_uniq_q.update(line.strip())

            else:
                # If no commonalities after the first add, we skip this group
                if grp_uniq_q.isdisjoint(line):
                    grp_uniq_q.clear()
                    no_common = True
                else:
                    grp_uniq_q.intersection_update(line)

        print(final_sum + len(grp_uniq_q))
        # assert final_sum + len(grp_uniq_q) == 6


part
