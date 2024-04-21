import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
Text_list = ["red","orange","yellow","green","blue","purple"]
text_font = pygame.font.SysFont("Times New Roman", 30)
text_font2 = pygame.font.SysFont("Times New Roman", 60)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Stroop Test")

# button image
stop_img = pygame.image.load("greyCheck.png").convert_alpha()
start_img = pygame.image.load("OrangeCheck.png").convert_alpha()

# button class
class Button():
    def __init__(self, x,y, image) -> None:
        self.image = pygame.transform.scale(image, (int(image.get_width()*3), int(image.get_height()*3)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def draw(self):
        inbox = False
        
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            inbox = True
        # draw button
        screen.blit(self.image,(int(SCREEN_WIDTH/2 - self.image.get_width()/2),self.rect.y))
        return inbox
    
    def change_img(self, image):
        self.image = pygame.transform.scale(image, (int(image.get_width()*3), int(image.get_height()*3)))


# create button
start_button = Button(275,300,start_img)

def draw_text(text, font, color, y):
    img = font.render(text, True, color);
    screen.blit(img, (int(SCREEN_WIDTH/2 - img.get_width()/2),y))
    

run = True
start_time = None
startPage = True
randomText = -1
time_string = ""
while run:

    if startPage:
        screen.fill((255,255,255))
        draw_text("HI!",text_font,(0,0,0) , 150)
        draw_text("To Start Press the Button",text_font,(0,0,0) , 175)
        start_button.draw()
        if time_string != "":
            draw_text("Time Taken: "+time_string,text_font,(0,0,0) , 10)
    else:
        screen.fill((245, 245, 245))
        # print color and text
        draw_text(Text_list[randomText],text_font2, (0,0,0) , 150)
        start_button.draw()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.draw():
                if start_time == None:
                    start_time = time.time()
                    startPage = False
                    start_button.change_img(stop_img)
                    time_string = ""
                    # randomize text and color
                    randomText = random.randint(0, 5)
                else:
                    time_string = str(time.time()-start_time)
                    start_time = None
                    startPage = True
                    start_button.change_img(start_img)
                    randomText = -1

        pygame.display.flip()


pygame.quit()