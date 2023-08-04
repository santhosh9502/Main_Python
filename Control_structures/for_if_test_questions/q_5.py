# Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT
str = "SHIFT"

for i in range(len(str)):
    shift = str[i:] + str[:i]
    print(shift)
print(str)