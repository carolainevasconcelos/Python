def fizzbuzz(x):
    if x % 3 == 0 and not x % 5 == 0:
        return ("Fizz")
    elif x % 5 == 0 and not x % 3 == 0:
        return ("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        return ("FizzBuzz")
    else:
        return (x)
    
print(fizzbuzz(3))
print(fizzbuzz(5))    
print(fizzbuzz(15))   
print(fizzbuzz(4))         