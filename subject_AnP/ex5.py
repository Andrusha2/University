local_max = 0
current_distance = 1
min_distance = 123
n = int(input())
while n != 0:
    n = int(input())
    if n == local_max:
        if min_distance > current_distance:
            min_distance = current_distance
        current_distance = 1
    if n > local_max:
        local_max = n
        current_distance = 1
        min_distance = 123
    if n < local_max:
        current_distance += 1

if min_distance == 123:
    min_distance = 0

print(min_distance)

# O(n)