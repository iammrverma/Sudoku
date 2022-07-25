import pygame
from solve import is_valid, puzzle, copy, solve, get_empty

# setting windows
WIDTH = HEIGHT = 450
x_spacing = WIDTH // 9
y_spacing = HEIGHT // 9
fps = 15
win_color = "white"
line_color = "black"


def draw_grid(win, pzl):
    font = pygame.font.SysFont('futura', 45)
    for i in range(0, 10):  # drawing the lines
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(win, line_color, (i * x_spacing, 0), (i * x_spacing, HEIGHT), width=line_width)
        pygame.draw.line(win, line_color, (0, i * y_spacing), (HEIGHT, i * y_spacing), width=line_width)
    for i in range(9):  # inserting numbers
        for j in range(9):
            win.blit(font.render(str(pzl[i][j]) if pzl[i][j] != 0 else " ", True, (125, 125, 125)),
                     (j * x_spacing + x_spacing / 4, i * y_spacing + y_spacing / 4))


def insert(win, position):
    insert_font = pygame.font.SysFont('futura', 45)
    i, j = position[0], position[1]
    i, j = j, i
    if puzzle[i][j] != 0:  # forbid editing original digit
        return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if 0 < event.key - 48 < 10:  # entering the new digit
                    if is_valid(copy, event.key - 48, i, j):
                        copy[i][j] = event.key - 48
                        pygame.draw.rect(win, win_color, (
                            position[0] * x_spacing, position[1] * y_spacing, x_spacing,
                            y_spacing))
                        value = insert_font.render(str(event.key - 48), True, (0, 0, 0))
                        win.blit(value,
                                 (position[0] * x_spacing + x_spacing / 4, position[1] * y_spacing + y_spacing / 4))
                        pygame.display.update()
                    return
                if event.key == 48:  # editing inserted digit
                    copy[i][j] = 0
                    pygame.draw.rect(win, win_color, (
                        position[0] * x_spacing, position[1] * y_spacing, x_spacing,
                        y_spacing))
                    pygame.display.update()
                    return
                if event.key == pygame.K_s:  # shortcut to solve
                    solve(puzzle)
                    return
                return
            return


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SUDOKU')
    win.fill(win_color)
    while True:
        clock = pygame.time.Clock()
        draw_grid(win, copy if get_empty(copy) is None else puzzle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0] // x_spacing, pos[1] // y_spacing))
        pygame.display.flip()
        clock.tick(fps)


main()
