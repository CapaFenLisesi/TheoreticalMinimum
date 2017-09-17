
# LAFFer Curves: vector.py
#     Vectors, and their common operations

# By: Alexander Ahmann (https://gaussian.horse)

class Vector:

    def __init__(self, *elements):
        elements = list(elements)
        for n, k in enumerate(elements):
            if type(k) is not int and type(k) is not float:
                raise Exception('All elements in vector must be int or float')

        self.__vector = elements

    def __call__(self):
        return self.__vector

def isVector(x): # needs peer review
    if type(x) is not list:
        return False
    else:
        for n, k in enumerate(x):
            if type(k) is not int and type(k) is not float:
                return False
    return True

def isLengthEqual(*vectors): # needs further testing / peer review
    base_length = len(vectors[0])
    for n, k in enumerate(vectors):
        if not isVector(k):
            raise Exception("one of the parameters does not meet the criteria for a vector")
        else:
            if len(k) is not base_length:
                return False
    return True

def scaleVector(param, vector): # needs further testing / peer review
    if not isVector(vector) or type(param) is not int:
        raise Exception("either the 'param', 'vector', or both is/are invalid")
    for n, k in enumerate(vector):
        vector[n] *= param
    return vector

def dotProduct(v_1, v_2): #needs testing / peer review
    if not isVector(v_1) or not isVector(v_2) or not isLengthEqual(v_1, v_2):
        raise Exception("either one of the vectors does not meet the criteria " \
                        "for a vector, or the vectors lengths are not equal")
    result = [x * y for x, y in zip(v_1, v_2)]
    return result

def vectorLength(v): # needs testing / peer review
    return dotProduct(v, v)**0.5