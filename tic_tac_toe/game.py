import pygame
from gameparts import Board
# from gameparts.exceptions import FieldIndexError, CellOccupiedError

pygame.init()

# Здесь определены разные константы, например 
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (242, 235, 211)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Задать размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Установить заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Заполнить фон окна заданным цветом.
screen.fill(BG_COLOR)

# Функция, которая отвечает за отрисовку горизонтальных и вертикальных линий.
def draw_lines():
    # Горизонтальные
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH 
        )

    # Вертикальные
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )

    # Функция, которая отвечает за отрисовку фигур 
    # (крестиков и ноликов) на доске.

def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (                   # рисует \
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (             # рисует /
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH    
                )
            elif board[row][col] == '0':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )
# Сюда нужно добавить функцию save_result().


def main():
# Создать игровое поле - объект класса Board.
    game = Board()
# Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    draw_lines()
# Отрисовать поле в терминале.
    # game.display()
# Тут запускается основной цикл игры.
    
    while running:
        # print(f'Ход делают {current_player}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE


        #while True:
        #    try:
            # Тут пользователь вводит координаты ячейки.
               # x = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
                # if x < 0 or x >= game.field_size:
        # ...выбросить исключение FieldIndexError.
                    # raise FieldIndexError
                # y = int(input('Введите номер столбца: '))
                #if y < 0 or y >= game.field_size:
                    # raise FieldIndexError
                if game.board[clicked_row][clicked_col] == ' ':
                    # raise CellOccupiedError
            # Если возникает исключение FieldIndexError...
            #except FieldIndexError:
            # ...выводятся сообщения...
             #   print(
             #   'Значение должно быть неотрицательным и меньше '
             ##   f'{game.field_size}.'
             #   )
             #   print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
            #    continue
        # Если в блоке try исключения не возникло...
            # except ValueError:
            #    print('Буквы вводить нельзя. Только числа.')
            #    print('Пожалуйста, введите значения для строки и столбца заново.')
            #    continue
            # except CellOccupiedError:
            #    print('Ячейка занята')
            #    print('Введите другие координаты.')
            #    continue
            # except Exception as e:
            #    print(f'Возникла ошибка: {e}')
            #    continue
            # else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            #    break
  

# Разместить на поле символ по указанным координатам - сделать ход.
# Теперь для установки значения на поле само значение берётся
# из переменной current_player.              
                    game.make_move(clicked_row, clicked_col, current_player)
    # print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
        # game.display()
    # После каждого хода надо делать проверку на победу и на ничью.
                    if game.check_win(current_player):
                        result = f'Победили {current_player}.'
                        print(result)
                        game.save_result(result)
                        running = False
                    elif game.is_board_full():
                        result = 'Ничья'
                        print(result)
                        game.save_result(result)
                        running = False
    # Теперь для установки значения на поле само значение берётся
    # из переменной current_player.
                    current_player = '0' if current_player == 'X' else 'X'
                    draw_figures(game.board)

        pygame.display.update()

    pygame.quit()                
    

if __name__ == '__main__':
    main()
    