#!/usr/bin/env python3

class Solution:
    def find_repeats(self, nums: list[int]) -> int:
        ndict = {}
        for num in nums:
            if num in ndict:
                return num
            ndict[num] = True
        return None



sol = Solution()
print(sol.find_repeats([1,2,3,2,4,5,6,4,1,2,4]))

print(sol.find_repeats([6,5,7,1,8,2,3,9,4,10]))

