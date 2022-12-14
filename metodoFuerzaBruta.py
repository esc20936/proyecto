import itertools as it

def checkIfAllTrue(lista):
    for i in lista:
        if i == False:
            return False
    return True


def fuerzaBruta(operacion):
    variables = []
    for conjuncion in operacion:
        for disyuncion in conjuncion:
            if disyuncion[0] not in variables:
                variables.append(disyuncion[0])
    lista = []
    for seq in it.product([True,False], repeat=len(variables)):
        a = set(zip(variables, seq))   
        for disyuncion in operacion:
            lista.append(bool(disyuncion.intersection(a)))
        if checkIfAllTrue(lista):
            return True, a
        lista = []
    
    return False, None