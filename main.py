
from lib import *
import sys 

"""dicc = {
    0: "meew",
    'nom': "Evelyn",
    'edad':35,
    'tel':{
        'cel':5,
        'fij':6
    }
}
print(dicc ['nom'])
print(dicc ['edad'])
print(dicc [0])
print(dicc)
print(dicc ['tel']['cel'])"""

diccRel = {}

#ES LO MISMO SOLO Q POR SEPARADO 
"""diccRel ['A'] = {'B':5, 'C':3}
diccRel ['B'] = {'A':5, 'C':2, 'D':4}
diccRel ['C'] = {'A':3, 'B':2, 'D':6, 'E':7}
diccRel ['D'] = {'B':4, 'C':6, 'E':8}
diccRel ['E'] = {'C':7, 'D':8}  """
grafoTest = grafo()
grafoTest.addArista('A', 'B', 5)
grafoTest.addArista('A', 'C', 3)

grafoTest.addArista('B', 'A', 5)
grafoTest.addArista('B', 'C', 2)
grafoTest.addArista('B', 'D', 4)

grafoTest.addArista('C', 'A', 3)
grafoTest.addArista('C', 'B', 2)
grafoTest.addArista('C', 'D', 6)
grafoTest.addArista('C', 'E', 7)

grafoTest.addArista('D', 'B', 4)
grafoTest.addArista('D', 'C', 6)
grafoTest.addArista('D', 'E', 8)

grafoTest.addArista('E', 'C', 7)
grafoTest.addArista('E', 'D', 8)

origenG = 'A'
destinoG = 'E'
path = {}
visitados = []
path[origenG]= {'-':0}
llaves = grafoTest.aristas[origenG].keys()
print(llaves)

for i in llaves:
    path[i]={origenG: grafoTest.aristas[origenG][i]}
    
print("primer iter:")   
print(visitados)
print(path)

verticeAct = 'B'
visitados.append(verticeAct)
llaves = grafoTest.aristas[verticeAct].keys()
print(llaves)
for i in llaves:
    if i not in visitados:
        if i not in path: path[i] = {}
        llave = list(path[verticeAct].keys())
        acumulado = path[verticeAct][llave[0]]
        path[i].update({verticeAct: grafoTest.aristas[verticeAct][i]+ acumulado})
        # reviso si hay más de dos llaves en una llave del path
        if len(path[i])== 2:
            kiss = list(path[i].keys())
            if kiss [0] < kiss[1]:
                del(path[i][kiss [1]])
            pass
    # fin if not in visitados
# fin for i
   
        
print(path)
exit()