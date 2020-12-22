def deck_score(deck):
    return sum((len(deck) - i) * val for i, val in enumerate(deck))


def run_part1(deck1, deck2):

    deck1, deck2 = deck1.copy(), deck2.copy()

    while len(deck1) * len(deck2) != 0:

        c1, c2 = deck1.pop(0), deck2.pop(0)

        if c1 > c2:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]

    return deck_score(deck1) if len(deck2) == 0 else deck_score(deck2)


def run_part2(deck1, deck2):

    deck1, deck2 = deck1.copy(), deck2.copy()
    mem = set()

    while len(deck1) * len(deck2) != 0:

        # 1: Check memory
        round_id = str(deck1) + str(deck2)

        if round_id in mem:
            return "player_1", deck1
        else:
            mem.add(round_id)

        # 2: Draw cards
        c1, c2 = deck1.pop(0), deck2.pop(0)

        # 3: Determine winner
        if (len(deck1) >= c1) and (len(deck2) >= c2):
            winner, _ = run_part2(deck1[:c1], deck2[:c2])
        else:
            winner = "player_1" if c1 > c2 else "player_2"

        # 4: Take cards
        if winner == "player_1":
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]

    return ("player_2", deck2) if len(deck1) == 0 else ("player_1", deck1)


if __name__ == '__main__':

    with open('input.txt') as file:
        deck1, deck2 = [list(map(int, x.split("\n")[1:])) for x in file.read().split("\n\n")]

    print(f"The solution to part 1 = {run_part1(deck1, deck2)}")
    print(f"The solution to part 2 = {deck_score(run_part2(deck1, deck2)[1])}")
