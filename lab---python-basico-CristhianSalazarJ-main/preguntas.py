"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    

    Rta/
    214

    """

    data = open("data.csv", "r").readlines()

    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]
    col2 = [int(col[1]) for col in data]

    return sum(col2)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    from collections import Counter
    from operator import itemgetter

    data = open("data.csv", "r").readlines()

    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    col1 = [fila[0] for fila in data]
    cnt_col1 = Counter(col1)
    tuplas = cnt_col1.items()
    tuplas = list(tuplas)
    tuplas.sort(key=itemgetter(0))

    return tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_2 = [(fila[0], int(fila[1])) for fila in data]
    d = defaultdict(int)

    for k,v in cols1_2:
        d[k] += v

    return sorted(d.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    from operator import itemgetter

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    col3_fechas = [fila[2] for fila in data]
    col3_fechas = [fecha.split("-") for fecha in col3_fechas]

    meses = [x[1] for x in col3_fechas]
    cnt_meses = Counter(meses)

    tuplas_meses = list(cnt_meses.items())
    tuplas_meses.sort(key=itemgetter(0))

    return tuplas_meses


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_2 = [(fila[0], int(fila[1])) for fila in data]

    d2 = defaultdict(list)

    for k,v in cols1_2:
        d2[k].append(v)

    list_tuplas = sorted(d2.items())
    
    res = [(tp[0], max(tp[1]), min(tp[1])) for tp in list_tuplas]

    return res


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    col5 = [fila[4].split(",") for fila in data]
    col5_split = [e.split(":") for fila in col5 for e in fila]

    d3 = defaultdict(list)

    for k,v in col5_split:
        d3[k].append(int(v))

    lista_tuplas2 = sorted(d3.items())

    res = [(tp[0], min(tp[1]), max(tp[1])) for tp in lista_tuplas2]

    return res


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_2 = [(fila[0], int(fila[1])) for fila in data]
    d4 = defaultdict(list)

    for v,k in cols1_2:
        d4[int(k)].append(v)

    res = sorted(d4.items())

    return res


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_2 = [(fila[0], int(fila[1])) for fila in data]
    d4 = defaultdict(list)

    for v,k in cols1_2:
        d4[int(k)].append(v)

    tuplas = sorted(d4.items())
    lista_unicos = [(tp[0], sorted(list(set(tp[1])))) for tp in tuplas]

    return lista_unicos


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from collections import Counter
    from operator import itemgetter
    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    col5 = [fila[4].split(",") for fila in data]
    col5_split = [e.split(":") for fila in col5 for e in fila]

    reg = [fila[0] for fila in col5_split]

    cnt_reg = Counter(reg)
    tuplas = list(cnt_reg.items())
    tuplas.sort(key=itemgetter(0))
    
    return dict(tuplas)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_4_5 = [(fila[0], fila[3], fila[4]) for fila in data]
    tuplas2 = [(tp[0], len(tp[1].split(",")), len(tp[2].split(","))) for tp in cols1_4_5]
    return tuplas2


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    
    from collections import defaultdict

    data = open("data.csv", "r").readlines()
    data = [fila.replace("\n","") for fila in data]
    data = [fila.replace("\t"," ") for fila in data]
    data = [fila.split(" ") for fila in data]

    cols1_5 = [(fila[0], fila[4].split(",")) for fila in data]
    col_1_5_tuples = [(letra, int(reg.split(":")[1])) for letra,lista in cols1_5 for reg in lista]

    d4 = defaultdict(int)

    for k,v in col_1_5_tuples:
        d4[k] += v

    lista_tuplas3 = sorted(d4.items())

    return dict(lista_tuplas3)
