f1=1
f2=1

n=open('input.txt').read()
n=int(n)
for x in range(2,n):
    f1,f2 = f2, f1+f2
open('output.txt', 'w').write(str(f2))
