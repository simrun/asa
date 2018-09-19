# Prints the Fibonacci sequence, in which every element is the sum of the previous two

first = 1
second = 1

print(first)
print(second)

for _ in range(10):
    x = first + second
    tmp = second
    second = x
    first = tmp
    print(x)