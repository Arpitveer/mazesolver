import cv2
import numpy as np
import pygame
import sys
img = cv2.imread('imposter_maze2.png', cv2.IMREAD_GRAYSCALE)
thresh = 128
img= cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
img=np.array(img)
sys.setrecursionlimit(10**6)
pygame.display.set_caption('mazesolver')
win=pygame.display.set_mode((475,590))
imga=pygame.image.load("imposter_maze2.png")
fanswer=[]
start=[415,589]
dist=[391,589]
radius=3
color=(220,20,60)
xpos=start[0]
ypos=start[1]
pos=[ypos,xpos]
win.blit(imga,(0,0))
pygame.display.update()
mouse=[]

answer=[]

clock = pygame.time.Clock()
fps =200
testR={}

def pathalgo(img1,xpo,ypo,dx,dy):

    global answer,fanswer

    if(ypo>=590 or xpo>=475or ypo<=0 or xpo<=0):
        return 0
    col=img1[ypo][xpo]

    if(img1[ypo][xpo]==100):
        return 0
    if(xpo==dist[0] and ypo ==dist[1]):#finish
        mylist = answer.copy()
        fanswer.append(mylist)
        print(fanswer)
        return 0
    if (col==0):#black
        return 0
    if(col==255):#white
        answer.append([xpo,ypo])
        img1[ypo][xpo]=100

    pathalgo(img1,xpo,ypo-4,0,-1)
    pathalgo(img1,xpo+4,ypo,1,0)
    pathalgo(img1,xpo-4,ypo,-1,0)
    pathalgo(img1,xpo,ypo+4,0,1)
    answer.pop()
    return 0
pygame.draw.circle(win,color,start,4)
def draw(ans):
    pygame.draw.circle(win,color,ans,radius)
    pygame.display.update()
pathalgo(img, xpos, ypos, 0, 0)
i=0
max=100000
print(fanswer)
for i in range(len(fanswer)):
    if (len(fanswer[i])<max):
        answer=fanswer[i]
print(answer)

i=0
while(i<len(answer)):
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit the program.
            quit()
            # Draws the surface object to the screen.

    ans=answer[i]
    draw(ans)
    i=i+1
    pygame.display.update()


