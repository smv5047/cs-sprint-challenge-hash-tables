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
    # print(intersect_dict)
    result = []
    print(array_volume)

    # results = [values == array_volume for values in intersect_dict.values()]
    for values == array_volume in intersect_dict.values():
        result.append(intersect_dict)

    print(results)
    # squares = [x**2 for x in range(10)]
    # determine which keys have a value that matches the volume of lists
    # return list of those values

    # for num in arrays[0]:

    # return result


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))

array1 = [1, 2, 3, 4, 5]
array2 = [12, 7, 2, 9, 1]
array3 = [99, 2, 7, 1]

combined_array = [array1, array2, array3]
intersection(combined_array)
