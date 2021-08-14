def getduplication(numbers_2):
    if len(numbers_2) <= 0 and numbers_2 is None:
        return -1
    start = 1
    end = len(numbers_2) - 1
    while end >= start:
        middle = ((end - start) >> 1) + start
        count_1 = countrange(numbers_2, start, middle)
        if end == start:
            if count_1 > 1:
                return start
        if count_1 > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return -1


def countrange(numbers_1, start, end):
    count = 0
    for i in numbers_1:
        if start <= i <= end:
            count += 1
    return count


if __name__ == '__main__':
    numbers = [1, 2, 2, 4, 5, 6, 7, 4]
    # numbers = []
    duplication = getduplication(numbers)
    print("重复的数字是%d" % duplication)
