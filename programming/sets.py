# sets unordered collection no duplicates elements no indexing

A = {2, 6, 8, 9}
print(len(A))
A.add(10)
print(A)
A.update([15, 18, 19, 16])
print(A)
A.remove(18)
print(A)
A.discard(15)
print(A)


A.pop()# remove random element
print(A)
A.clear()
print(A)
z = set([1,2,3,4])
print(z)
B = {9,60,30}
print(A|B)
print(A.union(B))
print(A&B)
print(A.intersection(B))
print(A - B)
print(B - A)
print(B.difference(A))
print (A^B)





