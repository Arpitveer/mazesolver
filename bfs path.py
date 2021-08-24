import cv2
import numpy as np
import pygame
import sys
class tree:
    def __init__(self,n):
        self.node = n
        self.back = 0
        self.next = 0

    def make(self,b):
        self.back = b
        return self

    def setn(self, n):
        self.next = n
    def get(self):
        return self.node

class queue1:
    Q=[]
    c=0
    def __init__(self,a):
        self.Q.append(a)
    def pop(self):
        r=self.Q[self.c]
        self.c=self.c+1
        return r
    def append(self,a):
        self.Q.append(a)

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
color=[220,20,60]
xpos=start[0]
ypos=start[1]
pos=[ypos,xpos]
win.blit(imga,(0,0))
pygame.display.update()
mouse=[]

answer=[]

clock = pygame.time.Clock()
fps =50
testR={}
f=0
count=0
def draw(ans):
    global count,color
    count=count+10
    if (count%3==0):
      color[1]=(color[1]+10)%255
    if(count%7==0):
        color[0] = (color[0] + 10) % 255
    if(count%9==0):
        color[2] = (color[2] + 10) % 255
    pygame.draw.circle(win,color,ans,radius)
    pygame.display.update()
path=[start]
s=tree(start)

queue=queue1(s)
array=[[0,-4],[4,0],[-4,0],[0,4]]
next=s
while(f==0):
    #print(xpo,ypo,i)
    i=-1
    pointer=queue.pop()
    do=pointer.get()
    xpo,ypo=do
    print(do)
    while(i<3):
            i=i+1
            xpo1=xpo+array[i][0]
            ypo1=ypo+array[i][1]

            if(ypo1>=590 or xpo1>=475or ypo1<=0 or xpo1<=0):
                continue
            col=img[ypo1][xpo1]
            if(col<=100):
                continue
            if(xpo1==dist[0] and ypo1 ==dist[1]):#finish
                answer=pointer
                queue.append([xpo1, ypo1])
                f=1
                break
            if (col==0):#black
                continue

            if(col>100 and col<=255):#white
                draw([xpo1,ypo1])
                img[ypo1][xpo1]=100
                lp=tree([xpo1,ypo1])
                lp.make(pointer)
                next.next=lp
                next=lp
                queue.append(lp)



print("done")
pygame.draw.circle(win,color,start,4)
win.blit(imga,(0,0))
i=0
while(answer!=0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit the program.
            quit()
            # Draws the surface object to the screen.

    ans=answer.node
    draw(ans)
    answer=answer.back
    i=i+1
    pygame.display.update()


