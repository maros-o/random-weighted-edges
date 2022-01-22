import pygame
import random

pygame.font.init()

X, Y = 50, 30
HALF_X = X//2
HALF_Y = Y//2
BLOCK_SIZE = 32
WIDTH, HEIGHT = X * BLOCK_SIZE, Y * BLOCK_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont('consolas', 20)

BGCOLOR = (130, 200, 255)
TEXTCOLOR = (255, 255, 255)
BLACK = (0, 0, 0)
NODECOLOR = (210,105,30)

class Node():
    def __init__(self, pos, number):
        self.pos = pos
        self.number = number

    def get_pos(self):
        return self.pos

    def get_number(self):
        return self.number

def create_edges():
    edges = [[0 for y in range(0, HALF_Y * HALF_X)] for x in range(0, HALF_X * HALF_Y)]
    print("edges len:", len(edges))

    skiplist = [HALF_X * x for x in range(0, HALF_X)]
    for x in range(0, HALF_X * HALF_Y):
        for y in range(0, HALF_Y * HALF_X):
            if not (x == y):
                if (x + 1 == y and y not in skiplist): edges[x][y] = random.randint(1, 3)
                elif (x + HALF_X == y): edges[x][y] = random.randint(1, 3)

    return edges    

def draw_edges(nodes, edges):
    for x in range(0, HALF_X * HALF_Y):
        for y in range(0, HALF_Y * HALF_X):
            if not (edges[x][y] == 0):
                for pos_x in range(0, HALF_X):
                    for pos_y in range(0, HALF_Y):
                        if (nodes[pos_x][pos_y].get_number() == x):
                            start = nodes[pos_x][pos_y].get_pos()
                        elif (nodes[pos_x][pos_y].get_number() == y):
                            end = nodes[pos_x][pos_y].get_pos()

                weight = edges[x][y]
                weight_color_power = 60

                color = (200 - weight * weight_color_power, 200 - weight * weight_color_power, 200 - weight * weight_color_power)

                pygame.draw.line(WIN, color, [start[0] * BLOCK_SIZE, start[1] * BLOCK_SIZE], [end[0] * BLOCK_SIZE, end[1] * BLOCK_SIZE ], weight * 3)


def create_nodes():
    nodes = [[Node((x*2+1, y*2+1), x + y * HALF_X) for y in range(0, HALF_Y)] for x in range(0, HALF_X)]
    print("nodes len:", len(nodes))
    return nodes

def draw_nodes(nodes):
    for x in range(0, HALF_X):
        for y in range(0, HALF_Y):
            pos_x, pos_y = nodes[x][y].get_pos()
            number = nodes[x][y].get_number()

            circle_radius = 14
            pygame.draw.circle(WIN, NODECOLOR, [pos_x * BLOCK_SIZE, pos_y * BLOCK_SIZE], circle_radius)

            text = FONT.render(str(number), 1, TEXTCOLOR)
            WIN.blit(text, (pos_x * BLOCK_SIZE - text.get_rect().width // 2, pos_y * BLOCK_SIZE - text.get_rect().height // 2))

def draw_grid():
    for x in range(1, X):
        pygame.draw.line(WIN, BLACK, [x * BLOCK_SIZE, 0], [x * BLOCK_SIZE, Y * BLOCK_SIZE])
    for y in range(1, Y):
        pygame.draw.line(WIN, BLACK, [0, y * BLOCK_SIZE], [X * BLOCK_SIZE, y * BLOCK_SIZE])

def draw_window(nodes, edges):
    WIN.fill(BGCOLOR)

    #draw_grid()
    draw_edges(nodes, edges)
    draw_nodes(nodes)

    pygame.display.update()

def main():
    pygame.display.set_caption("nodes with random weighted edges")

    nodes = create_nodes()
    edges = create_edges()

    draw_window(nodes, edges)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

main()