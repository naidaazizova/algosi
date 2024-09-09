a,b =open('input.txt').read().split()
a=int(a)
b=int(b)

open('output.txt','w').write(str(a+b))
