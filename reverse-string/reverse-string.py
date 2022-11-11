!/usr/bin/env python


def reverse_string(word):
  drow = ''
  for char in word:
    drow += char
  print(drow)

  drow = ''
  i = len(word) - 1
  while i >= 0:
    print(word[i])
    drow += word[i]
    i -= 1
  #drow = ''.join(str(char) for char in holder)
  # there might be a way to do this simultaneously
  print(drow)
  return drow


reverse_string('Hi my name is Jonathan')