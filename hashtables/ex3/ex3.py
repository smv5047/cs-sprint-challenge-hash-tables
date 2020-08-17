def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create dictionary
    intersect_dict = {}
    combined_array = []
    for array in arrays:
        combined_array = combined_array+array
    # determine how many lists are being compare
    array_volume = len(arrays)
    # enter #s into dictionary for each list

    for num in combined_array:
        # print(num)
        if num in intersect_dict:
            # if number exists add +1 to value
            intersect_dict[num] += 1
        else:
            intersect_dict[num] = 1

    # take all the keys where the value is equal to the volume of lists and add to a list
    result = [k for k, v in intersect_dict.items() if v == array_volume]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

array1 = [1, 2, 3, 66, 45, 8]
array2 = [1, 4, 5, 8]
array3 = [1, 6, 7, 8, 9, 10, 11, 12]

combined_array = [array1, array2, array3]
intersection([
    [1, 2, 3],
    [1, 4, 5],
    [1, 6, 7]]
)
