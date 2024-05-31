mxf = 0
mxs = 0
n = int(input())
while n != 0:
    if n > mxf:
        mxs, mxf = mxf, n
    elif n > mxs:
        mxs = n
    n = int(input())
print(mxs)

# O(n)