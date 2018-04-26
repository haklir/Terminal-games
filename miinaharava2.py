"""
Miinaharava - Ebin Edition
Eeppinen klassikko, joka on viety nextille levelille.
"""

from random import randrange, choice
from time import time, strftime

def main_menu():

    print("\n"
        "1 - Aloita uusi peli\n"
        "2 - Pelitilastot\n"
        "3 - Ohjeet\n"
        "4 - Poistu\n"
    )
    choice = 0
    game = 0
    
    while not 0 < choice < 5:
        try:
            choice = int(input("Valitse: "))
        except (ValueError):
            print("Valitse numero (1 - 4): ")
        except (KeyboardInterrupt, EOFError):
            choice = 4
        else:
            if not 0 < choice < 5:
                print("Valitse numero (1 - 4): ")
    
    if choice == 1:
        game = new_game()
    elif choice == 2:
        display_stats()
    elif choice == 3:
        instructions()
    
    return choice, game

def add_stats(time, moves, result):
    
    with open("stats.txt", "a") as stats:
        stats.write("{} - {:03d} - {:03d} - {} - {:02d} - {:02d} - {:03d}\n"
            .format(strftime("%d.%m.%Y %H:%M"), time, moves, result, game["WIDTH"], game["HEIGHT"], game["MINES"])
        )

def display_stats():
    
    try:
        with open("stats.txt") as stats:
            
            print("\n--Tilastot--\n\n"
                "pvm & aika, kesto(s), siirrot, häviö/voitto, leveys, korkeus, miinat\n\n"
            )
            
            while True:
                row = stats.readline()
                print(row.rstrip())
                if len(row) < 2:
                    break
            
    except (FileNotFoundError):
        print("\nTilastoja ei ole vielä olemassa.")

def instructions():
    
    print(
        "\n--Ohjeet--\n\n"
        "Pelin tavoitteena on purkaa miinakenttä. Jos et tiedä miten se tapahtuu, kysy Googlelta.\n\n"
        "Voit poistua päävalikkoon kesken pelin syöttämällä koordinaatiksi kirjaimen q.\n"
        "Keskeytetyistä peleistä ei tallenneta tilastomerkintöjä."
    )
    

