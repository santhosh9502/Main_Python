"""Write a program to numbers divisible by 7 and multiple of 5, between 1 and 100."""
def div_mul():
    numbers = []
    for i in range(1,101):
        if i % 7 == 0 and i % 5 == 0:
            numbers.append(i)
    return numbers

res = div_mul()
print(res)
