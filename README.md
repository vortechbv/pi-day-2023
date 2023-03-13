The Pisano period
=================

The Fibonacci series starts with [0, 1, 1, 2, ...] and has ever increasing numbers further down the series.
If you take these numbers modulo `n`, then the series will eventually become periodical.

This is called the [Pisano period][1] π(n). The series of Pisano numbers for n = [1, 2, 3, ...] is [A001175][2].


The challenge
-------------

Write a function `get_pisano_numbers()` in Python, which for a list of numbers `n` returns
the corresponding list of `π(n)`.  For example, `get_pisano_numbers([1,3])` would return `[1,8]`.

The winner is the function that is both the shortest and the fastest.


The rules
---------

 * The software used is Python 3.11.  Only modules from the standard library can be used, no numpy or other dependencies.
 * A submission should be a standalone `.py` file.
 * The score is the sum of the file size in bytes and the time to execute `get_pisano_numbers()` in miliseconds.
   Lower score wins.
 * Before scoring, the .py files are processed by `autopep8 --max-line-length 99999`, in order to limit
   tricks with removal of whitespace to some degree.
 * The input is a list of randomly chosen numbers from the range 2..6000.
   The list is 400 numbers long and the same for each submission.
 * The code is executed on a 16 core AMD CPU.


Examples
--------

As an example there are two implementations in the repository, together with a test script that executes them and prints a score.
Output of `test.py`:
```
    NAME                    RESULT    TIME    SIZE   SCORE
    pisano_example1         PASS         0   33004   33004
    pisano_example2         PASS    397668     794  398462
```

The first example includes all Pisano periods for 1..6000 hardcoded in the source.
This makes the execution very fast, but has a high score because of the file size.

The second example calculates all the requested numbers.
This is a lot smaller, but execution takes a very long time.



[1]: https://en.wikipedia.org/wiki/Pisano_period
[2]: https://oeis.org/A001175
