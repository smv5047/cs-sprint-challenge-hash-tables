def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create dict
    num_lookup = {}
    # create resulting list
    result = []
    # add all numbers to hash table
    for num in a:
        num_lookup[num] = num
    # search for negative numbers
    # determine if their absolute value is within hash table
    for num in a:
        if num < 0:
            # if absolute valiue is in the hash table add to results
            if abs(num) in num_lookup:
                result.append(abs(num))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
