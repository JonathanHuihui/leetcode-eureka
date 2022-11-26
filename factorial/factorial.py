#!/usr/bin/env python3

def factorial(number):
    if number == 2:
        return number
    return (number)*factorial(number-1)

def iteration(number: int) -> int:
    answer = number
    while number > 1:
        number -= 1
        answer *= number
    return answer




#print(iteration(number=5))

print(factorial(number=5))
