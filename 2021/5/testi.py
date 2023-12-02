import itertools

l = [1,2,2,3]
y = [1]
aa = list(itertools.zip_longest(l,y))
print(list(aa))
