lst = [1, 2, 3, 4, 2, 5, 3]

duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate elements:", duplicates)