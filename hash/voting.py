voted = {}


def verify_voter(name):
    if voted.get(name):
        print("Voting concluded")
    else:
        voted[name] = True
        print("Let me vote")


verify_voter("Mike")
verify_voter("Tom")
verify_voter("Mike")

print(voted)

