def slices(input: str, max_size: int = 3):

    if max_size == 1:
        yield [input]

    else:
        for i in range(1, len(input)):
            for p in slices(input[i:], max_size-1):
                yield [input[:i]] + p


def match(input: str, disj_clauses: list):

    if (input, str(disj_clauses)) in mem:
        return mem[(input, str(disj_clauses))]

    for clauses in disj_clauses:

        if len(input) < len(clauses):
            return False

        if (len(clauses) == 1) and not clauses[0].isnumeric():
            return input == clauses[0]

        for split in slices(input, max_size=len(clauses)):

            if all(match(a, rules[int(b)]) for a, b in zip(split, clauses)):
                mem[(input, str(disj_clauses))] = True
                return True

    mem[(input, str(disj_clauses))] = False
    return False

if __name__ == '__main__':

    with open('input_p2.txt') as file:
        rules, messages = [line.split("\n") for line in file.read().split("\n\n")]

    def rule_to_sublists(val: str):
        return [x for clause in val.split(" | ") for x in [clause.split(' ')]]

    rules = [rule.replace("\"", "").split(": ") for rule in rules]
    rules = {int(head): rule_to_sublists(val) for head, val in rules}

    sum = 0
    mem = dict()

    print(sum(match(message, rules[0]) for message in messages))