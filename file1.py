with open ("numere.txt", "r") as f:
    a=f.readline()
    b=f.readline()
if int(a)> int(b):
    x=int(b)
if int(b)> int(a):
    x=int(a)
with open("minim.txt", "w") as f:
    f.write(str(x))
    