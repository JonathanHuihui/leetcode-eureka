#!/usr/bin/env python3

# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7 
#  
def fibonacci(index: int) -> int:
    if index == 0:
        return 1
    return index + fibonacci(index-1)

print(fibonacci(index=5))




