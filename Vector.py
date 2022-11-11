import random
NUMBER = 10
RANDOM_VALUE_DOWN = -10
RANDOM_VALUE_UP = 10

NUMBER_VECTOR_ELEMENTS = 10
def random_vector_elements():
    n = NUMBER
    vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(n)]
    return vector

def input_vector_element(NUMBER_VECTOR_ELEMENTS):

    vector = [int(input("Input element of list:")) for i in range(NUMBER_VECTOR_ELEMENTS)]
    return vector

def input_float_vector_element(NUMBER_VECTOR_ELEMENTS):

    vector = [float(input("Input element of list:")) for i in range(NUMBER_VECTOR_ELEMENTS)]
    return vector
