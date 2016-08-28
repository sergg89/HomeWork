class Board(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_board(self):
        for i in range(self.a):
            if i % 2 == 0:
                self.print_row(0)
            else:
                self.print_row(1)

    def print_row(self, start_status):
        for j in range(self.b):
            if j % 2 == start_status:
                print '*',
            else:
                print ' ',
        print '\n',


b = Board(8,8)
b.print_board()