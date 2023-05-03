
import pygame
import random
from numpy import empty, int8
pygame.init()

# board info
screen = pygame.display.set_mode((735, 735),pygame.FULLSCREEN)
screen.fill((100, 80, 50))
tol = 80
arz = 80
col = 5
row = 5
from  pygame import  mixer
mixer.music.load('PerituneMaterial_Sakuya2.mp3')
mixer.music.play(-1)


# classes
class Card:
    card_height = 120
    card_width = 200
    bg_color = (180, 180, 180)

    def __init__(self, name, moves, starter):
        self.name = name
        self.moves = moves
        self.starter = starter


class Piece:
    def __init__(self, king_or_not, color, location, value):
        self.value = value
        self.king_or_not = king_or_not
        self.color = color
        self.location = location

    def move(self, destination):
        self.location = destination


class Hexes:
    def __init__(self, the_piece_on_it, location, is_showed_to_move):
        self.the_piece_on_it = the_piece_on_it
        self.location = location
        self.is_showed_to_move = is_showed_to_move

    def select(self, origin, selected_card, turn, pieces):
        # a piece is selected. we are going to show moves that are allowed
        if self.the_piece_on_it is not None and not self.is_showed_to_move:
            if self.the_piece_on_it.color == turn:
                # cleaning the last showed hexes
                for i in pieces:
                    for x in i:
                        x.is_showed_to_move = False

                # shows the valid moves
                for i in cards_info[selected_card][2].moves:
                    i = self.location + i if turn == "red" else self.location + i * -1

                    # because our x y in valid moves is 1 more. y is 10 and x is 1
                    if i // 10 >= 0 and i // 10 <= 4 and i % 10 >= 0 and i % 10 <= 4:
                        if pieces[i // 10][i % 10].the_piece_on_it is not None:  # a piece is in that hex
                            if pieces[i // 10][i % 10].the_piece_on_it.color != turn:  # the is not for us
                                pieces[i // 10][i % 10].is_showed_to_move = True
                        else:
                            pieces[i // 10][i % 10].is_showed_to_move = True  # there isn't any piece in that hex
                return self.location  # we return the selected hex
            else:
                # user has tried to select a piece that doesn't it's turn
                for i in pieces:
                    for x in i:
                        x.is_showed_to_move = False

        elif self.is_showed_to_move:  # a piece is moved to this hex
            pieces[origin // 10][origin % 10].the_piece_on_it.move(self.location)
            self.the_piece_on_it = pieces[origin // 10][origin % 10].the_piece_on_it
            pieces[origin // 10][origin % 10].the_piece_on_it = None

            for i in pieces:  # cleaning the showed hexes
                for x in i:
                    x.is_showed_to_move = False
            return -2

        elif not self.is_showed_to_move and self.the_piece_on_it is None:
            for i in pieces:  # the mouse button down did nothing, so we clean the last showed hexes
                for x in i:
                    x.is_showed_to_move = False


class Ai:

    def win_or_not(self, grid, turn_):
        if grid[0][2] == 100:

            return True
        if grid[4][2] == -100:
            return True
        for i in grid:
            for x in i:
                if x == turn_ * -100:
                    return False
        return True






    def graphic(self,selected_card,pieces):
        # Icon
        pygame_icon = pygame.image.load('images.jpg')
        pygame.display.set_icon(pygame_icon)
        # background
        background = pygame.image.load("background1.jpg")
        screen.blit(background, (0, 0))
        # every thing in board
        board = pygame.image.load("Screenshot_20230226_075425.png")
        board = pygame.transform.scale(board, (400, 400))
        screen.blit(board, (50, 156))
        for y in range(5):
            for x in range(5):
                # make board

                # pygame.draw.rect(screen, (200, 200, 100), (x * 80 + 50, y * 80 + 156, 78, 78))

                # show moves
                if pieces[y][x].is_showed_to_move and pieces[y][x].the_piece_on_it is None:
                    pygame.draw.rect(screen, (200, 120, 25), (50 + x * 80, 156 + y * 80, 80, 80))

                elif pieces[y][x].is_showed_to_move and pieces[y][x].the_piece_on_it is not None:
                    pygame.draw.rect(screen, (184, 76, 76), (50 + x * 80, 156 + y * 80, 78, 78))


                    if pieces[y][x].the_piece_on_it.king_or_not:
                        pygame.draw.rect(screen, (0, 255, 0), (50 + x * 80 + 25, 156 + y * 80 + 25, 30, 30))

                # make pieces
                if pieces[y][x].the_piece_on_it is not None:

                    # students
                    a = pieces[y][x].the_piece_on_it
                    # pygame.draw.circle(screen, (200, 0, 0) if a.color == "red" else (0, 0, 200),
                    # (x * 80 + 39 + 50, y * 80 + 39 + 156), 29)

                    if pieces[y][x].the_piece_on_it.color == "red":
                        srudent = pygame.image.load("student_red_asli.png")
                        srudent = pygame.transform.scale(srudent, (70, 70))
                        screen.blit(srudent, (50 + x * 80 + 5, 156 + y * 80 + 10))
                    else:
                        student = pygame.image.load("student_blue.png")
                        student = pygame.transform.scale(student, (80, 80))
                        screen.blit(student, (50 + x * 80 + 5, 156 + y * 80 + 3))

                    # masters
                    if pieces[y][x].the_piece_on_it.king_or_not and pieces[y][x].the_piece_on_it.color == "red":
                        master_r = pygame.image.load("ostad_red.png")
                        master_r = pygame.transform.scale(master_r, (80, 80))
                        screen.blit(master_r, (50 + x * 80 + 5, 156 + y * 80 + 3))
                        # pygame.draw.rect(screen, (0, 255, 0), (50 + x * 80 + 25, 156 + y * 80 + 25, 30, 30))
                    if pieces[y][x].the_piece_on_it.king_or_not and pieces[y][x].the_piece_on_it.color == "blue":
                        master_r = pygame.image.load("ostadl_blue.png")
                        master_r = pygame.transform.scale(master_r, (80, 80))
                        screen.blit(master_r, (50 + x * 80 + 5, 156 + y * 80 + 3))

        # cards
        for i in range(5):
            # bg of cards
            pygame.draw.rect(screen, (0, 0, 0), (cards_info[i][0], cards_info[i][1], 200, 120))

            # 5x5 small white board on it
            for n in range(5):
                for m in range(5):
                    pygame.draw.rect(screen, (255, 255, 255), (cards_info[i][0] + 10 + n * 20,
                                                               cards_info[i][1] + 10 + m * 20, 18, 18))

            # show the moves of cards
            # yellow square
            pygame.draw.rect(screen, (0, 255, 255), (cards_info[i][0] + 10 + 2 * 20,
                                                     cards_info[i][1] + 10 + 2 * 20, 18, 18))

            for n in cards_info[i][2].moves:
                # green squares
                if i > 2:
                    n *= -1
                pygame.draw.rect(screen, (0, 255, 0), (cards_info[i][0] + 10 + ((33 + n) % 10 - 1) * 20,
                                                       cards_info[i][1] + 10 + ((33 + n) // 10 - 1) * 20, 18, 18))
        # selected card
        pygame.draw.rect(screen, (0, 0, 255),
                         (cards_info[selected_card][0] - 5, cards_info[selected_card][1] - 5, 5, 130))
        pygame.draw.rect(screen, (0, 0, 255),
                         (cards_info[selected_card][0] + 200, cards_info[selected_card][1] - 5, 5, 130))
        pygame.draw.rect(screen, (0, 0, 255), (cards_info[selected_card][0], cards_info[selected_card][1] - 5, 200, 5))
        pygame.draw.rect(screen, (0, 0, 255),
                         (cards_info[selected_card][0], cards_info[selected_card][1] + 120, 200, 5))

    def get_data(self, grid):
        grid2 = empty((5, 5), dtype=int8)
        for i in range(5):
            for x in range(5):
                if grid[i][x].the_piece_on_it == None:
                    grid2[i][x] = 0
                    continue
                value = 10 if grid[i][x].the_piece_on_it.color == "blue" else -10
                value *= 10 if grid[i][x].the_piece_on_it.king_or_not else 1
                grid2[i][x] = value
        return grid2

    def heuristic(self, grid):
        point = 0
        adjacent = ["nan", [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        sh = [0, 0]
        # piece values
        for i in range(5):
            for x in range(5):
                if grid[i][x] != 0:
                    point += grid[i][x]
                    adjacent[1 if grid[i][x] > 0 else -1][sh[0] if grid[i][x] > 0 else sh[1]] = i*10 + x + 11
        if point <= -20:
            return point
        jam = 0
        for n in range(-1, 2, 2):
            for z in adjacent[n]:
                connections = 0
                for i in range(-1, 2):
                    for x in range(-1, 2):
                        s = z + i*10 + x
                        if s in adjacent[n]:
                            connections += 1
                jam += (connections *
                        n)
        point += jam

        return point

    def minimax(self, grid, turn_, alpha, beta, depth):
        # we are searching in the board for the hexes that is not empty
        for i in range(5):
            for x in range(5):

                # checking the color of the piece to see is it set with the turn or not
                if grid[i][x] > 0 and turn_ > 0 or grid[i][x] < 0 and turn_ < 0:
                    hand_cards = [cards_info[0 if turn_ == -1 else 3][2], cards_info[1 if turn_ == -1 else 4][2]]

                    # we find the cards that is for the player turn and append them to 'hand_cards' list
                    for z in range(2):
                        # setting the card with the turn
                        h = z + 3 if turn_ == 1 else z

                        for y in hand_cards[z].moves:
                            # we have selected our piece and card
                            # now we are checking all options that selected card gives us
                            # the move that we are optimizing each time, is saved in the 'next_move' variable
                            next_move = i * 10 + x + y if turn_ == -1 else i * 10 + x + y * -1
                            # we check if the move is valid or not
                            if next_move // 10 >= 0 and next_move // 10 <= 4 and\
                               next_move % 10 >= 0 and next_move % 10 <= 4:
                                # our move destination which is in 'next_move' may be location of an own piece
                                if grid[next_move // 10][next_move % 10] > 0 and turn_ > 0 or grid[next_move // 10][next_move % 10] < 0 and turn_ < 0:
                                    continue
                                # we are ready to do move action. so we save the info of destination hex in 'a'
                                # variable to don't miss it
                                # we also change the cards
                                a = grid[next_move // 10][next_move % 10]
                                grid[next_move // 10][next_move % 10], grid[i][x] =\
                                grid[i][x], 0
                                cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]

                                # if we kill enemy's master or take his seat by our master, we win.
                                # we check this in 'win_or_not' function
                                if self.win_or_not(grid, turn_):
                                    grid[next_move // 10][next_move % 10], grid[i][x] = a, grid[next_move // 10][next_move % 10]
                                    cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]
                                    return [i * 10 + x, next_move, h, turn_ * 10000]

                                # our system can't go down more than 8 times so if our 'depth' variable is 8,
                                # we call our 'heuristic' function. it tells us how the position is.
                                # it just counts the number of pieces that every color has.
                                elif depth == 6:
                                    value = self.heuristic(grid)
                                    grid[next_move // 10][next_move % 10], grid[i][x] = a, grid[next_move // 10][next_move % 10]
                                    cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]
                                    return [i * 10 + x, next_move, h, value]

                                # alpha beta
                                else:
                                    value = self.minimax(grid, turn_ * -1,
                                                         alpha, beta, depth + 1)

                                    if turn_ == 1:
                                        if int(value[3]) >= int(alpha[3]):
                                            alpha = [i * 10 + x, next_move, h, value[3]]
                                        if int(alpha[3]) >= int(beta[3]):
                                            grid[next_move // 10][next_move % 10], grid[i][x] =\
                                                a, grid[next_move // 10][next_move % 10]
                                            cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]
                                            return [i * 10 + x, next_move, h, 10000]
                                    else:
                                        if int(value[3]) <= int(beta[3]):
                                            beta = [i * 10 + x, next_move, h, value[3]]
                                        if int(alpha[3]) >= int(beta[3]):
                                            grid[next_move // 10][next_move % 10], grid[i][x] = \
                                                a, grid[next_move // 10][next_move % 10]
                                            cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]
                                            return [i * 10 + x, next_move, h, -10000]

                                grid[next_move // 10][next_move % 10], grid[i][
                                    x] = a, grid[next_move // 10][
                                    next_move % 10]
                                cards_info[h][2], cards_info[2][2] = cards_info[2][2], cards_info[h][2]
        if turn_ == -1:
            return beta
        else:
            return alpha

# the most useful variables



# cards
cards = [Card('elephant', [-1, 1, 9, 11], 'red'),
         Card('tiger', [-10, 20], 'blue'),
         Card('dragon', [8, 12, -11, -9], 'red'),
         Card('monkey', [-11, -9, 9, 11], 'blue'),
         Card('frog', [11, 2, -11], 'red'),
         Card('horse', [10, -10, 1], 'blue'),
         Card('rooster', [1, -1, 11, -11], 'red'),
         Card('mantis', [-10, 9, 11], 'blue'),
         Card('ox', [-1, -10, 10], 'red'),
         Card('cobra', [1, -11, 9], 'blue'),
         Card('crab', [2, -2, 10], 'red'),
         Card('crane', [10, -9, -11], 'blue'),
         Card('eel', [-1, -9, 11], 'red'),
         Card('boar', [10, 1, -1], 'blue'),
         Card('rabbit', [-9, 9, -2], 'red')]


# make board and pieces
def make_board():
    board = []
    for y in range(5):
        board.append([])
        for x in range(5):
            if y == 0:
                board[-1].append(Hexes(Piece(True if x == 2 else False, "red", y * 10 + x, -100 if x == 2 else -10),
                                        y * 10 + x, False))
            elif y == 4:
                board[-1].append(Hexes(Piece(True if x == 2 else False, "blue", y * 10 + x, 100 if x == 2 else 10),
                                        y * 10 + x, False))
            else:
                board[-1].append(Hexes(None, y * 10 + x, False))
    return board


# choose 5 cards randomly
def choose_cards(cards_info):
    for i in range(5):
        chosen_card = random.choice(cards)
        cards.remove(chosen_card)
        cards_info[i][2] = chosen_card
    return cards_info


cards_info = [[50, 18, None], [300, 18, None], [491, 302, None], [50, 586, None], [300, 586, None]]



def menu_(volume):
    run = True
    while run:
        background_menu = pygame.image.load("background1.png")
        background_menu = pygame.transform.scale(background_menu, (1050,800))
        screen.blit(background_menu, (0, 0))

        # start button
        # pygame.draw.rect(screen, (255, 0, 255), (217, 100, 300, 100))
        Start = pygame.image.load("start-button.png")
        Start = pygame.transform.scale(Start, (350, 120))
        screen.blit(Start, (190, 130))
        # exit button
        # pygame.draw.rect(screen, (0, 255, 255), (217, 300, 300, 100))
        Exit = pygame.image.load("exit.png")
        Exit = pygame.transform.scale(Exit, (350, 150))
        screen.blit(Exit, (190, 250))
        # un pause
        # pygame.draw.rect(screen, (255, 255, 0), (217, 415, 30, 30))
        unpause = pygame.image.load("sound.png")
        unpause = pygame.transform.scale(unpause, (40, 40))
        screen.blit(unpause, (217, 415))
        # pause music
        # pygame.draw.rect(screen, (255, 0, 255), (262, 415, 30, 30))
        pause = pygame.image.load("audio.png")
        pause = pygame.transform.scale(pause, (40, 40))
        screen.blit(pause, (262, 415))
        # increase volume
        # pygame.draw.rect(screen, (0, 255, 255), (442, 415, 30, 30))
        inc = pygame.image.load("increase-volume (1).png")
        inc = pygame.transform.scale(inc, (40, 40))
        screen.blit(inc, (442, 415))
        # decrease volume
        # pygame.draw.rect(screen, (0, 255, 255), (485, 415, 30, 30))
        dec = pygame.image.load("minus.png")
        dec = pygame.transform.scale(dec, (40, 40))
        screen.blit(dec, (485, 415))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pos()
                if a[0] >= 217 and a[0] <= 517:
                    if a[1] >= 100 and a[1] <= 200:
                        # the start button clicked
                        return True

                    elif a[1] >= 300 and a[1] <= 400:
                        # the exit button clicked
                        return False

                    elif a[0] <= 247 and a[1] >= 415 and a[1] <= 445:
                        # the music started
                        pygame.mixer.music.unpause()

                    elif a[0] >= 262 and a[0] <= 292 and a[1] >= 415 and a[1] <= 445:
                        # the music paused
                        pygame.mixer.music.pause()

                    elif a[0] >= 442 and a[0] <= 472 and a[1] >= 415 and a[1] <= 445:
                        volume += 0.5
                        pygame.mixer.music.set_volume(volume)
                    elif a[0] >= 485 and a[1] >= 415 and a[1] <= 445:
                        volume -= 0.5
                        pygame.mixer.music.set_volume(volume)
            pygame.display.update()


def main():

    running = True
    turn = "red"
    selected_piece = -1
    selected_card = 0
    ai = Ai()
    pieces = make_board()
    while running:
        ai.graphic(selected_card, pieces)

        # events
        # all the actions in the game are processed with clicking on something, the important thing is location of clicking
        if turn == "red":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    a = pygame.mouse.get_pos()  # as a shortcut

                    # user has clicked on something in the board
                    if a[0] >= 50 and a[0] <= 450 and a[1] >= 156 and a[1] <= 556:
                        # getting location of click
                        location = [(pygame.mouse.get_pos()[1] - 156) // 80, (pygame.mouse.get_pos()[0] - 50) // 80]

                        # we handle the clicking
                        selected_piece = pieces[location[0]][location[1]].select(selected_piece, selected_card, turn, pieces)

                        # if a move was processed function returns -2
                        if selected_piece == -2:
                            # checking the end game condition
                            if ai.win_or_not(ai.get_data(pieces), 1 if turn == "blue" else -1):
                                running = False

                            # preparing for the next turn
                            turn = "blue" if turn == "red" else "red"  # turn changes
                            s = cards_info[2][2]
                            cards_info[2][2] = cards_info[selected_card][2]
                            cards_info[selected_card][2] = s
                            selected_card = 3 if turn == "blue" else 0  # selected card changes

                    elif a[0] >= 50 and a[0] <= 250 or a[0] >= 300 and a[0] <= 500:  # if a card was clicked
                        if turn == "red":  # if it is red's turn he isn't allowed to use blue's cards
                            if a[1] >= 18 and a[1] <= 138:
                                selected_card = a[0] // 250
                        elif turn == "blue":  # if it is blue's turn he isn't allowed to use red's cards
                            if a[1] >= 574 and a[1] <= 694:
                                selected_card = 3 + a[0] // 250
                        for m in pieces:  # when user selects new card, we have to clean the last selected hexes
                            for n in m:
                                n.is_showed_to_move = False
        else:
            move = ai.minimax(ai.get_data(pieces), 1, [0, 0, 0, -100000], [0, 0, 0, 100000], 1)
            print(move)

            # to make the AI move easy and use the same function that we use to move player pieces we have to do some change
            selected_card = int(move[2])
            pieces[move[1] // 10][move[1] % 10].is_showed_to_move = True
            selected_piece = pieces[move[1] // 10][move[1] % 10].select(move[0], selected_card, turn, pieces)

            # checking the end game condition
            if ai.win_or_not(ai.get_data(pieces), 1 if turn == "blue" else -1):
                running = False

            # preparing for the next turn
            turn = "blue" if turn == "red" else "red"  # turn changes
            s = cards_info[2][2]
            cards_info[2][2] = cards_info[selected_card][2]
            cards_info[selected_card][2] = s
            selected_card = 3 if turn == "blue" else 0  # selected card changes
        ai.graphic(selected_card, pieces)
        pygame.display.update()


def game_over():
    while True:
        screen.fill((100, 80, 50))
        Game = pygame.image.load("Game_Over.png")
        Game = pygame.transform.scale(Game, (1050, 800))
        screen.blit(Game,(0,0))
        # retry button
        retry = pygame.image.load("refresh.png")
        retry = pygame.transform.scale(retry,(100,100))
        screen.blit(retry,(200,552))
        #pygame.draw.rect(screen, (100, 100, 100), (146, 552, 75, 75))
        # exit button
        #pygame.draw.rect(screen, (100, 100, 100), (438, 552, 75, 75))
        e = pygame.image.load("moz.png")
        e = pygame.transform.scale(e,(100,100))
        screen.blit(e,(400,552))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = pygame.mouse.get_pos()
                if a[1] >= 552 and a[1] <= 627:
                    if a[0] >= 146 and a[0] <= 221:
                        return True
                    elif a[0] >= 438 and a[0] <= 513:
                        return False
        pygame.display.update()


volume = 5
running = menu_(volume)
while running:
    cards_info = choose_cards(cards_info)
    for i in cards_info:
        cards.append(i[2])
    main()
    running = game_over()



