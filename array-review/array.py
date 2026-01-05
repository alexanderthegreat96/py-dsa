from array import array

# methods like: insert, append and extend for arrays
int_array = array("l", [0] * 7)


int_array[0] = 20
int_array[1] = 35
int_array[2] = -15
int_array[3] = 7


print(int_array)

print("-" * 80)

for index in range(len(int_array)):
    print(int_array[index])

print()
print(int_array.itemsize)

# arrays are stored in a single block in memory
# lists are the same
