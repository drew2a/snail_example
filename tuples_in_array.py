from random import randrange


def _find_second(array, first, value):
    for a in array:
        if a + first == value:
            return a

    return None


def random_array(size, limit=10):
    for i in range(size):
        yield randrange(0, limit)


def find_tuples(array, value):
    result = []
    digits = dict()

    for i in array:
        if i > value:
            continue

        if i not in digits:
            digits[i] = 0
        elif i in digits:
            if i + i == value:
                result.append(tuple((i, i)))
                del digits[i]
            else:
                second = _find_second(digits.keys(), i, value)
                if second is not None:
                    result.append(tuple((i, second)))
                    del digits[second]

    return result
