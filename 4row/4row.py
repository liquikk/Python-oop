import pygame

block_size = 105
WIDTH = block_size * 6
HEIGHT = block_size * 6
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Balls:

    def put_a_ball(arr, turn):
        x_pos, y_pos = pygame.mouse.get_pos()
        i = x_pos // block_size
        j = y_pos // block_size
        if arr[j][i] == 0:
            if turn % 2 == 0:
                arr[j][i] = "Player 1"
            else:
                arr[j][i] = "Player 2"
            turn += 1
        return turn

class Game:
    
    def get_field(game_over, arr):
        if not game_over:
            for row in range(6):
                for col in range(6):
                    color = WHITE
                    x = col * block_size
                    y = row * block_size
                    pygame.draw.circle(WIN,color, (x+block_size//2,y+block_size//2), (45))
                    if arr[row][col] == "Player 1":
                        pygame.draw.circle(WIN, RED, (x+block_size//2,y+block_size//2), (45))
                    elif arr[row][col] == "Player 2":
                        pygame.draw.circle(WIN, BLUE, (x+block_size//2,y+block_size//2), (45))

    def checker(arr, player):
        empty = 0
        for row in arr:
            empty += row.count(0)

        # vertical win 
        for i in range(6):
            for j in range(3):
                if arr[j][i] == player and arr[j+1][i] == player and arr[j+2][i] == player and arr[j+3][i] == player:
                    return (f'Победил {player}')

        # horizontal win
        for i in range(3):
            for j in range(6):
                if arr[j][i] == player and arr[j][i+1] == player and arr[j][i+2] == player and arr[j][i+3] == player:
                    return (f'Победил {player}')

        # diagonal win 1
        for i in range(3):
            for j in range(3):
                if arr[j][i] == player and arr[j+1][i+1] == player and arr[j+2][i+2] == player and arr[j+3][i+3] == player:
                    return (f'Победил {player}')

        # diagonal win 2
        for i in range(3):
            for j in range(3, 6):
                if arr[j][i] == player and arr[j-1][i+1] == player and arr[j-2][i+2] == player and arr[j-3][i+3] == player:
                    return (f'Победил {player}')
        if empty == 0:
            return 'Ничья'
        return False

    def start():
        arr = [[0]*6 for item in range(6)]
        turn = 0
        game_over = False
        run = True

        while run:
            Game.get_field(game_over, arr)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    turn = Balls.put_a_ball(arr, turn)

            if (turn-1) % 2 == 0:
                game_over = Game.checker(arr, "Player 1")
            else:
                game_over = Game.checker(arr, "Player 2")
            if game_over:
                WIN.fill(BLACK)
                font1 = pygame.font.SysFont('verdana', 70)
                font2 = pygame.font.SysFont('verdana', 25)
                text1 = font1.render(game_over, True, WHITE)
                text2 = font2.render("Нажмите ПКМ, чтобы начать новую игру", True, WHITE)

                text1_rect = text1.get_rect()
                text2_rect = text2.get_rect()

                text1_x = WIN.get_width() / 2 - text1_rect.width / 2
                text1_y = WIN.get_height() / 2 - text1_rect.height
                text2_x = WIN.get_width() / 2 - text2_rect.width / 2
                text2_y = WIN.get_height() / 2 + text2_rect.height 
                WIN.blit(text1, [text1_x, text1_y])
                WIN.blit(text2, [text2_x, text2_y])
                
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                            game_over = False
                            arr = [[0]*6 for i in range(6)]
                            turn = 0
                            WIN.fill(BLACK)
                    if event.type == pygame.QUIT:
                        run = False
                
            pygame.display.update()
        
pygame.init()
Game.start()
