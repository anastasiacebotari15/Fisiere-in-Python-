with open ('input.txt', 'r') as f:
    a=f.readline()
    b=int(a)-2
    c=int(b)+1
    d=int(a)+1
    e=int(d)+1
with open ('output.txt', 'w') as f:
    f.write(str(b))
    f.write('  ')
    f.write(str(c))
    f.write('  ')
    f.write(str(a))
    f.write('  ')
    f.write(str(d))
    f.write('  ')
    f.write(str(e))
    f.write('  ')