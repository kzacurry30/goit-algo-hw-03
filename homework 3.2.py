import random


def get_numbers_ticket(min_num, max_num, quantity):

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []


    numbers = random.sample(range(min_num, max_num + 1), quantity)


    numbers.sort()

    return numbers



print(get_numbers_ticket(1, 49, 6))  # Наприклад, для лотереї 6 з 49
print(get_numbers_ticket(1, 36, 5))  # Наприклад, для лотереї 5 з 36
