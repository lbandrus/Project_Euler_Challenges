"""Objective: Find the sum of all the multiples of 3 or 5 below 1000"""

def main(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == "__main__":
   print(main(1000))