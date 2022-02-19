'''
Referencia:
https://towardsdatascience.com/solving-mazes-with-python-f7a412f2493f

Inegrantes:
Mirka Monzon 18139
Daniela Villamar 19086

LABORATORIO 1 - GRAPH SEARCH

'''
import PIL
import cv2
import numpy as np
import matplotlib.pyplot as plt

#coordenadas de pixeles 
class Vertex:
    def __init__(self,x_coord,y_coord):
        self.x = x_coord
        self.y = y_coord
        self.d = float('inf')
        self.processed = False 

#return de vecinos en las 4 direcciones
def get_vecino(m,r,c):
    shape = m.shape
    vecino = []
    
    #verificacion de coordenadas vecinas dentro de la imagen 
    if r > 0 and not m[r-1][c].processed:
         vecino.append(m[r-1][c])
    if r < shape[0] - 1 and not m[r+1][c].processed:
            vecino.append(m[r+1][c])
    if c > 0 and not m[r][c-1].processed:
        vecino.append(m[r][c-1])
    if c < shape[1] - 1 and not m[r][c+1].processed:
            vecino.append(m[r][c+1])
    return vecino

def paso_arriba(queue, index):
    if index <= 0:
        return queue
    p_index=(index-1)//2
    if queue[index].d < queue[p_index].d:
            queue[index], queue[p_index]=queue[p_index], queue[index]
            queue[index].index_in_queue=index
            queue[p_index].index_in_queue=p_index
            quque = paso_arriba(queue, p_index)
    return queue
    
def paso_abajo(queue, index):
    length=len(queue)
    lc_index=2*index+1
    rc_index=lc_index+1
    if lc_index >= length:
        return queue
    if lc_index < length and rc_index >= length: 
        if queue[index].d > queue[lc_index].d:
            queue[index], queue[lc_index]=queue[lc_index], queue[index]
            queue[index].index_in_queue=index
            queue[lc_index].index_in_queue=lc_index
            queue = paso_abajo(queue, lc_index)
    else:
        small = lc_index
        if queue[lc_index].d > queue[rc_index].d:
            small = rc_index
        if queue[small].d < queue[index].d:
            queue[index],queue[small]=queue[small],queue[index]
            queue[index].index_in_queue=index
            queue[small].index_in_queue=small
            queue = paso_abajo(queue, small)
    return queue