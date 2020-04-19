from os import system, name
from colors import bcolors as c
from Tictacktoe import TicTacToe
import csv
import pandas as pd

def clear_screen():
    """Clear the terminal to make the game look better.
    Works for windows/linux/mac"""

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def make_empty_dict():
    """Create empty dict to save temporary stats between rounds."""

    temp_stats = {'totalgames':0, 'X_win':0, 'O_win':0, 'draw':0, 'X_n_moves':0, 'O_n_moves':0, 'n_moves':0}
    return temp_stats

def save_stats_to_dict(current_player_number, temp_stats, rounds):
    if current_player_number == 1:
        temp_stats['X_win'] = 1
        temp_stats['X_n_moves'] = (int(rounds / 2 + 1))

    if current_player_number == 2:
        temp_stats['O_win'] = 1
        temp_stats['O_n_moves'] = (int(rounds / 2))

    if current_player_number == 'draw':
        temp_stats['draw'] = 1
        temp_stats['O_n_moves'] = (int(rounds / 2))
        temp_stats['X_n_moves'] = (int(rounds / 2 + 1))

    temp_stats['n_moves'] = rounds
    temp_stats['totalgames'] = 1

    write_stats_to_file(temp_stats)

def write_stats_to_file(temp_stats):
    """Found this on stackoverflow to save the stats from a round to a csv file(from a dict).
    If the file doesent exist it creates one."""

    with open('stats.csv', 'a') as f:
        w = csv.DictWriter(f, temp_stats.keys())
        if f.tell() == 0:
            w.writeheader()
            w.writerow(temp_stats)
        else:
            w.writerow(temp_stats)

def save_current_stats(current_player_number, rounds):
    temp_stats = make_empty_dict()
    save_stats_to_dict(current_player_number, temp_stats, rounds)

def choose_grid():
    while True:
        try:
            grid_size = int(input("\nChoose gridsize : "))
        except ValueError:
            print("Wrong input must be a number")
            continue

        if grid_size < 3 or grid_size > 10:
            print("To small or to large")
            continue
        else:
            return grid_size

def choose_player_name(player):
    while True:
        player_name = input(f"\nName player {player} : ")

        if player_name.isdigit() or player_name == "":
            print("Name cant be a number ")
            continue
        else:
            return player_name

def return_current_player(current_player_number, player_one, player_two):
    """Function to switch player on every loop"""

    if current_player_number % 2 == 0:
        current_player_name = player_two
        current_player_number = 2
        return current_player_number, current_player_name

    else:
        current_player_name = player_one
        current_player_number = 1
        return current_player_number, current_player_name

def set_player_marker(current_player_number):
    if current_player_number == 1:
        return 'XX'
    else:
        return 'OO'

def check_win(t, rounds, grid_size, current_player_number, current_player_marker, current_player_name):
    """Checks if the player has gotten enough markers in a row to win or if the game is a draw"""

    win = False
    draw = False

    if t.check_win_horizontal(current_player_marker):
        win = True

    if t.check_win_vertical(current_player_marker):
        win = True

    if t.check_win_diagonally_right(current_player_marker):
        win = True

    if t.check_win_diagonally_left(current_player_marker):
        win = True

    if t.check_for_draw(rounds, grid_size) and win == False:
        draw = True

    if win == True or draw == True:
        clear_screen()
        t.print_grid()

        if win:
            print(c.blink + "\n" + current_player_name + " is the winner!!!\n" + c.RESET)

        if draw:
            current_player_number = 'draw'
            print(c.blink + "\n" + "The game is a draw!\n" + c.RESET)

        save_current_stats(current_player_number, rounds)

        return True
    return False

def play_again(choice):
    if choice == 'y':
        return True
    else:
        return False

def user_input(current_player_name, status_message):
    while True:
        try:
            chosen_number = int(input(c.CYELLOW + current_player_name + status_message + " --> " + c.RESET))
            return chosen_number
        except ValueError:
            print("Wrong input must be a number")
            continue

