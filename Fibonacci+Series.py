# Python Fibonacci series Program using Recursion

# Recursive Function Beginning
def Fibonacci_series(Number):
           if(Number == 0):
                      return 0
           elif(Number == 1):
                      return 1
           else:
                      return (Fibonacci_series(Number - 2)+ Fibonacci_series(Number - 1))

# End of the Function

# Fibonacci series will start at 0 and travel upto below number
Number = int(input("\nPlease Enter the Range Number: "))

# Find & Displaying Fibonacci series
for Num in range(0, Number):
           print(Fibonacci_series(Num))