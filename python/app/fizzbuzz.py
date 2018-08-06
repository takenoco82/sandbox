from .IllegalArgmentError import IllegalArgmentError


def fizzbuzz(n):
    validate(n)

    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return str(n)


def validate(n):
    if n is None:
        raise IllegalArgmentError
    if n is '':
        raise IllegalArgmentError
    if type(n) is not int:
        raise IllegalArgmentError
    if n < 0:
        raise IllegalArgmentError
