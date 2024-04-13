import pygame
from maze import SearchSpace
from algos import DFS, BFS, UCS, AStar, Greedy, BFSWithStations, Moving
from const import GREY
from model_matrix import Matrix
import argparse
import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 

def main(algo:str, inputFile: str = 'input.txt'):
    pygame.init()

    #initialize map 
    myMatrix = Matrix()
    myMatrix.parseFile(script_directory + "\\input_files\\"+ inputFile)

    your_caption = f'Space: {myMatrix.height + 1} x {myMatrix.width + 1}'
    
    pygame.display.set_caption(f'{your_caption} - {algo}')

    RES = (1350, 700) # size of the window

    sc = pygame.display.set_mode(RES)
    #print(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(GREY))

    g = SearchSpace(myMatrix)

    g.draw(sc)
    clock.tick(20)

    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    elif algo == 'UCS':
        UCS(g, sc)
    elif algo == 'ASTAR':
        AStar(g, sc)
    elif algo == 'GREEDY':
        Greedy(g, sc)
    elif algo == 'BFSWITHSTATIONS':
        BFSWithStations(g,sc)
    elif algo == 'MOVING' : 
        Moving(myMatrix,sc)
    else:
        raise NotImplementedError('Not implemented')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Search algorithms')
    parser.add_argument('--algo', type=str, help='Enter search algorithm', default='DFS')
    parser.add_argument('--input', type=str, help='Enter search input file name', default='input.txt')
    args = parser.parse_args()
    main(args.algo.upper(), args.input.lower())
