def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    return number == sum(d ** len(digits) for d in digits)
