import pygame

pygame.init()

WIDTH, HEIGHT =  800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAMAGOTCHI _pre-alpha_")

sadness_speed= 1 / 3
hunger_speed= 1 / 5
FEED_POINTS = 5
PLAY_POINTS = 3

font1 = pygame.font.SysFont(None, 30)
sad1 = font1.render('Мне скучно', True, (0, 0, 0))
sad2 = font1.render('Мне грустно, поиграй со мной', True, (0, 0, 0))
hungry1 = font1.render('Кажется я проголодался', True, (0, 0, 0))
hungry2 = font1.render('Я сильно голоден, покорми меня', True, (0, 0, 0))
dead = font1.render('Питомец умер', True, (0, 0, 0))


saciety_bar = font1.render('Сытость', True, (0, 0, 0))
happiness_bar = font1.render('Счастье', True, (0, 0, 0))

feed_msg = font1.render('Покормить', True, (0, 0, 0))
play_msg = font1.render('Поиграть', True, (0, 0, 0))

class Pet:

    def __init__(self, image = pygame.image.load('pet.png'), satiety=100, happiness=100, alive=True):
        self.satiety = satiety
        self.satiety_max = satiety
        self.hunger_speed = hunger_speed
        self.happiness = happiness
        self.happiness_max = happiness
        self.sadness_speed = sadness_speed  
        self.image = pygame.transform.scale(image, (250, 250))
        self.alive = alive
        self.cover = pygame.transform.scale(pygame.image.load('cover.png'), (200, 150))

    def feed(self):
        if self.alive:
            if self.satiety + FEED_POINTS >= self.satiety_max:
                self.satiety = self.satiety_max
            else:
                self.satiety += FEED_POINTS

    def play(self):
        if self.alive:
            if self.happiness + PLAY_POINTS > self.happiness_max:
                self.happiness = self.happiness_max
            else:
                self.happiness += PLAY_POINTS
    
    def hunger(self):
        if self.alive:
            if self.satiety > 0:
                self.satiety -= self.hunger_speed
            else:
                self.alive = False

    def sadness(self):
        if self.alive:
            if self.happiness > 0:
                self.happiness -= self.sadness_speed
            else:
                self.alive = False

    def status_check(self):
        if self.alive:
            if self.happiness <= 30:
                textRect = sad2.get_rect()
                textRect.center = (WIDTH/2, 50)
                WIN.blit(sad2, textRect)
            elif self.happiness <= 50:
                textRect = sad1.get_rect()
                textRect.center = (WIDTH/2, 50)
                WIN.blit(sad1, textRect)
            elif self.satiety <= 20:
                textRect = hungry2.get_rect()
                textRect.center = (WIDTH/2, 50)
                WIN.blit(hungry2, textRect)
            elif self.satiety <= 50:
                textRect = hungry1.get_rect()
                textRect.center = (WIDTH/2, 50)
                WIN.blit(hungry1, textRect)
        else:
            textRect = dead.get_rect()
            textRect.center = (WIDTH/2, 50)
            WIN.blit(dead, textRect)
            self.cover = pygame.transform.scale(self.cover, (0, 0))
            self.image = pygame.transform.scale(pygame.image.load('dead.png'), (250, 250))

    def status_bars(self):

        textRect = saciety_bar.get_rect()
        textRect.center = (700, 75)
        WIN.blit(saciety_bar, textRect)

        if self.satiety > 70:
            satiety_color = (0, 255, 0)
        elif self.satiety > 40:
            satiety_color = (255, 165, 0)
        else:
            satiety_color = (255, 0, 0)

        textRect = happiness_bar.get_rect()
        textRect.center = (100, 75)
        WIN.blit(happiness_bar, textRect)

        if self.happiness > 70:
            happiness_color = (0, 255, 0)
        elif self.happiness > 40:
            happiness_color = (255, 165, 0)
        else:
            happiness_color = (255, 0, 0)

        pygame.draw.rect(WIN, satiety_color, (650, 100, self.satiety, 30))
        pygame.draw.rect(WIN, (0, 0, 0), (648, 98, 104, 34), 2)

        pygame.draw.rect(WIN, happiness_color, (50, 100, self.happiness, 30))
        pygame.draw.rect(WIN, (0, 0, 0), (48, 98, 104, 34), 2)

class Button():

    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.active_clr = (23, 204, 58)
        self.inactive_clr = (13, 162, 58)

    def draw(self, x, y, msg, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x +self.width and y < mouse[1] < y +self.height:
                pygame.draw.rect(WIN, self.active_clr, (x, y, self.width, self.height))
                if click[0] == 1 and action is not None:
                    action()
        else:
            pygame.draw.rect(WIN, self.inactive_clr, (x, y, self.width, self.height))                    

        
        textRect = msg.get_rect()
        textRect.center = (x + self.width/2, y + self.height/2)
        WIN.blit(msg, textRect)


def game():
    w_btn = 200
    h_btn = 50
    run = True
    clock = pygame.time.Clock()
    bobik = Pet()
    feed = Button(w_btn, h_btn)
    play = Button(w_btn, h_btn)

    while run:
        clock.tick(20)
        WIN.fill((255,228,205))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.blit(bobik.cover, (WIDTH/2 - 100, HEIGHT/2-75))
        WIN.blit(bobik.image, (WIDTH/2 - 125, HEIGHT/2-200))

        feed.draw(425, 450, feed_msg, bobik.feed)
        play.draw(175, 450, play_msg, bobik.play)

        bobik.status_bars()
        bobik.hunger()
        bobik.sadness()
        bobik.status_check()
        pygame.display.update()
    pygame.quit()

game()