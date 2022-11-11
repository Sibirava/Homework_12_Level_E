import Vector

def find_module_elements(vector):

    module_list = []

    for element in vector:
        if element < 0:
            module = element * (-1)
        elif element == 0:
            module = 0
        else:
            module = element
        module_list.append(module)
    return module_list

def find_max_module_element_index(vector1):
    max_module_index = 0

    for index in range(len(vector1)):
        if vector1[index] >= vector1[max_module_index]:
            max_module_index = index
    return max_module_index


def mult_elements_after_max_module(vector):
    mult = 1

    for element in vector:
        mult *= element
    return mult


def main():
    vector = Vector.input_float_vector_element(NUMBER_VECTOR_ELEMENTS=5)

    vector1 = find_module_elements(vector)

    max_module = find_max_module_element_index(vector1)

    vector2 = vector1[max_module + 1:]

    msg = (f" The mult after max module element {max_module} in {vector} "
           f"is {mult_elements_after_max_module(vector2)}\n")
    print(msg)

main()
