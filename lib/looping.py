#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i-=1
    print('Happy New Year!')
        

print(happy_new_year())
    
   

def square_integers(int_list):
    result=list()
    for int in int_list:
        square=int*int
        result.append(square)
        
    return result

print(square_integers([1,2,3, 4,5]))
print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

def fizzbuzz():
    for i in range (1, 101):
        if (i%3==0 and i%5==0):
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        
        else:
            print(i)
print(fizzbuzz())
