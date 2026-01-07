# Name: Samarvir Garg
# Date: June 17, 2024
# Course Code: ICS3U1-01
# Discription: Final Summative Game - Wood Collector

# the following code will always put the screen in the top corner
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0,0)

import random
from pygame import * 

init()  # Initializing Pygame
size = width, height = 1000, 700  # defining the size of screen
screen = display.set_mode(size)

#defining all colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE=(160, 32, 240)
DARK_GREEN=(1,50,32)
LEAFGREEN=(108,143,15)
BROWN=(150,75,0)
YELLOW=(255,255,0)
SPACEBLUE=(29, 41, 81)
LIGHTBLUE=(152, 193, 217)


# define fonts
menuFont = font.SysFont("Times New Roman",60)
menuFont1 = font.SysFont("Times New Roman",30)
menuFont2 = font.SysFont("Times New Roman",20)

#states in the Game
STATE_MENU = 0
STATE_GAME = 1
STATE_INSTRUCTIONS = 2
STATE_QUIT = 3

blockWidth = width//3 # Defining the width of the block
blockHeight = height//9   # defining the height of the block

#Defining all the buttons
backbutton= Rect(5,5,80,40)
restartgamebutton=Rect(780,550,200,40)
backfromgamebutton=Rect(780,600,200,40)
yesbutton=Rect(350,400,200,50)
nobutton=Rect(350,500,200,50)
restartbutton=Rect(350,400,300,50)
backtomenubutton=Rect(350,500,300,50)

# defining all images
BackgroundPic = image.load("menu-background.png")
woodcollector=image.load("wood-collector.png")
lumberjack=image.load("lumberjack.png")
net=image.load("net.png")  
logofwood=image.load("log-wood.png")
wood=image.load("wood.png")
collector=image.load("collector.png")
frame=image.load("frame.png")
scoreboard=image.load("scoreboard.png")
mistakeboard=image.load("mistakeboard.png")

# Transforming the scales of all images to required
BackgroundPic = transform.scale(BackgroundPic,(1000,700))
woodcollector = transform.scale(woodcollector,(2*blockWidth,3*blockHeight))
lumberjack = transform.scale(lumberjack,(200,180)) 
net = transform.scale(net,(150,50)) 
logofwood = transform.scale(logofwood,(70,70))
wood=transform.scale(wood,(150,70))
collector=transform.scale(collector,(200,100))
frame=transform.scale(frame,(240,180))
scoreboard=transform.scale(scoreboard,(300,300))
mistakeboard=transform.scale(mistakeboard,(240,250))

# Defining all sounds
positive=mixer.Sound("positive.mp3")
negative=mixer.Sound("negative.mp3")

#  Function to draw a tree    
def tree(x,y):
    draw.circle(screen,DARK_GREEN,(x-5, y-15),40)
    draw.circle(screen,DARK_GREEN,(x+45, y-15),40)
    draw.circle(screen,DARK_GREEN,(x+25, y-40),40)
    draw.rect(screen,BROWN,(x,y,40,120))

# Function to draw a flower    
def flower(color,x,y):
    draw.rect(screen,DARK_GREEN,(x,y,5,20))
    draw.circle(screen,color,(x-2.5,y),6)
    draw.circle(screen,color,(x+7.5,y),6)
    draw.circle(screen,color,(x-2.5,y-7.5),6)
    draw.circle(screen,color,(x+7.5,y-7.5),6)
    draw.circle(screen,YELLOW,(x+2.5,y-4),5)

