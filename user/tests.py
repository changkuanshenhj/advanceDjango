from django.test import TestCase


def duplicate(numbers, length):
    if numbers is None or length <= 0:
        return False, -1
    for number in numbers:
        if number < 0 or number > length - 1:
            return False, -1
    index1 = -1
    for number in numbers:
        index1 = numbers.index(number, index1+1)
        while number != index1:
            if number == numbers[number]:
                return True, number
            temp = number
            numbers[index1] = numbers[temp]
            numbers[temp] = temp
            number = numbers[index1]
    return False, -1

# Create your tests here.


if __name__ == '__main__':
    a = [2, 3, 1, 0, 2, 5, 3]
    b, duplication = duplicate(a, len(a))
    print(b, duplication)
