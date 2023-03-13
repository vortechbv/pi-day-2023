def fib_mod(n):
    """Generator for the list of Fibonacci numbers modulo N.
    """
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a % n


def cycle_length(fibs):
    """Find the cycle length of a Fibonacci sequence, or returns False if no cycle present.
       A cycle is found if there are two adjacent numbers that are equal to the last two numbers of the list.
    """
    last_elements = fibs[-2:]
    for i in range(1, len(fibs)-1):
        if fibs[-i-2:-i] == last_elements:
            return i
    return False


def pisano(n):
    """Get the nth Pisano period.
    """
    fibs = []
    for f in fib_mod(n):
        fibs.append(f)
        c = cycle_length(fibs)
        if c:
            return c


def get_pisano_numbers(ns):
    return [pisano(n) for n in ns]
