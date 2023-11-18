def nextMultiple(n: int, m: int) -> int:
    # Calculate the remainder when n is divided by m
    remainder = n % m
    
    # If remainder is zero, n is already divisible by m, so return n
    if remainder == 0:
        return n
    
    # Calculate the next multiple of m greater than n
    next_multiple = n + (m - remainder)
    
    return next_multiple

# Example usage:
n = 17
m = 5
result = nextMultiple(n, m)

print(result)



# ninja has two numbers n and m your task to return closest number to n which is greater than n and divisable by m in python def nextMultiple(n: int, m: int) -> int:
#     # Write your code here.
#     pass
