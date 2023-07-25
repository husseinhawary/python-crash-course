def get_duplicated_elements_in_array(numbers):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[j])


get_duplicated_elements_in_array([1, 2, 1, 2, 3, 4, 5, 6, 5])


def get_unique_elements_in_array(numbers):
    unique_numbers = []
    for number in numbers:
        if number in unique_numbers:
            continue
        else:
            unique_numbers.append(number)
    return unique_numbers


print(get_unique_elements_in_array([1, 2, 1, 2, 3, 4, 5, 6, 5]))
