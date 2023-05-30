import pygame, sys, math
from random import randint
from math import sin, cos, radians, pi

pygame.init()
pygame.font.init()
wn = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
direction = 1

az = randint(-2,2)
ae = randint(-2,2)

dz = 1
de = 1
dx = 1
dy = 1
dd = randint(-5,2)

BLUE=(0,0,255)

x = 210
y = 230
z = 280
e = 290

theta1 = 90
dtheta = 2

distance1 = randint(40,50)
radius = 20

state = True
time_since_velocity_change = 0

def point_pos(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)

while state:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      state = False
  pygame.display.update()
  ring = pygame.draw.rect(wn,(100,100,100),(50,50,400,400))
  (x2, y2) = point_pos(z, e, distance1, theta1)
  if (x2 > 430):
    x2 = 430
    dtheta = 0
    dz = abs(dz) * -1;
  if (x2 < 70):
    dz = abs(dz)
    dtheta = 0
    x2 = 70
  if (y2 > 430):
    de = abs(de) * -1;
    y2 = 430
  if (y2 < 70):
    de = abs(de)
    dtheta = 0
    y2 = 70 
  
  pygame.draw.line(wn, BLUE, (z, e), (x2, y2)) 
 
  topright = pygame.draw.line(wn, (255, 200, 0), (250,50), (450, 250)) 
  topleft = pygame.draw.line(wn, (255, 200, 0), (250,50), (50, 250)) 
  bottomleft = pygame.draw.line(wn, (255, 200, 0), (50, 250), (250,450)) 
  bottomright = pygame.draw.line(wn, (255, 200, 0), (250,450), (450, 250)) 
 
  a = pygame.draw.circle(wn, (255,255,255), (x2, y2), radius)
  b = pygame.draw.circle(wn, (0,0,0), (z, e), radius)

  time_since_velocity_change += 60
  clock.tick(60)
  

  z += dz
  e += de
  
  theta1 += dtheta
  distance1 += dd
  
  if (distance1 > 200):
    distance1 = 200
  if (distance1 < -200):
    distance1 = -200
  
  if (z > 430):
    dz *= -1
    z = 430
  if (z < 70):
    dz *= -1
    z = 70
  if (e > 430):
    de *= -1
    e = 430
  if (e < 70):
    de *= -1
    e = 70 
  
  if (time_since_velocity_change > 5000):
    time_since_velocity_change = 0
    dz = randint(1, 5)
    de = randint(1, 5)
    dtheta = randint(-2, 2)
    dd = randint(-2,2)
  
  if (distance1 < 40 and distance1 > -40):
      if (distance1 < 0):
       distance1 = -40
      else:
       distance1 = 40
  textfordistance = 'Distance between boxers:'
  print(textfordistance, distance1)
  
  movementOfDefender = pygame.draw.line(wn, (250,100,100), (z, e), ((z+(20*dz)), (e+(20*de))))
  pygame.draw.line(wn, (250,150,100), (x2, y2), ((z+(20*dz)), (e+(20*de))))
  print('White Dot: (',round(x2),',',round(y2),')',)
  print('Black Dot: (',z,',',e,')',)
  
  alpha = math.sqrt((y2 - (e+(20*de)))**2 + (x2 - (z+(20*dz)))**2)
  beta = math.sqrt((20*de)**2 + (20*dz)**2)
  lambda1 = distance1
  
  AngleB = (alpha**2 + lambda1**2 - beta**2)/(2*alpha*lambda1)
  AngleL = (alpha**2 + beta**2 - lambda1**2)/(2*alpha*beta)
  AngleA = (beta**2 + lambda1**2 - alpha**2)/(2*lambda1*beta)
  print("Beta:",beta,"Lambda:", lambda1, "Alpha:", alpha)
  if (beta + lambda1 > alpha and lambda1 + alpha > beta and alpha + beta > lambda1):
    AngleB = math.acos(AngleB)
    AngleL = math.acos(AngleL)
    AngleA = math.acos(AngleA)
    print("Angles ->","A:", round(AngleA * 360 / (2 * math.pi)), "B:", round(AngleB* 360 / (2 * math.pi)), "L:", round(AngleL* 360 / (2 * math.pi)) )










