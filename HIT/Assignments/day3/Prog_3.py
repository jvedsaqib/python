# 3. Extract unique values from a dictionary.

di = {
      1 : 'A',
      2 : 'B',
      3 : 'A',
      4 : 'C',
      5 : 'C',
      6 : 'C',
      }

s = {x for x in di.values()}
print(s)