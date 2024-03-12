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

diccRel = {
    'A':{'B':5, 'C':3},
    'B':{'A':5, 'C':2, 'D':4},
    'C':{'A':3, 'B':2, 'D':6, 'E':7},
    'D':{'B':4, 'C':6, 'E':8},
    'E':{'C':7, 'D':8} 
    
}
#ES LO MISMO SOLO Q POR SEPARADO 
diccRel ['A'] = {'B':5, 'C':3}
diccRel ['B'] = {'A':5, 'C':2, 'D':4}
diccRel ['C'] = {'A':3, 'B':2, 'D':6, 'E':7}
diccRel ['D'] = {'B':4, 'C':6, 'E':8}
diccRel ['E'] = {'C':7, 'D':8}    

printDicc(diccRel)
vericaA=vertice('A')