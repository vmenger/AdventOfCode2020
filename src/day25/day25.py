import itertools


def c(i: int, m:int):
    return (i * m) % 20201227


def loopsize(t, val=1):
    return next(i for i in itertools.count(1) if (val := c(val, 7)) == t)


def transform(i, loops, val=1):
    for k in range(loops):
        val = c(val, i)
    return val


if __name__ == '__main__':

    a = 19241437
    b = 17346587

    print(transform(a, loopsize(b)))
