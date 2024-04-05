import pygame
from maze import SearchSpace, RES
from algos import DFS, BFS, UCS, AStar, Greedy
from const import GREY
import argparse

def main(algo:str):
    your_name = 'Nguyen Vu Thanh - 21120335'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')
    sc = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(GREY))

    g = SearchSpace()
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

    args = parser.parse_args()
    main(args.algo)