# Function to display the dropbox when user clicks on restart button while playing    
def restartpage():
    mx2=0
    my2=0
    while True:
        button2 = 0
        for e in event.get():             # checks all events that happen
            if e.type == QUIT:
                running = False
            if e.type == MOUSEBUTTONDOWN:
                mx2, my2 = e.pos          
                button2 = e.button
            elif e.type == MOUSEMOTION:
                mx2, my2 = e.pos 
                
            # Display all fonts,texts,color   
            draw.rect(screen,SPACEBLUE,(150,200,600,500),0,10)  
            draw.rect(screen,LIGHTBLUE,(150,200,600,500),10,10)
            draw.rect(screen,WHITE,(350,400,200,50),0,10)
            draw.rect(screen,WHITE,(350,500,200,50),0,10)
            question=menuFont1.render("Do you want to restart the game ?",True,WHITE)
            screen.blit(question,(230,300))
            yes=menuFont1.render("Yes",True,BLACK)
            no=menuFont1.render("Resume Game",True,BLACK)
            screen.blit(yes,(425,410))
            screen.blit(no,(360,505))
            
            if yesbutton.collidepoint(mx2,my2):    # Checks if user hover over the yes button
                draw.rect(screen,LIGHTBLUE,(350,400,200,50),5,10)
                if button2==1: # Checks if user clicks on yes button
                    state=drawGame()  # starts the main game
                    return state
                
            if nobutton.collidepoint(mx2,my2): # Checks if user hover over the no button
                draw.rect(screen,LIGHTBLUE,(350,500,200,50),5,10)
                if button2==1: # Checks if user clicks on no button
                    status="continue" # defined a new variable that will be used to continue the game from the same point
                    return status
            display.flip()
 
# Function to display the dropbox when user clicks on back button while playing  
def backpage():
    mx2=0
    my2=0
    while True:
        button2 = 0
        for e in event.get():             # checks all events that happen
            if e.type == QUIT:
                running = False
            if e.type == MOUSEBUTTONDOWN:
                mx2, my2 = e.pos          
                button2 = e.button
            elif e.type == MOUSEMOTION:
                mx2, my2 = e.pos          
            
            # Display all fonts,color,text.
            draw.rect(screen,SPACEBLUE,(150,200,600,500),0,10)
            draw.rect(screen,LIGHTBLUE,(150,200,600,500),10,10)
            draw.rect(screen,WHITE,(350,400,200,50),0,10)
            draw.rect(screen,WHITE,(350,500,200,50),0,10)
            question=menuFont1.render("Do you want to go back to main menu ?",True,WHITE)
            screen.blit(question,(230,300))
            yes=menuFont1.render("Yes",True,BLACK)
            no=menuFont1.render("Resume game",True,BLACK)
            screen.blit(yes,(425,410))
            screen.blit(no,(360,505))
            
            if yesbutton.collidepoint(mx2,my2): # Checks if user hover over the yes button
                draw.rect(screen,LIGHTBLUE,(350,400,200,50),5,10)
                if button2==1: # Checks if user clicks on yes button
                    state=STATE_MENU # sets the state to Menu state
                    return state
                
            if nobutton.collidepoint(mx2,my2): # Checks if user hover over the no button
                draw.rect(screen,LIGHTBLUE,(350,500,200,50),5,10)
                if button2==1: # Checks if user clicks on no button
                    status="continue"  # defined a new variable that will be used to continue the game from the same point
                    return status
            display.flip()

