'''
name: Cameron Ball
FSUID: cbb18
'''
import time, sys

def printer(func, *args):
    '''
    Handles all the printing and formatting for this assignment.
    '''
    print('''*************************************************
Calling function {name}.'''.format(name = func.__name__))

    if len(args) == 0:
        print("No arguments.")
    else:
        print("Arguments:")
        for arg in args:
            t = str(type(arg))
            formatted = str()
            for char in t[8:-2]:
                formatted += char
            print("    - " + str(arg) + " of type " + formatted + ".")
                
    print("Output:")
    start = time.time()
    o = func(*args)
    stop = time.time()
    print("Execution time: {:.5f} s.".format(stop - start))
    
    if o == None:
        print("No return value.")
    else:
        t = str(type(o))
        formatted = str()
        for char in t[8:-2]:
            formatted += char
        print("Return value: {val} of type {tp}.".format(val = o, tp = formatted))

    print("*************************************************\n")

def log(out = ''):               # second wrapper function for passing in file argument
    def decorate(func):
        def func_wrapper(*args):
            if out == '' or not isinstance(out, str): # if no file was provided, print to sys.stdout like normal
                printer(func, *args)
            else:                           # if a file is provided...
                try:                        # try to open it
                    f = open(out, "a")
                    ogOut = sys.stdout          # capture previous out stream
                    sys.stdout = f              # set current out stream to the file we opened
                    printer(func, *args)        # if no exception was raised by now, print to the file
                    sys.stdout = ogOut          # reset the output stream
                    f.close()                   # and close the file
                except FileNotFoundError:   # if an exception was raised,
                    printer(func, *args)    # print to sys.stdout like normal
        return func_wrapper
    return decorate

@log()
def factorial(*num_list):
    results = []
    for number in num_list :
        res = number
        for i in range(number-1,0,-1): 
            res = i * res
        results.append(res)
    return results

@log("logger.txt")
def waste_time(a,b,c):
    print("Wasting time.")
    time.sleep(5)
    return a, b, c

@log("logger.txt") 
def gcd(a, b):
    print("The GCD of", a, "and", b, "is ", end="") 
    while a!=b:
        if a > b: 
            a -= b
        else:
            b -= a
    print(abs(a))
    return abs(a)

@log()
def print_hello(): 
    print("Hello!")

@log(10)
def print_goodbye():
    print("Goodbye!")

if __name__ == "__main__":
    factorial(4, 5)
    waste_time("one", 2, "3")
    gcd(15 ,9)
    print_hello()
    print_goodbye()