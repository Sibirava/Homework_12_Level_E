import Vector

def get_min_value_index(vector):
    min_index = 0

    for index in range(0, len(vector) - 1):
        if vector[index] <= vector[min_index]:
            min_index = index
    return min_index

def sum_elements(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)

def main():
    vector = Vector.random_float_vector_elements()
    min = get_min_value_index(vector)

    vector1 = vector[:min]

    msg = f"The sum of elements before min element with index {min} in \n" \
          f"{vector} \n" \
          f" is {sum_elements(vector1)}"

    print(msg)
main()