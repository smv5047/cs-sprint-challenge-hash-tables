def get_indices_of_item_weights(weights, length, limit):
    # create dict
    weight_location = {}
    # search through weight list
    # create entries in weight location by using each weight as key,
    # and placement in list as value
    if length == 2:
        if weights[0]+weights[1] == limit:
            return (1, 0)

    for i in range(length):
        weight_location[weights[i]] = i

    for key in weight_location:
        weight_needed = limit-key
        if weight_needed in weight_location:
            print(weight_location[limit-key], weight_location[key])
            return((weight_location[limit-key], weight_location[key]))

    # determine two keys in dict (in order) that equal limit
    # take the values of those two keys and add their values to a tuple
    # return tuple

    return None


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
