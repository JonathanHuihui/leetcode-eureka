#!/usr/bin/env python3
def merge_sorted_arrays(a0, a1):
  aSort = []

  if len(a0) == 0:
    return a1
  elif len(a1) == 0:
    return a0
  
  i0 = i1 = 0
  while i1 < len(a1) and i0 < len(a0):
    if a1[i1] <= a0[i0]: # either trial could be <=
      aSort.append(a1[i1])
      i1 += 1
    elif a0[i0] <= a1[i1]: 
      aSort.append(a0[i0])
      i0 += 1  
    # else:
    #   aSort.append(a0[i0])
    #   i0 += 1
    #   aSort.append(a1[i1])
    #   i1 += 1

  while i1 < len(a1) and i0 == len(a0):
      aSort.append(a1[i1])
      i1 += 1

  while i0 < len(a0) and i1 == len(a1):
      aSort.append(a0[i0])
      i0 += 1

  return aSort


A0= [1,2,3,5,7,25]
A1 = [3,6,9,13,20]
print(merge_sorted_arrays(A0, A1))