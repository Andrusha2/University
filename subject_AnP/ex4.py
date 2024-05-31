max_row = 0
current_row = 1
previous = 0
current = int(input())
while current != 0:
    if current == previous:
        current_row += 1
    else:
        if current_row > max_row:
            max_row = current_row
        current_row = 1
    previous = current
    current = int(input())

if current_row > max_row:
    max_row = current_row

print(max_row)

# O(n)