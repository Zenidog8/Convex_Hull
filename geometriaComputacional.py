from random import randint

def generarPuntos(cantidad):
    '''
    Genera n puntos en un plano cartesiano
    '''
    matriz = []
    if(cantidad > 0 and cantidad < 101):
        for i in range(0, cantidad):
            tmp = []
            x = randint(1, 80)
            y = randint(1, 80)
            tmp.append(x)
            tmp.append(y)
            matriz.append(tmp)

    return matriz


def producto_cruz(a, b):
    '''
    Calcula del producto cruz entre dos puntos
    '''
    return (a[0] * b[1]) - (b[0] * a[1])


def rp(a, b):
    '''
    Resta dos puntos
    '''
    tmp = []
    x = a[0] - b[0]
    y = a[1] - b[1]
    tmp.append(x)
    tmp.append(y)
    return tmp


def cmpAmayorB(a, b):
    '''
    Genera un criterio para comparar elementos
    '''
    if a[0] > b[0]:
        return True

    if a[0] < b[0]:
        return False

    else:
        if a[1] >= b[1]:
            return True
        elif a[1] < b[1]:
            return False


def ordenarPuntos(puntos):
    '''
    Ordenamiento basico para ordenar los puntos
    '''
    for i in range(len(puntos)):
            for j in range(len(puntos)-1):
                    if cmpAmayorB(puntos[j], puntos[j+1]):
                            tmp = puntos[j]
                            puntos[j] = puntos[j+1]
                            puntos[j+1] = tmp

    return puntos


def convexhull(puntos):
    '''
    Selecciona los puntos mas externos de manera que se pueda generar un
    poligono con estos y que los demas puntos existentes queden contenidos
    '''
    idx_u = 0
    idx_l = 0
    mayores = []
    menores = []
    largo = len(puntos)

    for j in range(largo):
        mayores += [[0,0]]
        menores += [[0,0]]

    puntos = ordenarPuntos(puntos)

    i = 0
    while i < largo:
        while (idx_u > 1) and (producto_cruz(rp(puntos[i], mayores[idx_u - 2]), rp(mayores[idx_u - 1], mayores[idx_u - 2])) <= 0):
            idx_u -= 1

        mayores[idx_u] = puntos[i]
        idx_u += 1
        i += 1

    e = largo - 1
    while e > -1:
        while (idx_l > 1) and (producto_cruz(rp(puntos[e], menores[idx_l - 2]), rp(menores[idx_l - 1], menores[idx_l - 2])) <= 0):
            idx_l -= 1

        menores[idx_l] = puntos[e]
        idx_l += 1
        e -= 1

    idx_u -= 1
    idx_l -= 1

    nuevoLargo = idx_u + idx_l
    idx_l = 0
    while idx_u < nuevoLargo:
        mayores[idx_u] = menores [idx_l]
        idx_u += 1
        idx_l += 1

    res = []

    k = 0
    while(k < len(mayores)):
        if (mayores[k][0] != 0 and mayores[k][1] != 0):
            if mayores.count(mayores[k]) == 1 and mayores[k] not in res:
                res.append(mayores[k])
        k += 1

    return res


def calcularArea(puntos):
    '''
    Calcula el area del poligono usando el producto cruz de los puntos
    '''
    area = 0
    a = 0
    b = 1
    while(b < len(puntos)):
        area += producto_cruz(puntos[a], puntos[b])
        a += 1
        b += 1

    area += producto_cruz(puntos[len(puntos) - 1], puntos[0])
    area = area / 2

    if area < 0:
        area = area * -1

    return area
