#!usr/bin/env python

"""
file descriptor

"""

__author__ = "Tadhg O'Rourke"
__date__ = "30/08/2019"


def factorial(n):
    """Calculates n! recursively"""

    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n - 1)


# will attempt to run code in try clause
try:
    print(factorial(30))
    print(factorial(999))

# if a recursion error is raised while attempting to run try clause, it will stop and run the exception clause
# except (RecursionError, ZeroDivisionError):
#     print("Factorial too large or cannot divide by zero")

except RecursionError:
    print("Factorial too large")

except ZeroDivisionError:
    print("Cannot divide by zero")

# will execute if try clause is executed without any problems - must be after exception clauses
else:
    print("all actions preformed successfully")

# will always execute - must be final statement
finally:
    print("Always executes")
