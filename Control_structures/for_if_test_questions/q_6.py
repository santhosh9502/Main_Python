# Get all the initials, sort them alphabetically, and put them in a space-separated string.
# Sample Input: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# Expected Output: 'E J M M N S U V'

l = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
l.sort()
for i in l:
    if i.title():
        print(i[0],end=" ")
