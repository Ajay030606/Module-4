# Module-4

**Task1**

Function Definition – func(x)
if x < 0:
Factorial is not defined for negative numbers.
So it returns the message: "not defined for negative numbers".

elif (x == 0):
Base case of recursion.
By definition: 0! = 1.

else:
Recursive case:

𝑛!=𝑛×(𝑛−1)!

n!=n×(n−1)!

So the function calls itself with a smaller number (x-1) until it reaches the base case.

x = int(input("Enter a number: "))
Asks the user to enter a number.
Converts it to an integer and stores it in x.

print("Factorial of", x, "is", func(x))
Calls the function func(x) with user’s input.
Prints the factorial result.

**Task2**

import math

You import Python’s math module, which contains many mathematical functions (square root, log, trigonometry, etc.).

num = float(input("Enter a number: "))

Asks the user to type a number.

input() takes it as a string.

float(...) converts it into a decimal number (so you can enter numbers like 5.5 as well).

Stores it in variable num.

square_root = math.sqrt(num)

Calculates the square root of num.
Example: if num = 9, result = 3.0.

log_value = math.log(num)

Calculates the natural logarithm (base e ≈ 2.718) of num.

Example: if num = 10, result ≈ 2.302585.

sine_value = math.sin(num)

Calculates the sine of num.

num is taken in radians, not degrees.

Example: if num = 3.14 (≈ π), result ≈ 0.0.
