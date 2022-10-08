from java.lang import System
from java.lang import Math
System.out.println("Basic maths")
n=int(input("Enter a number:"))
print "Square root of the number is : ",Math.sqrt(n)
print "Logarithm of the number is : ", Math.log(n)
print "Log 10 of the number is : ",Math.log10(n)
print "Exponent of the number is : ",Math.exp(n)
print "Exponentm 1 of the number is : ",Math.expm1(n)
print "Sine of the number : ",Math.sin(n)
print "Cos of the number : ",Math.cos(n)
print "Tan of the number: ",Math.tan(n)
print "Absolute value of the number: ",Math.abs(n)
print "Cube root of the number: ",Math.cbrt(n)
print "FIBONACCI SERIES"
a,b=0,1
c=0
while c<n:
    print(a)
    nth=a+b
    a=b
    b=nth
    c=c+1
print("---- THE END ---")



