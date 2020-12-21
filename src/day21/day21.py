from collections import defaultdict
from pprint import pprint

if __name__ == '__main__':

    with open('input.txt') as file:
        input = file.read().splitlines()

    foods = [line.split(" (")[0].split(" ") for line in input]
    food_allergens = [line.split("(")[1][9:-1].split(", ") for line in input]

    mapping = defaultdict(lambda: [])
    for ingredients, food_allergens in zip(foods, food_allergens):
        for allergen in food_allergens:
            mapping[allergen].append(set(ingredients))

    counter = defaultdict(lambda: 0)
    for ingredients in foods:
        for ingredient in ingredients:
            counter[ingredient] += 1

    # Part 1
    can_contain_allergens = set.union(*[set.intersection(*v) for k, v in mapping.items()])

    print(sum(counter[allergen]
              for allergen in counter
              if allergen not in can_contain_allergens
              )
          )

    # Part 2
    # only 8 allergens, easier to just finish this in excel :-)
    pprint([(k, set.intersection(*v)) for k, v in mapping.items()])

