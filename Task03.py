import Vector

def find_last_positive_element(vector):

    for index in range(len(vector) - 1, -1, -1):
        if vector[index] > 0:
            vector1 = vector[:index]
            return vector1

def count_elements_before_last_positive_element(vector1):
    sum = 0

    for element in vector1:
        sum += element
    return round(sum, 2)
       
def main():
    vector = Vector.random_float_vector_elements()
    vector1 = find_last_positive_element(vector)
    sum = count_elements_before_last_positive_element(vector1)
    msg = f"In {vector} the sum of elements before the last positive element is {sum} "
    print(msg)

main()