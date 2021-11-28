from pygame import*

#variables
surface_width = 900
surface_height = 700
ch_size = 90
border_left = 0
border_top = 0
border_right = surface_width - ch_size
border_bottom = surface_height - ch_size


#window
window = display.set_mode((surface_width, surface_height))
display.set_caption("Ping Pong")
clock = time.Clock()

#label
font.init()
font1 = font.SysFont("Arial", 40)
lose1 = font1.render("Player 1 lost!", True, (216, 41, 131))
lose2 = font1.render("Player 2 lost!", True, (216, 41, 131))

score1 = font1.render("Score: ", True, (127, 43, 250))
score2 = font1.render("Score: ", True, (127, 43, 250))

menu = font1.render("1.to play press SPACE", True, (127, 43, 250))
menu2 = font1.render("2.To go to the store, press M", True, (127, 43, 250))

item = font1.render("blue ball (to buy pr B)", True, (127, 43, 250))
item2 = font1.render("green background for game (to buy pr G)", True, (127, 43, 250))



#images
img_background = (173, 158, 215)                               #(171, 247, 224)
img_racket = "racket02.png"
img_ball = "tennis_ball02.png"
img_ball02 = "t_ball02.png"
img_background2 = (80, 223, 131)
img_background3 = (159, 230, 73)


#classes
 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, start_x, start_y, size, player_speed):
        super().__init__()
  
        self.image = transform.scale(image.load(player_image), (ch_size, ch_size))
        self.speed = player_speed
  
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Racket(GameSprite):
    def __init__(self, player_image, start_x, start_y, size, player_speed):
        super().__init__(player_image, start_x, start_y, size, player_speed)
 
    def right_update(self):
        k_pressed = key.get_pressed()
        if k_pressed[K_DOWN] and self.rect.y > 10 and self.rect.y < border_bottom:
            self.rect.y += self.speed

        if k_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        
    def left_update(self):
        k_pressed = key.get_pressed()
        if k_pressed[K_s] and self.rect.y > 10 and self.rect.y < border_bottom:
            self.rect.y += self.speed

        if k_pressed[K_w] and self.rect.y > 10:     #and self.rect.y < border_top
            self.rect.y -= self.speed


#characters
racket1 = Racket(img_racket, 40, 300, ch_size, 20)
racket2 = Racket(img_racket, 750, 300, ch_size, 20)
ball = GameSprite(img_ball, 400, 300, ch_size, 2)
ball02 = GameSprite(img_ball02, 400, 300, ch_size, 2)

x_speed = 5
y_speed = 5

score_l = 0
score_r = 0

run = True
finale = False
game_run = False
store = False
back_purchased = False
ball_purchased = False
#cycle 
while run:
    window.fill(img_background)
    window.blit(menu, (200, 300))
    window.blit(menu2, (200, 330))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif game_run == False and e.type == KEYDOWN:
            if e.key == K_SPACE:
                game_run = True
                
            elif store == False and e.type == KEYDOWN:
                if e.key == K_m:
                    store = True

    if store == True:
        window.fill(img_background2)
        window.blit(item, (10, 15))
        window.blit(item2, (10, 55))
        if back_purchased == False and e.type == KEYDOWN:
            if e.key == K_g:
                back_purchased = True
                
        elif ball_purchased == False and e.type == KEYDOWN:
            if e.key == K_b:
                ball_purchased = True

    if game_run == True:
        window.fill(img_background)
        racket1.reset()
        racket2.reset()
        racket1.left_update()
        racket2.right_update()
        ball.reset()
        window.blit(score1, (10, 15))
        window.blit(score2, (730, 15))

        if finale != True:
            racket1.left_update()
            racket2.right_update()

            ball.rect.x += x_speed
            ball.rect.y += y_speed
            

            if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                racket1.left_update()
                racket2.right_update()
                x_speed *= -1
                y_speed *= -1
                

            if ball.rect.y > border_bottom or ball.rect.y < 0:
                y_speed *= -1
                x_speed *= -1

            if ball.rect.x < border_left:
                #finale = True
                #window.blit(lose1, (300, 300))
                score_r += 1
                window.blit(score2, (730, 15))
                #run = False

            if ball.rect.x > border_right:
                #finale = True
                score_l += 1
                window.blit(score1, (10, 15))
                #run = False

            if score_l == 3:
                run = False
                window.blit(lose2, (300, 300))

            if score_r == 3:
                run = False
                window.blit(lose1, (300, 300))




        
    display.update()
    clock.tick(60)
