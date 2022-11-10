import Vector

def cut_vector(vector):
    vector1 = vector[1: len(vector) - 1]
    return vector1

def sum_elements(vector1):
    sum = 0
    for element in vector1:
        sum += element
    return sum

def main():
    vector = Vector.random_vector_elements()
    vector1 = cut_vector(vector)
    print(vector1)
    
    msg = f"Sum of elements between zero elements in {vector} is {sum_elements(vector1)}"
    print(msg)
main()