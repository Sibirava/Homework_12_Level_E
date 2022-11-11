import Vector

def get_max_value_index(vector):
    max_index = 0

    for index in range(0, len(vector) - 1):
        if vector[index] >= vector[max_index]:
            max_index = index
    return max_index

def sum_elements(vector1):
    sum = 0

    for element in vector1:
        if element > 0:
            sum += element
    return round(sum, 2)

def main():
    vector = Vector.random_float_vector_elements()

    max = get_max_value_index(vector)
    vector1 = vector[:max + 1]
    print(vector1)
    msg = f"The sum of elements before the max element with index {max} in " \
          f"{vector} is {sum_elements(vector1)}"

    print(msg)
main()