def meny():
    while True:
        clear_screen()
        print(" -----------------")
        print(c.CGREEN + " #1.Play TicTacToe")
        print(" #2.Print stats")
        print(" #3.Rules")
        print(" #4.Quit" + c.RESET)
        print(" -----------------")
        try:
           sub_meny = int(input('\n --> '))
        except ValueError:
            print("Wrong input")
            continue
        if(sub_meny == 1):
            game_loop()
        if(sub_meny == 2):
            print_game_stats()
        if(sub_meny == 3):
            print_game_rules()
        if(sub_meny == 4):
            break

def print_game_rules():
    clear_screen()
    print(" -----------------------------------------------")
    print(c.OKBLUE + " * Pick a size for the board(3 means 3x3 grid) *")
    print(" * Minumum 3 and maximum 10                    *")
    print(" * For boardsize 3-5 you win with 3 in a row   *")
    print(" * For boardsize 6-7 you win with 4 in a row   *")
    print(" * For boardsize 8-10 you win with 5 in a row  *" + c.RESET)
    print(" -----------------------------------------------")

    input("\n Press ENTER to exit")

def print_game_stats():
    clear_screen()
    try:
        df = pd.read_csv (r'stats.csv')

        total_games = df['totalgames'].sum()
        x_wins = df['X_win'].sum()
        o_wins = df['O_win'].sum()
        draw = df['draw'].sum()
        average_move = df['n_moves'].mean()
        average_x_win_move = df.loc[df.X_win == 1, 'X_n_moves'].mean()
        average_o_win_move = df.loc[df.O_win == 1, 'O_n_moves'].mean()
        x_win_procent = x_wins/total_games * 100
        o_win_procent = o_wins/total_games * 100
        draw_procent = draw/total_games * 100

        print(" -----------------------------")
        print(c.OKBLUE + f' Total games played: {total_games}\n')
        print(f' Total wins X: {x_wins}, {x_win_procent:.1f}%\n')
        print(f' Total wins O: {o_wins}, {o_win_procent:.1f}%\n')
        print(f' Total draws: {draw}, {draw_procent:.1f}%\n')
        print(f' Average moves per game: {average_move:.1f}\n')
        print(f' Average X win moves: {average_x_win_move:.1f}\n')
        print(f' Average O win moves: {average_o_win_move:.1f}' + c.RESET)
        print(" -----------------------------")

    except IOError:
        print(" No history yet, you need to play first")
    except pd.errors.EmptyDataError:
        print(" No history yet, you need to play first")

    input("\n Press ENTER to exit")

def game_loop():
    """The game runs in here, if you dont wanna play again it exits to the mainmeny"""

    grid_size = choose_grid()

    t = TicTacToe(grid_size)

    player_one = choose_player_name("one")
    player_two = choose_player_name("two")

    rounds = 0
    status_message = c.italic + " Make a move"
    current_player_number = 1

    while True:
        clear_screen()
        t.print_grid()

        print(c.CGREY + f"\nget {t.n_markers_to_win} to win\n" + c.RESET)

        current_player_number, current_player_name = return_current_player(current_player_number, player_one, player_two)

        chosen_number = user_input(current_player_name, status_message)

        spot_is_available = t.check_if_available(chosen_number)

        if spot_is_available:
            t.place_marker(chosen_number, current_player_number, grid_size)
            status_message = c.italic + " Make a move"
            clear_screen()
            t.print_grid()
        else:
            status_message = c.italic + " Try again number dont exist or is taken"
            continue

        rounds += 1

        current_player_marker = set_player_marker(current_player_number)

        if check_win(t, rounds, grid_size, current_player_number, current_player_marker, current_player_name) == True:

            if play_again(input("Play again? Y/N --> " ).lower()):
                t = TicTacToe(grid_size)
                rounds = 0
                current_player_number = 1
                continue
            else:
                break

        current_player_number += 1

if __name__ == '__main__':
    meny()
