numsX = range(1, 1000)


def is_P(num):
    for y in range(2, num):
        if (num % y) == 0:
            return False
        return True


primeNumber = list(filter(is_P, numsX))

print(primeNumber)

# Easy calc for prime number in a list from 1 - 1000
