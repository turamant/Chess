class ChessFigure:
    """Chess piece class"""
    IMG = None
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[self.color]


class Pawn(ChessFigure):
    IMG = ('♙', '♟︎')

class King(ChessFigure):
    IMG = ('♔', '♚')

class Queen(ChessFigure):
    IMG = ('♕', '♛')

class Elephant(ChessFigure):
    IMG = ('♗', '♝')

class Horse(ChessFigure):
    IMG = ('♘', '♞')

class Rook(ChessFigure):
    IMG = ('♖', '♜')

class ChessBoard:
    """Chess board class"""
    def __init__(self):
        self.board = [['.']*8 for y in range(8)]
        self.placing_pawn()
        self.placing_figure()

    def placing_pawn(self):
        """Placement of pawns on the chessboard """
        for pawn in range(0, 8):
            self.board[1][pawn] = Pawn(0) # color white
            self.board[6][pawn] = Pawn(1) # color black

    def placing_figure(self):
        """Arrangement of pieces on the chessboard """
        for f in range(0, 8, 7):
            if f == 0:
                color = 0 # white color
            else:
                color = 1 # black color
            self.board[f][0] = Rook(color)
            self.board[f][1] = Horse(color)
            self.board[f][2] = Elephant(color)
            self.board[f][3] = King(color)
            self.board[f][4] = Queen(color)
            self.board[f][5] = Elephant(color)
            self.board[f][6] = Horse(color)
            self.board[f][7] = Rook(color)

    def __repr__(self):
        res = ''
        for i in range(8):
            res += ''.join(map(str, self.board[i])) + '\n'
        return res



if __name__ == '__main__':
    print(ChessBoard())



