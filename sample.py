def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return 'FizzBuzz'
    elif input % 5 == 0:
        return 'Fizz'
    elif input % 3 == 0:
        return 'Buzz'
    return input