# Function to display a page when user losses            
def losepage():
    mx3=0
    my3=0
    while True:
        button3 = 0
        for e in event.get():             # checks all events that happen
            if e.type == QUIT:
                running = False
            if e.type == MOUSEBUTTONDOWN:
                mx3, my3 = e.pos          
                button3 = e.button
            elif e.type == MOUSEMOTION:
                mx3, my3 = e.pos
        
        #Display all text and images
        screen.fill(SPACEBLUE)
        draw.rect(screen,LIGHTBLUE,(0,0,1000,700),10)
        message=menuFont.render("AHH! YOU LOSE",True,WHITE)
        screen.blit(message,(250,50))
        message2=menuFont1.render("The evil lumberjack wins in his intensions. You are not able to collect sufficient",1,WHITE)
        screen.blit(message2,(30,200))
        message3=menuFont1.render("logs of wood. You should score 60 points before missing 15 logs of wood",1,WHITE)
        screen.blit(message3,(30,240))
        message4=menuFont1.render("to save the world from global warming.",1,WHITE)
        screen.blit(message4,(30,280))
        draw.rect(screen,WHITE,(350,400,300,50),0,10)
        draw.rect(screen,WHITE,(350,500,300,50),0,10)
        restart=menuFont1.render("Restart Game",1,BLACK)
        back=menuFont1.render("Go to Main Menu",1,BLACK)
        screen.blit(restart,(420,410))
        screen.blit(back,(400,510))
        
        if restartbutton.collidepoint(mx3,my3): # Checks if user hover over the restart button
            draw.rect(screen,LIGHTBLUE,(350,400,300,50),3,10)
            if button3==1: # Checks if user clicks on restart button
                state=drawGame() # starts the game again
                return state
        
        if backtomenubutton.collidepoint(mx3,my3): # Checks if user hover over the back button
            draw.rect(screen,LIGHTBLUE,(350,500,300,50),3,10)
            if button3==1: # Checks if user clicks on back button
                state=STATE_MENU # sets the state to menu state
                return state
        display.flip()            
 
# Function to display the page if user wins th game   
def winpage():
    mx3=0
    my3=0
    while True:
        button3 = 0
        for e in event.get():             # checks all events that happen
            if e.type == QUIT:
                running = False
            if e.type == MOUSEBUTTONDOWN:
                mx3, my3 = e.pos          
                button3 = e.button
            elif e.type == MOUSEMOTION:
                mx3, my3 = e.pos          

        # Display all texts, fonts, and images
        screen.fill(SPACEBLUE)
        draw.rect(screen,LIGHTBLUE,(0,0,1000,700),10)
        message=menuFont.render("YEAH! YOU WIN",True,WHITE)
        screen.blit(message,(250,50))
        message2=menuFont1.render("The evil lumberjack did not win in his intensions. You are able to collect ",1,WHITE)
        screen.blit(message2,(30,200))
        message3=menuFont1.render("sufficient logs of wood. You scored 60 points before missing 15 logs of wood ",1,WHITE)
        screen.blit(message3,(30,240))
        message4=menuFont1.render("and you saved the world from global warming.",1,WHITE)
        screen.blit(message4,(30,280))
        draw.rect(screen,WHITE,(350,400,300,50),0,10)
        draw.rect(screen,WHITE,(350,500,300,50),0,10)
        restart=menuFont1.render("Restart Game",1,BLACK)
        back=menuFont1.render("Go to Main Menu",1,BLACK)
        screen.blit(restart,(420,410))
        screen.blit(back,(400,510))

        if restartbutton.collidepoint(mx3,my3): # Checks if user hover over the restarts button
            draw.rect(screen,LIGHTBLUE,(350,400,300,50),3,10)
            if button3==1: # Checks if user clicks on retart button
                state=drawGame() # Starts the game again
                return state

        if backtomenubutton.collidepoint(mx3,my3): # Checks if user hover over the back button
            draw.rect(screen,LIGHTBLUE,(350,500,300,50),3,10)
            if button3==1: # Checks if user clicks on back button
                state=STATE_MENU # sets the state to menu state
                return state
        display.flip()    
    
    
