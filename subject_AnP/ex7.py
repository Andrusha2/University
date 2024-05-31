a = list(map(int, input().split()))
mx = a[0]
counter = 1
for i in range(1, len(a)):
    if a[i] > mx:
        if a[i] - a[i - 1] == 1:
            counter += 1
        mx = a[i]

print(counter)

# O(n)