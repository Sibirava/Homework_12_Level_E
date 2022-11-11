import Vector

def find_first_zero_element_vector(vector, value):

    for i in range(len(vector)):
        if vector[i] == value:
            return i

def find_second_zero_element_vector(vector, value):
    count = 0

    for i in range(len(vector)):
        if vector[i] == value:
            count += 1
            if count == 2:
                return i

def mult_elements_between_first_second(vector1):
    mult = 1

    for element in vector1:
        mult *= element
    return mult

def main():
    vector = Vector.random_vector_elements()

    first = find_first_zero_element_vector(vector, value=0)

    second = find_second_zero_element_vector(vector, value=0)

    vector1 = vector[first + 1:second]

    mult = mult_elements_between_first_second(vector1)

    msg = (f"The mult between first {first} and second {second} zeros in {vector}"
           f"is {mult}")
    print(msg)

main()