# Function to display the main menu
def drawMenu(screen, button, mx, my, state):
    rectList = [Rect(blockWidth, 3*blockHeight, blockWidth, blockHeight), # game choice  # Defining the rectangles for all buttons
                Rect(blockWidth, 5*blockHeight, blockWidth, blockHeight), #help choice
                Rect(blockWidth, 7*blockHeight, blockWidth, blockHeight)] # quite choice
    stateList = [STATE_GAME, STATE_INSTRUCTIONS, STATE_QUIT] # Defining all the states
    titleList = ["Play Game", "Instructions", "Quit Game"] # defining all the titles
    screen.blit(BackgroundPic,(0,0,1000,700))
    screen.blit(woodcollector,(2*blockWidth-480,3*blockHeight-200))   
    for i in range(len(rectList)):
        rect = rectList[i] # get the current Rect
        draw.rect(screen, GREEN, rect)  # draw the Rect
        text = menuFont.render(titleList[i],1,BLACK)	# make the font
        textWidth, textHeight = menuFont.size(titleList[i]) # get the font size
        useW = (blockWidth - textWidth)//2  #use for centering
        useH = (blockHeight - textHeight)//2
        # getting a centered Rectangle
        textRect = Rect(rect[0] + useW, rect[1] + useH, textWidth, textHeight)
        screen.blit(text, textRect)	# draw to screen
        if rect.collidepoint(mx, my):
            draw.rect(screen, BLACK, rect, 2)
            if button == 1:
                state = stateList[i]
    return state

