""" 1.
Write a program to count the occurrences of each word in the text given below.
	Through three cheese trees three free fleas flew.
	While these fleas flew, freezy breeze blew.
	Freezy breeze made these three trees freeze.
	Freezy trees made these trees' cheese freeze.
	That's what made these three free fleas sneeze.
"""
counter = """Through three cheese trees three free fleas flew.
	While these fleas flew, freezy breeze blew.
	Freezy breeze made these three trees freeze.
	Freezy trees made these trees' cheese freeze.
	That's what made these three free fleas sneeze."""

result = {}
res = counter.title().split()
for sent in res:
    if sent not in result:
        result[sent] = 1
    else:
        result[sent] += 1

print(result)
