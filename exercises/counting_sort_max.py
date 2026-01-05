from itertools import accumulate
from typing import MutableSequence


def stable_counting_sort(data: MutableSequence, max_value: int, key: callable = None) -> None:
    """Stable counting sort to sort a list in place.

    :param data: The list to sort.
    :param max_value: The maximum value in the list.
    :param key: A function that will be applied to each item, to get the value to sort on.
    :return: None, the data list is modified to contain its items in sorted order.
    """

    count_array: list[int] = [0] * (max_value + 1) 
    output: list = [0] * len(data)

    for item in data:
        if key:
            count_index = key(item)
        else:
            count_index = item
        count_array[count_index] += 1

    # Calculate a prefix sum over count_array
    count_array[:] = accumulate(count_array)

    for item in reversed(data):
        if key:
            count_index = key(item)
        else:
            count_index = item
        count_array[count_index] -= 1
        output[count_array[count_index]] = item

    # Transfer the sorted values back into the original list.
    for index, item in enumerate(output):
        data[index] = item


def main():
    from basic_employee import BasicEmployee

    def employee_key(emp: BasicEmployee) -> int:
        return emp.id

    employee_details = (           # Employees arranged by last name then first name.
        ('Mary', 'Amis', 4725),
        ('Mike', 'Blogs', 4586),
        ('John', 'Charles', 1330),
        ('John', 'Doe', 8792),
        ('Jane', 'Evans', 4586),
        ('Adele', 'Freeman', 5729),
    )

    # Build the list that we're going to sort.
    employee_list = []
    for detail in employee_details:
        employee_list.append(BasicEmployee(*detail))

    print(f'{len(employee_list)=}')

    max_value = max(emp.id for emp in employee_list)
    print(f'{max_value - min(emp.id for emp in employee_list)}')

    stable_counting_sort(employee_list, max_value, key=employee_key)
    for employee in employee_list:
        print(employee)


if __name__ == '__main__':
    main()
