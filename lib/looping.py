#!/usr/bin/env python3


    

# def square_integers(int_list):
#     # code goes here!
    



# while loop 
def happy_new_year():
    i = 10 
    while i > 0 :
        print(i)
        i -= 1 
    print("Happy New Year!")

happy_new_year()   

# for loop 
def happy_new_year_forloop():
    for i in range(10,0,-1):
        print(i)
    print("Happy New Year!")

happy_new_year_forloop() 

def square_integers(numbers):
    # squared = [ ]
     return [num * num for num in numbers]
    # for num in numbers :
    #     result = num * num 
    #     squared.append(result)
    #     print(result)
    # print(squared)

new_array = square_integers([1,2,3,4,5])
print(new_array)

def fizzbuzz():
    for i in range (1,101):
        if i % 15 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
    #  elif i % 5 == 0 and i % 3 == 0:
    #     print("FizzBuzz")
        
        else:
          print(i) 

fizzbuzz()

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    filtered_birds = [bird for bird in birds if bird not in geese]

    return filtered_birds    
