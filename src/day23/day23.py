from common.utils import timeit
from itertools import chain
from typing import List

class CupListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class CupList:

    def __init__(self, input):

        first_val = next(input)
        self.current_node = CupListNode(first_val)
        self.val_to_node = {first_val: self.current_node}

        iter_node = self.current_node

        for i in input:
            new_node = CupListNode(i)
            self.val_to_node[i] = new_node
            iter_node.next = new_node
            iter_node = new_node
        else:
            iter_node.next = self.current_node  # wrap around

    def head(self) -> int:
        return self.current_node.val

    def rotate_by_one(self) -> int:
        val = self.current_node.val
        self.current_node = self.current_node.next
        return val

    def rotate_to_val(self, val: int):
        self.current_node = self.val_to_node[val]

    def pop_next_n(self, n_pops: int) -> List[CupListNode]:

        iter_node = self.current_node.next
        output = []

        for _ in range(n_pops):
            output.append(iter_node)
            iter_node = iter_node.next
        else:
            self.current_node.next = iter_node

        return output

    def insert_at(self, val: int, insert: List[CupListNode]):

        start_node = self.val_to_node[val]
        insert[-1].next = start_node.next
        start_node.next = insert[0]


@timeit
def run(cups: CupList, num_iterations: int, max_val: int):

    for p in range(num_iterations):

        # if p%(num_iterations/10000) == 0:
        #     print(f"Currently at {p} = {100*(p/num_iterations):.1f}%")

        current_label = cups.head()
        three_cups = cups.pop_next_n(3)
        three_cups_values = [cup.val for cup in three_cups]

        insert_at = current_label-1

        while (insert_at in three_cups_values) or (insert_at == 0):
            if insert_at == 0:
                insert_at = max_val
            else:
                insert_at -= 1

        cups.insert_at(insert_at, three_cups)
        cups.rotate_by_one()

    return cups


def run_part1(input: List[int], iterations: int):

    cups = CupList(iter(input))
    run(cups, iterations, max(input))
    cups.rotate_to_val(1)
    cups.rotate_by_one()

    return ''.join(str(cups.rotate_by_one()) for _ in range(len(input)))


def run_part2(input: List[int], iterations: int, max_val: int):

    cups = CupList(chain(input, range(len(input)+1, max_val+1)))
    run(cups, iterations, max_val)

    cups.rotate_to_val(1)
    cups.rotate_by_one()
    return cups.rotate_by_one() * cups.rotate_by_one()


if __name__ == '__main__':

    input = [int(x) for x in list('853192647')]

    print(f"The solution to part 1 = {run_part1(input, iterations=100)}")
    print(f"The solution to part 2 = {run_part2(input, iterations=10000000, max_val=1000000)}")


