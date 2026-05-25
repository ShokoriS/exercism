def steps(number):

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0

    operations = [lambda number: number // 2, lambda number: number * 3 + 1]
    steps = 0
    while number > 1:
        number = operations[number % 2](number)
        steps += 1

    return steps

