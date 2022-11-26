#!/usr/bin/env python3

def factorial(number: int):
    if number == 2:
        return number
    number-=1
    return (number+1)*factorial(number)

def iteration(number: int) -> int:
    answer = number
    while number > 1:
        number -= 1
        answer *= number
    return answer




#print(iteration(number=5))

print(factorial(number=5))
