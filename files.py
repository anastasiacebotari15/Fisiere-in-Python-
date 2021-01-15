with open ('text.txt', 'r') as f:
    a=f.read()
    l= [c for c in a if c.islower()]
with open ('litereA.txt', 'w') as f:
    f.write(str(l))
with open ('text.txt', 'r')as f:
    a=f.read()
    x= [u for u in a if a.isupper()]
with open ('litereB.txt', 'w') as f:
    f.write(str(x))

    
    
    