from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
# Создать игровое поле - объект класса Board.
    game = Board()
# Отрисовать поле в терминале.
    game.display()
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
        except Exception as e:
            print(f'Возникла ошибка: {e}')
            continue
        else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break
  

# Разместить на поле символ по указанным координатам - сделать ход.
    game.make_move(x, y, 'X')
    print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
 