# Run the Game
def drawGame():
    
    # Defining all the variable that control the functioning of the game
    y1=210
    y2=320
    y3=430
    y4=540
    x1=550
    x2=300
    x3=50
    w1=0
    movement="left"
    PRESS_RIGHT = False
    PRESS_LEFT = False
    moveRate=15
    shipX = 0 
    woodincolumn1="no"
    speed1=0
    woodincolumn2="no"
    speed2=0
    woodincolumn3="no"
    speed3=0  
    score=0
    mistake=15
    mx1=0
    my1=0
    button1=0
    
    while True:
        for e in event.get():   # checks all event in the game
            if e.type == QUIT:
                running = False
    
            if e.type == MOUSEBUTTONDOWN:
                mx1, my1 = e.pos          
                button1 = e.button
            elif e.type == MOUSEMOTION:
                mx1, my1 = e.pos
    
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    PRESS_RIGHT = True
                if e.key == K_LEFT:
                    PRESS_LEFT = True 
                if e.key == K_UP:
                    PRESS_UP = True
                if e.key == K_DOWN:
                    PRESS_DOWN = True   
            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    PRESS_RIGHT = False
                if e.key == K_LEFT:
                    PRESS_LEFT = False 
                if e.key == K_UP:
                    PRESS_UP = False
                if e.key == K_DOWN:
                    PRESS_DOWN = False
                    
        # for net movement
        if PRESS_RIGHT == True:
            shipX += moveRate
            if shipX>700:
                shipX-=moveRate
        if PRESS_LEFT == True:
            shipX -= moveRate 
            if shipX<-100:
                shipX+=moveRate
                
        catchnet=Rect(shipX+10,680,70,20)  # Defining the rectangle for the net
        
        # Display all text,fonts,images
        draw.rect(screen, GREEN, (0, 0, width, height))
        draw.line(screen,BLACK,(250,0),(250,700))
        draw.line(screen,BLACK,(500,0),(500,700))
        draw.line(screen,BLACK,(750,0),(750,700))
        draw.line(screen,BLACK,(0,200),(750,200))
        flower(WHITE,10,y1)
        flower(WHITE,735,y1)
        flower(BLUE,10,y2)
        flower(BLUE,735,y2)
        flower(WHITE,10,y3)
        flower(WHITE,735,y3)
        flower(BLUE,10,y4)
        flower(BLUE,735,y4)
        screen.blit(net,(shipX,670,50,20))  
        draw.rect(screen,PURPLE, (750,0,250,700))
        draw.rect(screen,BLUE,backfromgamebutton,0,10)
        draw.rect(screen,RED,restartgamebutton,0,10)
        restart=menuFont1.render("Restart",1,WHITE)
        back=menuFont1.render("Back",1,WHITE)
        screen.blit(restart,(830,552))
        screen.blit(back,(840,602))
        screen.blit(lumberjack,(x1,75,100,50))
        screen.blit(lumberjack,(x2,75,100,50))
        screen.blit(lumberjack,(x3,75,100,50))
        screen.blit(frame,(755,10))
        screen.blit(wood,(800,30))
        screen.blit(collector,(770,80))
        screen.blit(scoreboard,(727.5,140))
        draw.rect(screen,LEAFGREEN,(785,270,170,85),0,20)
        screen.blit(mistakeboard,(750,350))
        tree(350,80)
        tree(100,80)
        tree(600,80)
        gamescore = menuFont.render(str(score),True,WHITE)
        if score>=10:
            screen.blit(gamescore,(845,280)) 
        else:
            screen.blit(gamescore,(855,280)) 
        mistale_allowed=menuFont2.render("Mistakes allowed :",True,BLACK)
        screen.blit(mistale_allowed,(780,415))
        mistakescore=menuFont.render(str(mistake),True,BLACK)
        screen.blit(mistakescore,(840,435))        
                           
        if woodincolumn1=="no":   # Checks if there is wood in column 1 or not
            woodincolumn1=random.choice(["yes","no","no","no"])  # If not, randomly decides if there should be wood or not after each loop
            if woodincolumn1=="yes": 
                w1=150 # resets the y-value 
                if score>30: 
                    speed1=random.choice([4,5,5,6,6,7]) # picks up random speed between 4 to 6 if score is greater that 30
                else:
                    speed1=random.choice([2,2,3,3]) # picks up random speed between 4 to 6 if score is less that 30
        if woodincolumn1=="yes":  # checks if there is wood in column 1
            screen.blit(logofwood,(90,w1,70,70)) # display the log of wood
            w1+=speed1 # Change the y value with specific number
            if w1>700:  # if wood touches the botton line then decrease the score by 1
                woodincolumn1="no"
                score-=1
                mistake-=1
                negative.play()
            if catchnet.clipline((110,w1+60),(155,w1+15)) or catchnet.clipline((95,w1+45),(140,w1+5)): # checks if net touches the log of wood
                woodincolumn1="no"
                score+=2
                positive.play()
            
        if woodincolumn2=="no": # same for 2nd column
            woodincolumn2=random.choice(["yes","no","no","no"])
            if woodincolumn2=="yes":
                w2=150
                if score>30:
                    speed2=random.choice([4,5,5,6,6,7])
                else:
                    speed2=random.choice([2,2,3,3])                
        if woodincolumn2=="yes":
            screen.blit(logofwood,(340,w2,70,70))            
            w2+=speed2
            if w2>700:
                woodincolumn2="no"
                score-=1
                mistake-=1
                negative.play()
            if catchnet.clipline((360,w2+60),(405,w2+15)) or catchnet.clipline((345,w2+45),(390,w2+5)):
                woodincolumn2="no"
                score+=2
                positive.play()
                
        if woodincolumn3=="no": # same for 3rd column
            woodincolumn3=random.choice(["yes","no","no","no"])
            if woodincolumn3=="yes":
                w3=150
                if score>30:
                    speed3=random.choice([4,5,5,6,6,7])
                else:
                    speed3=random.choice([2,2,3,3])                
        if woodincolumn3=="yes":
            screen.blit(logofwood,(590,w3,70,70))           
            w3+=speed3
            if w3>700:
                woodincolumn3="no" 
                score-=1
                mistake-=1
                negative.play()
            if catchnet.clipline((610,w3+60),(655,w3+15)) or catchnet.clipline((595,w3+45),(640,w3+5)):
                woodincolumn3="no"
                score+=2
                positive.play()
        
        if score<0:  # score cannot be negative
            score=0
        
        # For movement of flowers          
        y1+=1
        if y1>=650:
            y1 = 210  
        y2+=1
        if y2>=650:
            y2 = 210 
            
        y3+=1
        if y3>=650:
            y3 = 210
        y4+=1
        if y4>=650:
            y4 = 210
            
        # for movement of Lumberjack   
        if movement == "left":
            x1-=1
            x2-=1
            x3-=1
            if x1<460:
                movement = "right"
        elif movement == "right":
            x1+=1
            x2+=1
            x3+=1
            if x1>490:
                movement = "left"  
                
        # Checks if user hover over the restart button
        if restartgamebutton.collidepoint(mx1,my1):
            draw.rect(screen,BLACK,restartgamebutton,2,10)
            if button1==1: # checks if user clics on restart button
                state=restartpage() # display the mini restart page
                if state==STATE_GAME or state==STATE_MENU: 
                    return state
                else:
                    button1=0
                    continue
        # Checks if user hover over the back button
        if backfromgamebutton.collidepoint(mx1,my1):
            draw.rect(screen,BLACK,backfromgamebutton,2,10)
            if button1==1: # checks if user clics on back button
                state=backpage() # display the mini back page
                if state==STATE_MENU:
                    return state
                else:
                    button1=0
                    continue   
                
        # Displays the lose page if mistakes is less than 0        
        if mistake<=0:
            state=losepage()
            return state
        
        # displays the win page if score is greater than 60
        if score>=60:
            state=winpage()
            return state
        
        myClock.tick(60)                     # waits long enough to have 60 fps
        display.flip()


