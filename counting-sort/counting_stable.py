from itertools import accumulate

def stable_counting_sort(data, max_value, key: callable) -> None:
    """Sorts a mutable sequence in place using Stable Counting Sort."""
    count_array = [0] * (max_value + 1)
    output = [None] * len(data)

    # Count occurrences of each key value
    for item in data:
        count_array[key(item)] += 1

    # Update count_array to contain positions
    # for i in range(1, len(count_array)):
    #     count_array[i] += count_array[i - 1]
    count_array[:] = accumulate(count_array)
    
    # Build the output array in stable manner
    for item in reversed(data):
        count_index = key(item)
        count_array[count_index] -= 1
        output[count_array[count_index]] = item
        
    # Transfer sorted output back to data
    data[:] = output[:]

def main():
    from basic_employee import BasicEmployee
    from typing import MutableSequence
    
    def employee_key(employee: BasicEmployee) -> int:
        return employee.id
    
    employee_details = (
        ("John", "Doe", 345),
        ("Jane", "Smith", 123),
        ("Emily", "Jones", 234),
        ("Michael", "Brown", 456),
        ("Sarah", "Davis", 567),
        ("David", "Wilson", 678),
    )
    
    employee_list: MutableSequence[BasicEmployee] = [BasicEmployee(*detail) for detail in employee_details]
    print(f'{len(employee_list)} Employees before sorting:')
    
    max_value = max(emp.id for emp in employee_list)

    stable_counting_sort(employee_list, max_value, key=employee_key)
    for employee in employee_list:
        print(employee)