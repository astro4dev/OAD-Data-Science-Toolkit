# Python Pre-Assessment

This assessment is design to test a students prior knowledge of Python.

### Q1 - How would you define a variable, a, and set it's value equal to 5 in python?

a) ```def variable(a):```  
b) ```a = 5```  
c) ```a == 5```  
d) ```a = 5;```  


### Q2 - What is the output of print str[2:5] given str = 'Hello World!'?

a) ```ello W```  
b) ```llo ```  
c) ```llo Wo```  
d) ```lo Wo```  

### Q3 - What is the output list*5 given list = ['a','b',12]

a) ```['a', 'b', 12, 'a', 'b', 12, 'a', 'b', 12, 'a', 'b', 12, 'a', 'b', 12]```  
b) ```['aaaaa', 'bbbbb', 60]```  
c) ```[['a','b',12],['a','b',12],['a','b',12],['a','b',12],['a','b',12]]```  
d) list*5 produces an error because you can't multiply an int by a mixed array.

### Consider the following piece of code

```python 
import numpy

a = numpy.array([1,2,3,4,5])

for i in range(len(a)):
	b = i*a

print(b)
```

### Q4 - What is numpy?

a) A header file  
b) A program  
c) A reference to a file called numpy on the computer  
d) A package  

### Q5 - What are the values of i?

a) 0, 1, 2, 3, 4  
b) 1, 2, 3, 4, 5  
c) i does not change  
d) [1, 2, 3, 4, 5]  

### Q6 - What would the output of the program be if a = [1,2,3,4,5]

a) Would not work. You need an array for multiplication to work.  
b) [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  
c) [ 4  8 12 16 20]  
d) [1, 2, 3, 4, 5]  

### Q7 - Give that a = [12,26,330,41,50]. What is a[:-1]?

a) [50,41,330,26,12]  
b) Not possible.  
c) [12,26,330,41]  
d) 50 

### Q8 - What error occurs when you execute: apple = banana? 

a) No error. Apple is asigned the variable banana.  
b) ValueErrror  
c) SyntaxError  
d) NameError  
e) SyntaxError  

### Q9 - What data type is this object: a = [1,'hello',3.14,0,]

a) list  
b) array  
c) dictionary  
d) tuple  

### Q10 - Which pieaces of code will result in: _This code will work_ ?

a) "This code will",work  
b) "This code will"+"work"  
c) This code will work  
d) "This+code+will+work"  