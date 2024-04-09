import pygame
from maze import SearchSpace
from algos import DFS, BFS, UCS, AStar, Greedy
from const import GREY, BOUND , A1
from model_matrix import Matrix
import argparse

def main(algo:str, inputFile: str = 'input.txt'):
    your_name = 'Nguyen Vu Thanh - 21120335'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')

    #initialize map 
    myMatrix = Matrix() 
    myMatrix.parseFile(inputFile)
    COLS, ROWS= myMatrix.width+1, myMatrix.height+1
    RES = WIDTH , HEIGHT = 800+2*BOUND + (ROWS-1)*(A1), 800+2*BOUND + (COLS-1)*(A1)

    sc = pygame.display.set_mode(RES)
    print(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(GREY))


    g = SearchSpace(myMatrix)

    g.draw(sc)
    clock.tick(200)

    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    elif algo == 'UCS':
        UCS(g, sc)
    elif algo == 'AStar':
        AStar(g, sc)
    elif algo == 'Greedy':
        Greedy(g, sc)
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
