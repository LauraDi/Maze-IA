
#Archivo de prueba

import maze
import pytest

@pytest.mark.parametrize('file, coordenadaB', [('maze1.txt',(1, 5)), ('maze2.txt',(8, 13)), ('maze3.txt',(2, 1)), ('maze4.txt',(0, 5)), ('maze5.txt',(1, 9))])
# file es el txt de maze
#coordenadaB es la coordenada exacta de la B puesta a mano por mi para testear que al final se llega a esa
def test_algoritmo(file, coordenadaB):
    m = maze.Maze(file)
    m.solve
    assert m.goal == coordenadaB




# @pytest.mark.parametrize('file, coordenadaB', [('maze1.txt',(1, 5)), ('maze2.txt',(8, 13)), ('maze3.txt',(2, 1)), ('maze4.txt',(0, 5)), ('maze5.txt',(1, 9))])
# def test_prueba(file, coordenadaB):
#     m = maze.Maze(file)
#     m.solve
#     assert m.goal == coordenadaB