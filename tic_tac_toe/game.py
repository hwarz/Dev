from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
# Создать игровое поле - объект класса Board.
    game = Board()
# Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True

# Отрисовать поле в терминале.
    game.display()
# Тут запускается основной цикл игры.
    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
            # Тут пользователь вводит координаты ячейки.
                x = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
                if x < 0 or x >= game.field_size:
        # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                y = int(input('Введите номер столбца: '))
                if y < 0 or y >= game.field_size:
                    raise FieldIndexError
                if game.board[x][y] != ' ':
                    raise CellOccupiedError
            # Если возникает исключение FieldIndexError...
            except FieldIndexError:
            # ...выводятся сообщения...
                print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
                continue
        # Если в блоке try исключения не возникло...
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
                break
  

# Разместить на поле символ по указанным координатам - сделать ход.
# Теперь для установки значения на поле само значение берётся
# из переменной current_player.              
        game.make_move(x, y, current_player)
    # print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
        game.display()
    # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            running - False
        elif game.is_board_full():
            print('Ничья!')
            result_str = 'Ничья!'
            running = False    
    # Теперь для установки значения на поле само значение берётся
    # из переменной current_player.
        current_player = '0' if current_player == 'X' else 'X'
    

if __name__ == '__main__':
    main()
    