# Function to display the instructions page
def drawinstructions(screen, button, mx, my, state):
    
    #display all text,fonts,images
    draw.rect(screen,GREEN, (0, 0, width, height))
    draw.rect(screen,RED, (20,50,960,640))
    text = menuFont.render("Welcome to Wood Collector Game",True, BLACK)
    screen.blit(text,(70,55))
    text2=menuFont1.render("There is a evil lumberjack who is cutting trees that contributes to global",1,BLACK)
    screen.blit(text2,(40,150))
    text3=menuFont1.render("warming. Your goal is to score 60 points before missing 15 logs",1,BLACK)
    screen.blit(text3,(40,190))
    text4=menuFont1.render("of wood and plant them again to save the world.",1,BLACK)
    screen.blit(text4,(40,230))
    keypic=image.load("keydisplay.png")
    keypic=transform.scale(keypic,(250,250))
    screen.blit(keypic,(640,270))
    text5=menuFont1.render("To move the net to the right, press the right key",1,BLACK)
    text6=menuFont1.render("To move the net to the left, press the left key",1,BLACK)
    screen.blit(text5,(40,400))
    screen.blit(text6,(40,450))
    text7=menuFont1.render("Collecting one log of wood gives you 2 points",1,BLACK)
    text8=menuFont1.render("Failure to collect one log of wood gives you -1 points",1,BLACK)
    screen.blit(text7,(40,290))
    screen.blit(text8,(40,330))
    draw.rect(screen,BLUE,backbutton)
    back=menuFont1.render("Back",1,WHITE)
    screen.blit(back,(10,10))
    
    # This is for the back button the top left on the screen
    if backbutton.collidepoint(mx,my):
        draw.rect(screen,BLACK,backbutton,2)
        if button==1:
            state = STATE_MENU          
    return state

# Initializing some variables
running = True
myClock = time.Clock()
# initializing variables
state = STATE_MENU
mx = my = 0


# the Main Game Loop
while running:
    button = 0
    for e in event.get():             # checks all events that happen
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = e.pos          
            button = e.button
        elif e.type == MOUSEMOTION:
            mx, my = e.pos          
            #button = e.button 
    
    #switch between different pages        
    if state == STATE_MENU:                
        state = drawMenu(screen, button, mx, my, state)
    elif state == STATE_GAME:
        state = drawGame()
    elif state == STATE_INSTRUCTIONS:
        state = drawinstructions(screen, button, mx, my, state)
    else:
        running = False
        
    display.flip()
    myClock.tick(60)                     # waits long enough to have 60 fps
    
quit()
