
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

    def is_board_full(self):   
        # Цикл проходится по всем столбцам и строкам игрового поля.
        for i in range(self.field_size):
            for j in range(self.field_size):
                 # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    return False
        # Иначе - ничья!
        return True
    
    # Этот метод будет определять победу.
    def check_win(self, player):
      # Тут реализована проверка по вертикали и горизонтали.
        for i in range (3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Тут реализована проверка по диагонали.
        if(
           self.board[0][0] == self.board[1][1] == self.board[2][2] == player
           or
           self.board[0][2] == self.board[1][1] == self.board[2][0] == player 
        ):
            return True
        