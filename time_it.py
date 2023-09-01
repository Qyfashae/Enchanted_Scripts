# The "timeit" module lets you measure the execution time of small bits of python code

import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

0.3412662749997253

>>> timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)

0.2996307989997149

>>> timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)

0.24581470699922647

# the prints are only how long it took for the execution of the code/script to happend in ms
