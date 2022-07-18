""" 
    Objective: By considering the terms in the Fibonacci sequence whose values 
    do not exceed four million, find the sum of the even-valued terms.
"""
def main(max_number):
    sum = 0
    first_fib = 1
    second_fib = 1
    while second_fib < max_number:
        if second_fib % 2 == 0:
            sum += second_fib
        first_fib, second_fib = second_fib, first_fib + second_fib
    return(sum)

if __name__ == "__main__":
    print(main(4000000))