def new_game():
    
    width = 0
    height = 0
    mines = 0
    
    while width < 1:
        try:
            width = int(input("Kentän leveys: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("Anna kokonaisluku.")
        else:
            if width < 1:
                print("Luvun täytyy olla suurempi kuin nolla.")
    
    while height < 1:
        try:
            height = int(input("Kentän korkeus: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("Anna kokonaisluku.")
        else:
            if height < 1:
                print("Luvun täytyy olla suurempi kuin nolla.")
    
    while mines < 1 or mines > height * width:
        try:
            mines = int(input("Miinojen lukumäärä: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("Anna kokonaisluku.")
        else:
            if mines < 1 or mines > width * height:
                print("Luvun täytyy olla välillä 1 - {}.".format(width * height))
    
    board, board_print = create_board(width, height, mines)
    game = {
        "WIDTH": width,
        "HEIGHT": height,
        "MINES": mines,
        "BOARD": board,
        "BOARD_PRINT": board_print
    }
    return game

def create_board(width, height, mines):
    
    board = []
    board_print = []
    mines_placed = 0
    empty = []
    
    for y in range(height):
        board.append([])
    for row in board:
        for i in range(width):
            row.append(0)

    for i in range(width):
        for j in range(height):
            empty.append((i + 1, j + 1))
    
    while mines_placed < mines:
        a = randrange(len(empty))
        (x, y) = empty[a]
        empty.__delitem__(a)
        board[y - 1][x - 1] = 1
        mines_placed += 1
    
    for i in range(height):
        board_print.append([])
    for i in range(height):
        for j in range(width):
            board_print[i].append("+")
    
    return board, board_print

############################################

def ask_coordinates():
    
    while True:
        
        while True:
            try:
                x = input("Avaa ruutu antamalla sen x-koordinaatti: ")
                if x == "q":
                    return None, None
                x = int(x)
            except (ValueError, KeyboardInterrupt, EOFError):
                print("Koordinaatin tulee olla kokonaisluku.")
            else:
                if x < 1 or x > game["WIDTH"]:
                    print("Koordinaatti on kentän ulkopuolella.")
                else:
                    break
        
        while True:
            try:
                y = input("ja y-koordinaatti: ")
                if y == "q":
                    return None, None
                y = int(y)
            except (ValueError, KeyboardInterrupt, EOFError):
                print("Koordinaatin tulee olla kokonaisluku.")
            else:
                if y < 1 or y > game["HEIGHT"]:
                    print("Koordinaatti on kentän ulkopuolella.")
                else:
                    break
        
        if game["BOARD_PRINT"][y - 1][x - 1] != "+":
            print("Olet jo avannut kyseisen ruudun.")
        else:
            break
    
    return x, y

def print_board():
    
    print()
    
    for i in range(game["HEIGHT"] -1, -1, -1):
            print("{:02d}".format(i + 1), "  ".join(game["BOARD_PRINT"][i]))
    
    numbers = ["  "]
    for i in range(game["WIDTH"]):
            numbers.append("{:02d}".format(i + 1))
    print(" ".join(numbers), "\n")

def count_mines(x, y):
    
    mines_around = 0
    
    if game["BOARD"][y - 1][x - 1] == 1:
        game["BOARD_PRINT"][y - 1][x - 1] = "¤"
        return "mine"
    
    for i in range(-1, 2):
        if x + i < 1 or x + i > game["WIDTH"]:
            continue
        for j in range(-1, 2):
            if y + j < 1 or y + j > game["HEIGHT"]:
                continue
            if game["BOARD"][y + j - 1][x + i - 1] == 1:
                mines_around += 1
    
    if mines_around == 0:
        game["BOARD_PRINT"][y - 1][x - 1] = " "
    else:
        game["BOARD_PRINT"][y - 1][x - 1] = str(mines_around)
    
    return mines_around

def sweep(x, y):
    
    sweeped = []
    to_be_sweeped = [(x, y)]
    while len(to_be_sweeped) > 0:
        (x, y) = to_be_sweeped[-1]
        to_be_sweeped.__delitem__(-1)
        mines_around = count_mines(x, y)
        if mines_around == 0:
            for i in range(-1, 2):
                if x + i < 1 or x + i > game["WIDTH"]:
                    continue
                for j in range(-1, 2):
                    if y + j < 1 or y + j > game["HEIGHT"]:
                        continue
                    if (x + i, y + j) not in sweeped:
                        to_be_sweeped.append((x + i, y + j))
        sweeped.append((x, y))

def the_end(message, result):
    
    for i in range(game["WIDTH"]):
        for j in range(game["HEIGHT"]):
            if game["BOARD_PRINT"][j][i] == "+":
                count_mines(i + 1, j + 1)
    
    print_board()
    elapsed_time = round(time() - starting_time)
    print(
        "{}\n"
        "Peli kesti {} sekuntia.\n"
        "Teit pelin aikana {} siirtoa."
        .format(message, elapsed_time, moves)
    )
    add_stats(elapsed_time, moves, result)
            
if __name__ == "__main__":
    print("\n--Miinaharava--")
    
    choice = 0
    while choice != 4:
        choice, game = main_menu()
        if choice == 1:
            starting_time = time()
            moves = 0
        
        while choice == 1:
            print_board()
            x, y = ask_coordinates()
            moves += 1
            
            if x == None:
                break
            
            if count_mines(x, y) == "mine":
                the_end("Astuit miinaan!", "H")
                choice = 0
            elif count_mines(x, y) == 0:
                sweep(x, y)
            
            unopened = 0
            for row in game["BOARD_PRINT"]:
                unopened += row.count("+")
            if unopened == game["MINES"]:
                the_end("Onneksi olkoon selvisit hengissä!", "V")
                choice = 0