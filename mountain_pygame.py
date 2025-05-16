import pygame
import sys, math

pygame.init()
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

FPS = 60
FramePerSec = pygame.time.Clock()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))

n = 5
rect_height = 40
rect_width = 60
margin = 20



centers = []
current_path = []
lines = []

while True:
    
    screen.fill((255, 255, 255))


    starting_x = margin + (n - 1) * (rect_width / 2)
    y = margin
    for row_num in range(0, n):
        x = starting_x
        for rect_index in range(0, row_num + 1):
            if (row_num, rect_index) in current_path:
                pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(x, y, rect_width, rect_height), 1)
            x += rect_width

        starting_x -= rect_width // 2
        y += rect_height


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row_num = (y - margin) // rect_height
            rect_index = (x - margin - (n - row_num - 1) * (rect_width // 2)) // rect_width
            current_path = [(row_num, rect_index)]
            print(current_path)
        
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            row_num = (y - margin) // rect_height
            rect_index = (x - margin - (n - row_num - 1) * (rect_width // 2)) // rect_width
            if row_num >= 0 and row_num < n and rect_index <= row_num and rect_index >= 0:
                if len(current_path) > 0 and current_path[-1] != (row_num, rect_index):
                    if len(current_path) > 1:
                        if current_path[-2] == (row_num, rect_index):
                            current_path = current_path[:-1]
                        elif (current_path[-1][0] - row_num, current_path[-1][1] - rect_index) in [(-1, -1), (-1, 0), (1, 0), (1, 1)]:
                            current_path.append((row_num, rect_index))
                    elif (current_path[-1][0] - row_num, current_path[-1][1] - rect_index) in [(-1, -1), (-1, 0), (1, 0), (1, 1)]:
                        current_path.append((row_num, rect_index))

        if event.type == pygame.MOUSEBUTTONUP:
            current_path = []


    pygame.display.flip()
    pygame.time.Clock()