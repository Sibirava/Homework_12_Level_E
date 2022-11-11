import Vector

def find_first_negative_element_vector(vector):

    for i in range(len(vector)):
        if vector[i] < 0:
            return i

def find_second_negative_element_vector(vector):
    count = 0

    for i in range(len(vector)):
        if vector[i] < 0:
            count += 1
            if count == 2:
                return i

def sum_between_first_second_negative_elements(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)

def main():
    vector = Vector.random_float_vector_elements()

    first = find_first_negative_element_vector(vector)

    second = find_second_negative_element_vector(vector)

    vector1 = vector[first + 1:second]

    sum = sum_between_first_second_negative_elements(vector1)

    msg = (f"The sum between first negative element with index {first} and second "
           f"negative element {second} \n in {vector} is {sum}")
    print(msg)

main()