import Vector

def find_first_negative_element_vector(vector):

    for i in range(len(vector)):
        if vector[i] < 0:
            return i

def find_last_negative_element_vector(vector):

    for i in range(len(vector) - 1, -1, -1):
        if vector[i] < 0:
            return i

def sum_between_first_last_negative_elements(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)

def main():
    vector = Vector.random_float_vector_elements()

    first = find_first_negative_element_vector(vector)

    last = find_last_negative_element_vector(vector)

    vector1 = vector[first + 1:last]

    sum = sum_between_first_last_negative_elements(vector1)

    msg = (f"The sum between first negative element with index {first} and last "
           f"negative element {last} \n in {vector} is {sum}")
    print(msg)

main()