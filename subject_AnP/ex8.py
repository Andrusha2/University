a = int(input())
numbers = input().split()
spis = []
was_in = []
for i in numbers:
    if i in was_in:
        pass
    elif i in spis:
        was_in.append(i)
        spis.remove(i)
    else:
        spis.append(i)

print(*spis)

# O(n)