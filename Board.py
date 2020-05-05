class Board:
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def render(self):
        for row in self.board:
            row_string = ""
            for row_item in row:
                row_string += row_item + "|"

            print(row_string[:5])

    @property
    def game_over(self):
        rows = self.board
        columns = [[], [], []]
        col_index = 0
        for row in rows:
            columns.append(row[col_index])
            col_index += 1
        
        for row in self.board:
            if "-" in row or ("X" in row and "O" in row): continue
            return True

        return False
