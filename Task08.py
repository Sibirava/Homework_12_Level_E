import Vector

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

    last = find_last_zero_element_vector(vector, value=0)
    vector1 = vector[last:]
    msg = f"The sum of elements after the last zero elements {last} in " \
          f"{vector} is {sum_elements(vector1)}"

    print(msg)
main()