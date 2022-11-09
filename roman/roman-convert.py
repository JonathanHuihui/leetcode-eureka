#!/usr/bin/env python3
# Initially I wanted to do a for loop, however
# in order to account for the case of IV, CM, etc.
# the index should be iterated over a variable 
# distance.
# I ended up using a more brute force method
# of a nested if statement in order to 
# fix the issue of running out of index
# when I check for a pair of characters.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        rdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        index = 0 

        while index < len(s):
          char = s[index]
          if index < (len(s)-1):
            if rdict[char] < rdict[s[index+1]]:
              number += rdict[s[index+1]] - rdict[char]
              index += 2
            else: 
              number += rdict[char]    
              index += 1
          else:
            number += rdict[char]  
            index += 1
          print(number)

        return number

sol = Solution()
print(sol.romanToInt('XXVII'))
# XXVII
# MCMXCIV
# M CM XC IV
