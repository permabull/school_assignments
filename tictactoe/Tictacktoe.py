
from colors import bcolors as c

"""hej"""

class TicTacToe:

    def __init__(self, grid_size):
        self.grid_layout = self.generate_grid(grid_size)
        self.player_one_marker = 'XX'
        self.player_two_marker = 'OO'
        self.board_frame = self.make_frame(grid_size)
        self.n_markers_to_win = self.n_markers_to_win(grid_size)

    def n_markers_to_win(self, grid_size):
        """Number of markers the player needs to win a game depending in gridsize"""

        if grid_size >= 3 and grid_size <= 5:
            return 3
        if grid_size >= 6 and grid_size <= 7:
            return 4
        if grid_size >= 8 and grid_size <= 10:
            return 5

    def make_frame(self, grid_size):
        return "___" * grid_size

    def generate_grid(self, grid_size):
        return [list(range(s, s+grid_size)) for s in range(1, grid_size*grid_size, grid_size)]

    def print_grid(self):
        print(c.CWHITE +  self.board_frame + "\n" + c.RESET)

        for i in range(len(self.grid_layout)) :
            for j in range(len(self.grid_layout[i])):

                if type(self.grid_layout[i][j]) == int:

                    if self.grid_layout[i][j] < 10:
                        print(c.CWHITE + "0" + str(self.grid_layout[i][j]), end=" " + c.RESET)
                    else:
                        print(c.CWHITE + str(self.grid_layout[i][j]), end=" " + c.RESET)

                elif self.grid_layout[i][j] == self.player_one_marker:
                    print(c.WARNING + str(self.grid_layout[i][j]), end=" " + c.RESET)

                elif self.grid_layout[i][j] == self.player_two_marker:
                    print(c.FAIL + str(self.grid_layout[i][j]), end=" " + c.RESET)

                else:
                    print(str(self.grid_layout[i][j]), end=" ")
            print()

        print(c.CWHITE + self.board_frame)

    def check_if_available(self, chosen_number):
        """Check if the number that the current player choose is not taken
        and place its market on the board"""

        for i in range(len(self.grid_layout)) :
            for j in range(len(self.grid_layout[i])):

                if chosen_number == self.grid_layout[i][j]:

                    if self.grid_layout[i][j] == self.player_one_marker or self.grid_layout[i][j] == self.player_two_marker:
                        return False
                    else:
                        return True

    def place_marker(self, chosen_number, player, grid_size):
        for i in range(0, grid_size):
            for j in range(0, grid_size):

                if chosen_number == self.grid_layout[i][j]:

                    if player == 1:
                        self.grid_layout[i][j] = self.player_one_marker
                        return
                    elif player == 2:
                        self.grid_layout[i][j] = self.player_two_marker
                        return

    def check_for_draw(self, rounds, grid_size):
        if rounds == grid_size * grid_size:
            return True
        else:
            return False

    """The four functions below is almost identical except for the while loop condition.
    If it finds a correct marker it will keep looking for the right pattern and if the conditions
    are met the player wins"""

    def check_win_horizontal(self, player_marker):
        for i in range(len(self.grid_layout)) :
            for j in range(len(self.grid_layout[i])):
                try:
                    if self.grid_layout[i][j] == player_marker:
                        counter = 1
                        hits = 1

                        while self.grid_layout[i][j+counter] == player_marker:
                            hits += 1
                            counter += 1

                            if hits == self.n_markers_to_win:
                                return True

                except IndexError:
                    pass
        return False

    def check_win_vertical(self, player_marker):
        for i in range(len(self.grid_layout)) :
            for j in range(len(self.grid_layout[i])):
                try:
                    if self.grid_layout[i][j] == player_marker:
                        counter = 1
                        hits = 1

                        while self.grid_layout[i+counter][j] == player_marker:
                            hits += 1
                            counter += 1

                            if hits == self.n_markers_to_win:
                                return True

                except IndexError:
                    pass
        return False

    def check_win_diagonally_right(self, player_marker):
        for i in range(len(self.grid_layout)) :
            for j in range(len(self.grid_layout[i])):
                try:
                    if self.grid_layout[i][j] == player_marker:
                        counter = 1
                        hits = 1

                        while self.grid_layout[i+counter][j+counter] == player_marker:
                            hits += 1
                            counter += 1

                            if hits == self.n_markers_to_win:
                                return True

                except IndexError:
                    pass
        return False

    def check_win_diagonally_left(self, player_marker):

          for i in range(len(self.grid_layout)) :
              for j in range(len(self.grid_layout[i])):
                  try:
                      if self.grid_layout[i][j] == player_marker:
                          counter = 1
                          hits = 1

                          while self.grid_layout[i+counter][j-counter] == player_marker and j-counter >= 0:
                              hits += 1
                              counter += 1

                              if hits == self.n_markers_to_win:
                                  return True

                  except IndexError:
                      pass
          return False