'''collidetopright = topright.collidepoint((x2,y2))
  collidetopleft = topleft.collidepoint((x2,y2))
  collidebottomright = bottomright.collidepoint((x2,y2))
  collidebottomleft = bottomleft.collidepoint((x2,y2))
  
  if collidetopright or collidetopleft or collidebottomleft or collidebottomright and (abs(x2) < abs(z) and abs(y2) < abs(e)) and (distance1 < 30):
    pygame.draw.line(wn, (255, 255, 255), (x2, y2), (450, 250))'''
"""
  if ( -1 <= AngleB <= 1)  or (-1 <= AngleL <=1) or (-1 <= AngleA <= 1):
    AngleB = math.acos(AngleB)
    AngleL = math.acos(AngleL)
    AngleA = math.acos(AngleA)
    print("Sides ->","Alpha:", alpha, "Beta:", beta, "Lambda:", lambda1)
    print("Angles ->","A:", round(AngleA), "B:", round(AngleB), "L:", round(AngleL) )
  elif ( 1 <= AngleB  or (1 <= (alpha**2 + beta**2 - lambda1**2)/(2*alpha*beta)) or (1 <= (beta**2 + lambda1**2 - alpha**2)/(2*lambda1*beta)):
    AngleB = math.acos(AngleB -1)
    AngleL = math.acos(((alpha**2 + beta**2 - lambda1**2)/(2*alpha*beta)) -1)
    AngleA = math.acos(((beta**2 + lambda1**2 - alpha**2)/(2*lambda1*beta)) -1)
    print("Sides ->","Alpha:", alpha, "Beta:", beta, "Lambda:", lambda1)
    print("Angles ->","A:", round(AngleA), "B:", round(AngleB), "L:", round(AngleL))
  else:
    AngleB = math.acos(((alpha**2 + lambda1**2 - beta**2)/(2*alpha*lambda1)) +1)
    AngleL = math.acos(((alpha**2 + beta**2 - lambda1**2)/(2*alpha*beta)) +1)
    AngleA = math.acos(((beta**2 + lambda1**2 - alpha**2)/(2*lambda1*beta)) +1)
    print("Sides ->","Alpha:", alpha, "Beta:", beta, "Lambda:", lambda1)
    print("Angles ->","A:", round(AngleA), "B:", round(AngleB), "L:", round(AngleL))    

  leftWall = pygame.draw.line(wn, (250,200,100), (0, 0), (0,500))
  topWall = pygame.draw.line(wn, (250,200,100), (0, 0), (500,0))
  rightWall = pygame.draw.line(wn, (250,200,100), (500, 0), (500,500))
  bottomWall = pygame.draw.line(wn, (250,200,100), (0, 500), (500,500))
  
  font = pygame.font.SysFont(None, 36)
  img = font.render(str(x2), True, BLUE)
  wn.blit(img, (20, 20))
  font.update()
  wn.blit(img, (20, 20))'''

 class Label():
    def __init__(self, txt, location, size=(160,30), bg=(255,255,255), fg=(0,255,0), font_name=None, font_size=12):
        self.bg = bg  
        self.fg = fg
        self.size = size

        self.font = pygame.font.Font(None, 36)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(topleft=location) 



    def draw(self, wn):
        wn.blit(self.surface, self.rect)


    def update(self):
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)

  x2Label = Label((str(x2), (20,20),(160,30), (255,255,255), (0,255,0), None, 12))
  x2Label.update()'''


  #slopeOfDefenderLine = e/z
  #yIntOfDefenderLine = 
#surface = pygame.Surface((50 , 50))

  #if blue dot coords intersect w a red line -> if coord of black have larger magnitude than blue -> draw 2 45 deg lines from point of intersection between blue dot and line of red square
  """