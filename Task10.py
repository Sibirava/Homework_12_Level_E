import Vector

def find_last_positive_element(vector):

    for i in range(len(vector) - 1, -1, -1):
        if vector[i] > 0:
            return i

def find_first_positive_element(vector):

    for i in range(len(vector)):
        if vector[i] > 0:
            return i

def sum_elements(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)

def main():
    vector = Vector.random_float_vector_elements()
    first = find_first_positive_element(vector)
    last = find_last_positive_element(vector)
    vector1 = vector[first + 1:last]

    msg = f"The sum of elements between first positive element with index {first} \n" \
          f"and last zero elements with index {last} in \n" \
          f"{vector} \n" \
          f" is {sum_elements(vector1)}"

    print(msg)
main()