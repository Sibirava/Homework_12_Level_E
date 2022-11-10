import Vector

def check_value_in_vector(vector, value):
    count = 0

    for element in vector:
        if element == value:
            count += 1
            if count >= 2:
                return True
        return False

def find_first_zero_element_vector(vector, value):

    for i in range(len(vector)):
        if vector[i] == value:
            return i

def find_last_zero_element_vector(vector, value):

    for i in range(len(vector) - 1, -1, -1):
        if vector[i] == value:
            return i

def sum_elements(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return sum

def main():
    vector = Vector.random_vector_elements()

    first = find_first_zero_element_vector(vector, value=0)
    last = find_last_zero_element_vector(vector, value=0)

    vector1 = vector[first:last]

    sum = sum_elements(vector1)

    msg = f"Sum of elements between {first} and {last} zero elements in {vector} is {sum}"

    print(msg)


main()