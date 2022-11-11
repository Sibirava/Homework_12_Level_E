import Vector

def get_max_value_index(vector):
    max_index = 0

    for index in range(0, len(vector) - 1):
        if vector[index] >= vector[max_index]:
            max_index = index
    return max_index


def get_min_value_index(vector):
    min_index = 0

    for index in range(0, len(vector) - 1):
        if vector[index] <= vector[min_index]:
            min_index = index
    return min_index

def cut_vector_between_max_min(vector,max_index, min_index):

    if min_index > max_index:
        vector1 = vector[max_index:min_index + 1]
    else:
        vector1 = vector[min_index::max_index + 1]
    return vector1

def mult_elements_vector1(vector1):
    mult = 1

    for element in vector1:
        mult *= element
    return round(mult, 2)

def main():
    vector = Vector.random_float_vector_elements()
    max_index = get_max_value_index(vector)
    min_index = get_min_value_index(vector)

    vector1 = cut_vector_between_max_min(vector,max_index, min_index)
    mult = mult_elements_vector1(vector1)

    msg = f"initial vector is {vector}\n " \
          f"index of max element {max_index}, index of min element is {min_index} \n" \
          f"after cut vector {vector1} and mult of elements in vector1 is {mult}."
    print(msg)

main()

