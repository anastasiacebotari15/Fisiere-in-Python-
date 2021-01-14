with open ('globulet.txt', 'r') as f:
    a=f.readline()
    r=int(a)+3
    ar=int(a)+ int(r)
    b=int(ar) -2
    s=int(ar)+ int(b)
with open ('bradut.txt', 'w') as f:
    f.write(str(s))