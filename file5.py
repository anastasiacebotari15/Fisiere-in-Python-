with open('numar.txt', 'r') as f:
    n=f.readline()
a=int(n)*1
b=int(n)*2
c=int(a)*3
d=int(a)*4
e=int(a)*5
k=int(a)*6
g=int(a)*7
h=int(a)*8
i=int(a)*9
j=int(a)*10
with open('inmultire.txt', 'w') as f:
    f.write(str(n) + '*1' + '=' + str(a))
    f.write('\n')
    f.write(str(n) + '*2' + '=' + str(b))
    f.write('\n')
    f.write(str(n) + '*3' + '=' + str(c))
    f.write('\n')
    f.write(str(n) + '*4' + '=' + str(d))
    f.write('\n')
    f.write(str(n) + '*5' + '=' + str(e))
    f.write('\n')
    f.write(str(n) + '*6' + '=' + str(k))
    f.write('\n')
    f.write(str(n) + '*7' + '=' + str(g))
    f.write('\n')
    f.write(str(n) + '*8' + '=' + str(h))
    f.write('\n')
    f.write(str(n) + '*9' + '=' + str(i))
    f.write('\n')
    f.write(str(n) + '*10' + '=' + str(j))