# Write a method in python to display the elements of list thrice if it is a number and display the element terminated with ‘#’ if it is not a number.
# For example, if the content of list is [‘41’,‘DHRUVA’,‘GURU’, ‘13’,‘ZARA’]
# The output should be
# 414141
# DHRUVA#
# GURU#
# 131313
# ZARA#

l = ['12','saravana','332','raja','221','wwe']
for i in l:
    if i.isnumeric():
        print(i * 3)
    else:
        print(i + "#")
