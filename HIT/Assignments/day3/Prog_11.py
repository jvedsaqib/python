di = {
      0 : "---",
      1 : "x--",
      2 : "w--",
      3 : "wx-",
      4 : "r--",
      5 : "rx-",
      6 : "rw-",
      7 : "rwx",
      }

o = input("Input octal value (_ _ _): ")

s = ""


for i in o:
    s += str(di.get(int(i)))

print(s)