import Vector

def find_first_positive_element_vector(vector):

    for i in range(len(vector)):
        if vector[i] > 0:
            return i

def sum_elements_after_first_positive(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)


def main():
    vector = Vector.random_float_vector_elements()

    first = find_first_positive_element_vector(vector)

    vector1 = vector[first + 1:]

    sum = sum_elements_after_first_positive(vector1)

    msg = (f"The sum of elements after first positive {first} in {vector}"
           f"is {sum}")
    print(msg)

main()
