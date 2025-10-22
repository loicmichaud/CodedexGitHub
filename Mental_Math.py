numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even_numbers = []
odd_numbers = []

for items in numbers :
    if items % 2 ==0:
        even_numbers.append(items)
    else :
        odd_numbers.append(items)

print(even_numbers)
print(odd_numbers)