n=int(input())
e=0
o=0
ep=0
op=0
while n:
	r=n%10
	if r%2==0:
		e+=r*(10**ep)
		ep+=1
	else:
		o+=r*(10**op)
		op+=1
	n//=10
print("Even number", e)
print("Odd number", o)
print("Even square", e*e)
print("Odd square", o*o)