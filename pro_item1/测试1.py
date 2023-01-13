import pygame
import sys
import time
import tempfile
from math import pi, sin, cos
from pygame.locals import *

pygame.init()
p2=1.57
p4=p2/2.0
#                        Edit these:
ax = [-2,2,0]
ay = [1.5,1.5,0]
fx = [-1,.99,.5]
fy = [.99,1,.49]
px = [0,p2,0]
py = [p4,0,0]
dd=0.00003
black=(0,0,0)               # Fore- and background colors
white=(255,255,255)
bg=black
fg=white
inc=0.04

width,height=1024,768       # Window size
aspect=width/height*1.0
yscale=120
xscale=yscale*aspect
d=1              # resolution

screen = pygame.display.set_mode((width,height))    # You can add FULLSCREEN as last parameter
screen.fill(bg)

t=0.0                       # angle for sin
first=True
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            restart=True
        elif event.type == KEYDOWN and event.key == K_s:
            pars="a,f,p(x,y)="+str(ax)+str(ay)+str(fx)+str(fy)+str(px)+str(py)
            myfont = pygame.font.SysFont("monospace", 15)
            label = myfont.render(pars, 1, (100,100,100))
            screen.blit(label, (100, height-15))
            tf=tempfile.NamedTemporaryFile(prefix='hg', suffix='.jpg', dir ='.', delete=False)
            pygame.image.save(screen, tf.name)
                            # calculate next x,y point along line
    x = xscale * d * (ax[0]*sin(t * fx[0] + px[0]) +
                      ax[1]*sin(t * fx[1] + px[1]) +
                      ax[2]*sin(t * fx[2] + px[2])) + width/2
    y = yscale * d * (ay[0]*cos(t * fy[0] + py[0]) +
                      ay[1]*cos(t * fy[1] + py[1]) +
                      ay[2]*cos(t * fy[2] + py[2])) + height/2

    d = d - dd

    if not first:           # ignore any complaint about prev_x,y being undefined
        pygame.draw.aaline(screen, fg, (x, y), (prev_x, prev_y), 2)
    else:
        first=False

    prev_x = x              # save x,y for next line segment start
    prev_y = y

    pygame.display.update()
    t+=inc                  # increment angle for sin