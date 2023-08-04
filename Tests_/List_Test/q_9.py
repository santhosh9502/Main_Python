# Given this nested list, use indexing to grab the word "hello"
# [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

l = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(l[3][1][2])
