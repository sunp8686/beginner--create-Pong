import pygame, random
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Ball.png')
        self.rect = self.image.get_rect(center= (400, 300))
        self.ball_x, self.ball_y = -5* random.choice((-1,1)) , -7*random.choice((-1,1))
        self.active = False
        self.score_time = 0
    def ball_move(self):
        if self.active:
            self.rect.centerx += self.ball_x
            self.rect.centery -= self.ball_y
            self.ball_colli()
        else: self.time_counter()
    def ball_colli(self):
        if self.rect.top <=5 or self.rect.bottom >= 595:
            self.ball_y *= -1
        if self.rect.left <= -100 or self.rect.right >= width + 100:
            self.ball_x *= -1
        if player.rect.colliderect(ball.rect):
            print('colli')
            if abs(player.rect.right - ball.rect.left) < 15:
                self.ball_x *= -1
        if opponent.rect.colliderect(ball.rect):
            print('collo')
            if abs(ball.rect.right - opponent.rect.left) < 15:
                self.ball_x *= -1
    def reset_ball(self):
        self.score_time = pygame.time.get_ticks()
        self.rect.centerx , self.rect.centery = (400, 300)
        self.active = False
        self.ball_move()
    def time_counter(self):
        current_time = pygame.time.get_ticks()
        countdown = 3
        if current_time - self.score_time <= 700:
            countdown = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown = 1
        if current_time - self.score_time > 2100:
            self.active = True
        basic_font = pygame.font.Font(None, 35)
        time_counter = basic_font.render(str(countdown), True, (0, 0, 255))
        time_counter_rect = time_counter.get_rect(center= (300, 150))
        screen.blit(time_counter, time_counter_rect)
class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Paddle, self).__init__()
        self.image = pygame.image.load('Paddle.png')
        self.rect = self.image.get_rect(center= (pos_x, pos_y))
        self.pad_move = 20
    def pad_lim(self):
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > high:
            self.rect.bottom = 599
    def pad_move(self):
        self.rect.centery += 5
        if self.rect.top < 0:
            self.rect.centery *= -1
        if self.rect.bottom > high:
            self.rect.centery *= -1
class Score(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super(Score, self).__init__()
        self.font = pygame.font.Font('PoetsenOne-Regular.ttf', 40)
        self.point = 1
        self.image = pygame.draw.rect(screen, (0 , 255 , 0),(pos_x, pos_y, 5, high))
    def check_score(self):
        global player_score, opponent_score, can_score
        if player_score_line.colliderect(ball.rect) and can_score:
            opponent_score += self.point
            can_score = False
            ball.reset_ball()
        if ball.rect.colliderect(opponent_score_line) and can_score:
            player_score += self.point
            can_score = False
            ball.reset_ball()
        if ball.rect.colliderect(mid_line):
            can_score = True
        if player_score >=3 or opponent_score >= 3:
            player_score, opponent_score = 0, 0
            game_state().state = 'game_over'
            print(game_state().state)
        self.player_score_dis = self.font.render(f'{player_score}', False, (0, 255, 255))
        self.opponent_score_dis = self.font.render(f'{opponent_score}', False,(0, 255, 255))
        screen.blit(self.player_score_dis, (width/2 - 40, 270))
        screen.blit(self.opponent_score_dis, (width/2 + 15, 270))

class game_state():
    def __init__(self):
        #super().__init__()
        self.state = 'intro'
        self.intro_image = pygame.image.load('intro.png')
        self.intro_image_rect = self.intro_image.get_rect(center=(400, 300))
        self.gameov_image = pygame.image.load('gamov.png')
        self.gameov_image_rect = self.gameov_image.get_rect(center= (400, 300))
    def main_game(self):
        self.state = 'main_game'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.rect.centery -= player.pad_move
                if event.key == pygame.K_DOWN:
                    player.rect.centery += player.pad_move
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.rect.centery -= player.pad_move
                if event.key == pygame.K_DOWN:
                    player.rect.centery += player.pad_move
        screen.fill(WHITE)
        pygame.draw.rect(screen, (0, 0, 0), mid_line)
        pygame.draw.circle(screen,(0, 255, 0), center, 100, 5)
        ball_sprite.draw(screen)
        player_sprite.draw(screen)
        opponent_sprite.draw(screen)
        Score(0, 0).image
        Score(width-5, 0).image
        Score(0, 0).check_score()
        ball.ball_move()
        player.pad_lim()
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                self.state = 'main_game'
        print(self.state)
        screen.fill(WHITE)
        screen.blit(self.intro_image, self.intro_image_rect)

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 'main_game'
                    print(self.state)
        screen.fill((0 , 0 ,0))
        screen.blit(self.gameov_image, self.gameov_image_rect)
    def state_manager(self):
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'intro':
            self.intro()
        if self.state == 'game_over':
            self.game_over()
#Main:
pygame.init()
clock = pygame.time.Clock()
width, high = 800, 600
screen = pygame.display.set_mode((width, high))
WHITE = (255, 255, 255)
mid_line = (width/2-2, 0, 5, high)
center = (width/2, high/2)
#Sprite attr
#ball
ball_sprite = pygame.sprite.Group()
ball = Ball()
ball_sprite.add(ball)
#player
player_sprite = pygame.sprite.Group()
player = Paddle(15, 300)
player_sprite.add(player)
player_score_line = Score(0 ,0).image
#opponent
opponent_sprite = pygame.sprite.Group()
opponent = Paddle(width - 15, 300)
opponent_sprite.add(opponent)
opponent_score_line = Score(width-5 ,0).image
#score
can_score = False
player_score = 0
opponent_score = 0
while True:
    game_state().state_manager()
    pygame.display.flip()
    clock.tick(60)
