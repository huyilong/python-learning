#fibonacci numbers module
#could directly input python3 on mac terminal to invoke version 3
def fib(n):
	a, b = 0, 1
	while b < n:
		print( b),
		#there is a trailing comma "," after the print to indicate not print output a new line 
		a, b = b, a+b
		print #this is print out a empty line 
		#if you use print() then it will actually output a () rather than a new line
		


def fib2(n):
	result = []
	a, b =0, 1
	while b<n:
		result.append(b)
		a, b = b, a+b
	return result

if __name__=="__main__":
	#here the __name__ and __main__ all have two underlines! not only one _!
	import sys
	fib(int(sys.argv[1]))

print("hello, this is my first module for fibonacci numbers generator")
print("Usage: fibo_module.fib(1000)")