
class Board:
    field_size = 3
    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    
    def __init__(self):
        self.board = [[' ' for i in range(self.field_size)] for i in range(self.field_size)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, x, y, player):
        self.board[x][y] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for i in self.board:
            print('|'.join(i))
            print('-' * 5)
