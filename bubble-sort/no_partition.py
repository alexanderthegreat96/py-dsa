# bubble sort
# compares values inside the array
# and if the values on the left are bigger than the ones
# on the right, they get swapped

# this is a simpler, more optimized variant
numbers = [89, 122, 33, -15, 12, 5, 34]

print(f"before: {numbers}")

total_numbers = len(numbers)
for i in range(total_numbers):
    swapped: bool = False
    for j in range(total_numbers - 1):
        # print(f'Comparing: {numbers[j]} with {numbers[j+1]}')
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    if not swapped:
        break


print(f"after: {numbers}")
