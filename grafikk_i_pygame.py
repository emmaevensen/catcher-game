
#importerer nødvendige biblioteker
import pygame as pg
import sys, random

#lager et vindu/flate

# Konstanter
WIDTH = 400
HEIGHT = 600

#størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

#Frames per sekund (bilder per sekund)
FPS = 60

#Farger (RGB)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (152,152,152)
LIGHTBLUE = (140,160,255)

# Initiere pygame, starter pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

#variabel som styrer om spillet skal kjøres 
run = True

#Verdier for spilleren
w = 60 #bredde
h = 80 #høyde


#Startposisjon
x = WIDTH/2
y = HEIGHT-h-10

#Henter bilde til spilleren
player_img = pg.image.load('bucket.png')

#Henter bilde for bakgrunn
background_img = pg.image.load('background_snow_2-3.png')

#Tilpasser bakgrunnsbildet til vår skjermstørrelse
background_img = pg.transform.scale(background_img, SIZE)


# Henter font
font = pg.font.SysFont('Arial', 22) #tallet er størrelsen i pixler

points = 0
liv = 3

# Funksjon som viser antall poeng
def display_points():
    text_img = font.render(f"Antall poeng: {points}", True, WHITE)
    #metode som putter bilde oppå bilde, klistremerke
    surface.blit(text_img, (20,20))
    
def display_liv():
    text_liv = font.render(f"Antall liv: {liv}", True, WHITE)
    surface.blit(text_liv, (20,50))


class Ball:
    # konstruktør
    def __init__(self):
        self.radius = 10
        self.x = random.randint(self.radius,WIDTH-self.radius)
        self.y = -self.radius
        
    def update(self):
        self.y += 5
        
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x, self.y), self.radius)
        
        
# Lager et ball-objekt
ball = Ball()
    

#Spill-løkken
while run: #ubestemt hvor mange ganger den skal kjøre, hvor lenge man vil spille, derfor while
    #Sørger for at løkken kjører i korrekt hastighet
    clock.tick(FPS)
    
    #Går gjennom hendelser (events)
    for event in pg.event.get():
        #Sjekker om vi ønsker å lukke vinduet
        if event.type==pg.QUIT:
            run = False # Spillet skal avsluttes
    
    
    #Fyller skjermen med en farge
    #surface.fill(LIGHTBLUE)
            
    
    #Bruker bakgrunnsbildet
    surface.blit(background_img, (0,0)) #(0,0) er startkoordinatene 
    
    #Hastigheten til spilleren
    vx = 0
    
            
    #Henter knappene fra tastaturet som trykkes på
    keys = pg.key.get_pressed()
    
    # Sjekker om ulike taster trykkes på og endrer farge
    if keys[pg.K_LEFT]:
        vx = -5
    
    elif keys[pg.K_RIGHT]:
        vx = 5
        
    #Oppdaterer posisjonen til rektangelet
    x += vx
    
    #Sjekker kollisjon med venstre side av skjermen
    if  x <=0 :
        x=0
        y= HEIGHT - h
        
    #Sjekker kollisjon med høyre side av skjermen
    if x+w >= WIDTH:
        x = WIDTH-w
        y = HEIGHT - h
        
    # Ball
    ball.update()
    ball.draw()
    
    #Prøver å lage flere baller
    if ball.y == HEIGHT/2:
        ball2 = Ball()
    
  
    
    # Sjekker kollisjon
    if ball.y > y and x < ball.x < x+w:
        points += 1 #øker antall poeng
        ball = Ball()
        
    
    # Sjekker om vi ikke klarer å fange ballen
    if ball.y + ball.radius > HEIGHT:
        print("Du klarte ikke å fange ballen")
        liv -= 1
        if liv > 0:
            ball = Ball()
        else:
            print("Du mistet alle livene dine")
            print(f"Du fikk {points} poeng")
            run = False #Game over
    
    
    # Spiller
    #pg.draw.rect(surface, GREY, [x,y,w,h])
    
    #legger bilde på skjermen, hver gang den oppdateres endres posisjonen
    surface.blit(player_img,(x,y))
    
    # Tekst
    display_points()
    display_liv()
        
        
    #"Flipper" displayet for å vise hva vi har tegnet
    pg.display.flip()


#Avslutter pygame
pg.quit()
sys.exit()

    

