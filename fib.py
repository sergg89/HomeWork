# CASE 1 - using recursion
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def create_fib_list(n):
    result = []
    for i in range(1, n+1):
        result.append(fib(i))
    return result

print(create_fib_list(10))

# CASE 2 - without recursion

def create_fib_list_without_recursion(n = 2):
    fib_list = [1, 1]
    i = 2
    while i < n:
        fib_list.append(fib_list[i - 2] + fib_list[i - 1])
        i += 1
    print(fib_list)

create_fib_list_without_recursion(10)
