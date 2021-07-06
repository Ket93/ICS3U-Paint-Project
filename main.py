from pygame import *
from random import *
from math import *

size = width, height = 1150,800
screen = display.set_mode(size)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
r,g,b,a=0,0,0,10

### Load ALL Images

titlePic=image.load("Images/Christmas Title.png")
titlePic=transform.scale(titlePic,(600,135))

wheelPic = image.load("Images/Colour wheel.png")
wheelPic=transform.scale(wheelPic,(170,170))
pencilPic = image.load("Images/Pencil.png")
pencilPic = transform.scale(pencilPic, (50, 50))
eraserPic = image.load("Images/Eraser.png")
eraserPic = transform.scale(eraserPic, (50, 50))
rectPic = image.load("Images/Rectangle.png")
rectPic = transform.scale(rectPic, (50, 50))
ellipsePic = image.load("Images/Ellipse.png")
ellipsePic = transform.scale(ellipsePic, (50, 50))
linePic = image.load("Images/Line.png")
linePic = transform.scale(linePic, (50, 50))
sprayPic = image.load("Images/Spraypaint.png")
sprayPic = transform.scale(sprayPic, (50, 50))
brushPic = image.load("Images/Paintbrush.png")
brushPic = transform.scale(brushPic, (50, 50))
polygonPic = image.load("Images/Polygon.png")
polygonPic = transform.scale(polygonPic, (48, 48))
highlighterPic = image.load("Images/Highlighter.png")
highlighterPic = transform.scale(highlighterPic, (50,50))
dropperPic = image.load("Images/Dropper.png")
dropperPic = transform.scale(dropperPic, (50,50))
clearPic = image.load("Images/Clear.png")
clearPic = transform.scale(clearPic, (47,47))
filledPic = image.load("Images/Filled.png")
filledPic = transform.scale(filledPic, (70, 70))
unfilledPic = image.load("Images/Unfilled.png")
unfilledPic = transform.scale(unfilledPic, (70, 70))
backgroundPic = image.load("Images/Background.png")
backgroundPic = transform.scale(backgroundPic, (1150, 800))

pausePic=image.load("Images/Pause.png")
pausePic = transform.scale(pausePic, (40, 40))
playPic=image.load("Images/Play.png")
playPic = transform.scale(playPic, (40, 40))
forwardPic=image.load("Images/Forward.png")
forwardPic = transform.scale(forwardPic, (40, 40))
backwardPic=image.load("Images/Backward.png")
backwardPic = transform.scale(backwardPic, (40, 40))
textBackgroundPic=image.load("Images/Textbackground.png")
textBackgroundPic=transform.scale(textBackgroundPic,(350,150))
textBackgroundPicSmall=image.load("Images/Textbackground.png")
textBackgroundPicSmall=transform.scale(textBackgroundPicSmall,(250,140))
textBackgroundPicSmaller=image.load("Images/Textbackground.png")
textBackgroundPicSmaller=transform.scale(textBackgroundPicSmaller,(220,140))

leftArrowPic=image.load("Images/Left Arrow.png")
leftArrowPic=transform.scale(leftArrowPic,(20,20))
rightArrowPic=image.load("Images/Right Arrow.png")
rightArrowPic=transform.scale(rightArrowPic,(20,20))
santaStamp=image.load("Images/Santa Stamp.png")
santaStamp=transform.scale(santaStamp,(80,102))
raindeerSmilingStamp=image.load("Images/Raindeer Smiling Stamp.png")
raindeerSmilingStamp=transform.scale(raindeerSmilingStamp,(80,102))
christmasTreeStamp=image.load("Images/Christmas Tree Stamp.png")
christmasTreeStamp=transform.scale(christmasTreeStamp,(80,102))
sledStamp=image.load("Images/Sled Stamp.png")
sledStamp=transform.scale(sledStamp,(80,102))
bellsStamp=image.load("Images/Bells Stamp.png")
bellsStamp=transform.scale(bellsStamp,(80,102))
snowmanStamp=image.load("Images/Snowman Stamp.png")
snowmanStamp=transform.scale(snowmanStamp,(80,102))
stockingStamp=image.load("Images/Stocking Stamp.png")
stockingStamp=transform.scale(stockingStamp,(80,102))
ornamentsStamp=image.load("Images/Ornaments Stamp.png")
ornamentsStamp=transform.scale(ornamentsStamp,(80,102))
penguinStamp=image.load("Images/Penguin Stamp.png")
penguinStamp=transform.scale(penguinStamp,(80,102))
presentStamp=image.load("Images/Present Stamp.png")
presentStamp=transform.scale(presentStamp,(80,102))

background1ActualPic=image.load("Images/Background1.png")
background1ActualPic=transform.scale(background1ActualPic,(850,500))
background1DisplayPic=image.load("Images/Background1.png")
background1DisplayPic=transform.scale(background1DisplayPic,(150,100))
background2ActualPic=image.load("Images/Background2.png")
background2ActualPic=transform.scale(background2ActualPic,(850,500))
background2DisplayPic=image.load("Images/Background2.png")
background2DisplayPic=transform.scale(background2DisplayPic,(150,100))
background3ActualPic=image.load("Images/Background3.png")
background3ActualPic=transform.scale(background3ActualPic,(850,500))
background3DisplayPic=image.load("Images/Background3.png")
background3DisplayPic=transform.scale(background3DisplayPic,(150,100))
background4ActualPic=image.load("Images/Background4.png")
background4ActualPic=transform.scale(background4ActualPic,(850,500))
background4DisplayPic=image.load("Images/Background4.png")
background4DisplayPic=transform.scale(background4DisplayPic,(150,100))

undoPic=image.load("Images/Undo Arrow.png")
undoPic=transform.scale(undoPic,(45,45))
redoPic=image.load("Images/Redo Arrow.png")
redoPic=transform.scale(redoPic,(45,45))
                                                       
whitePic = image.load("Images/Whitebackground.png") #loading a white pic to use for backgrounds
whitePic = transform.scale(whitePic, (50, 50))
whiteActualPic = image.load("Images/Whitebackground.png") #loading a white pic to use for backgrounds
whiteActualPic = transform.scale(whitePic, (850, 500))
whiteDisplayPic = image.load("Images/Whitebackground.png") #loading a white pic to use for backgrounds
whiteDisplayPic = transform.scale(whitePic, (150, 100))


tool = "No Tool"
fill = "No Fill"
col = BLACK
cornerThick=0
stamp="0"
verticiesNoFill = []  # vertices is used for polygon tool. It keeps track of the vertices
verticiesFill=[]
play=True
changeStamp=0 # a number to know which stamp page the user is on
changeBackground=0 # a number to know which background page the user is on
undoList=[]
redoList=[]
textures=[background1ActualPic,background2ActualPic,background3ActualPic,background4ActualPic]
background=False
appendCanvasShot=False # defining a variable to help with undo and redo
redoCount=0
screenCapCount=0
pos=0
lenTextures=len(textures)

### Defining fonts and text
font.init()
sofiaFont=font.SysFont("Sofia Regular", 38)
sofiaFontSmall=font.SysFont("Sofia Regular", 16)

### Defining all Thicknesses

pencilThick=1
eraserThick=2
rectThick=2
ellipseThick=2
brushThick=5
lineThick=2
polyThick=2
highlighterThick=5
sprayThick=30


### Defining all RECTS

pencilRect = Rect(65, 20, 50,50)
eraserRect = Rect(155, 20, 50, 50)
rectRect = Rect(65, 90, 50, 50)
lineRect = Rect(155, 90, 50, 50)
ellipseRect = Rect(65, 160, 50, 50)
polygonRect = Rect(155, 160, 50, 50)
sprayRect = Rect(155, 230, 50, 50)
brushRect = Rect(65, 230, 50, 50)
highlighterRect=Rect(65,300,50,50)
dropperRect=Rect(155,300,50,50)
clearAllRect=Rect(65,370,50,50)
textRect=Rect(770,635,350,150)
filledRect = Rect(50, 650, 70, 70)
unfilledRect = Rect(150, 650, 70, 70)
canvasRect = Rect(275, 125,850, 500)
wheelRect = Rect(53, 480, 170, 170)
backwardRect=Rect(25,740,40,40)
pauseRect=Rect(85,740,40,40)
playRect=Rect(145,740,40,40)
forwardRect=Rect(205,740,40,40)
stampsRect=Rect(495,640,250,140)
stamp1Rect=Rect(530,660,80,102)
stamp2Rect=Rect(632,660,80,102)
stampLeftRect=Rect(500,700,20,20)
stampRightRect=Rect(720,700,20,20)
backgroundRect=Rect(260,640,220,140)
backgroundDisplayRect=Rect(295,660,150,100)
backgroundLeftRect=Rect(265,700,20,20)
backgroundRightRect=Rect(455,700,20,20)
undoRect=Rect(250,10,50,50)
redoRect=Rect(320,10,50,50)
saveRect=Rect(250,70,50,50)

### "Blit" all images and whitePic to get a white picture background

screen.blit(backgroundPic, (0, 0))
screen.blit(whitePic, (65, 20))
screen.blit(pencilPic, (65, 20))
screen.blit(whitePic, (155, 20))
screen.blit(eraserPic, (155, 20))
screen.blit(rectPic, (65, 90))
screen.blit(whitePic, (65, 160))
screen.blit(ellipsePic, (65, 160))
screen.blit(whitePic, (155, 90))
screen.blit(linePic, (155, 90))
screen.blit(whitePic, (155, 160))
screen.blit(polygonPic, (155, 160))
screen.blit(whitePic, (155, 230))
screen.blit(sprayPic, (155, 230))
screen.blit(brushPic, (65, 230))
screen.blit(whitePic, (65,300))
screen.blit(highlighterPic, (65,300))
screen.blit(whitePic, (155,300))
screen.blit(dropperPic, (155,300))
screen.blit(whitePic, (65,370))
screen.blit(clearPic, (66,371))
screen.blit(filledPic, (50, 650))
screen.blit(unfilledPic, (150, 650))
screen.blit(wheelPic, (55, 480))
whitePic = transform.scale(whitePic, (40, 40)) # re-transforming the white background so it fits the new picture size
screen.blit(whitePic, (85,740))
screen.blit(pausePic, (85,740))
screen.blit(whitePic, (145,740))
screen.blit(playPic, (145,740))
screen.blit(whitePic, (205,740))
screen.blit(forwardPic, (205,740))
screen.blit(whitePic, (25,740))
screen.blit(backwardPic, (25,740))
screen.blit(textBackgroundPicSmall,(495,640))
screen.blit(textBackgroundPicSmaller,(backgroundRect))
screen.blit(leftArrowPic,(backgroundLeftRect))
screen.blit(rightArrowPic,(backgroundRightRect))
whitePic = transform.scale(whitePic, (50, 50))
screen.blit(whitePic, (250,10))
screen.blit(undoPic,(250,10))
screen.blit(whitePic, (320,10))
screen.blit(redoPic,(320,10))

draw.rect(screen, WHITE, (canvasRect))  # drawing canvas after background so it dosen't overlap

display.flip()

### Loading the music

init()  # need init to initialize the mixer
mixer.music.load("Music/Jingle Bells.mp3")  #load a MUSIC object

### Making a list for music to go forward and backwards for switching songs
music=["Music/Jingle Bells.mp3","Music/12 Days.mp3","Music/First Noel.mp3","Music/Deck The Halls.mp3","Music/Oh Christmas Tree.mp3","Music/Silent Night.mp3"]
songChoice=0
mixer.music.play()

mb = mouse.get_pressed()
mx, my = mouse.get_pos()

running = True
while running:
    click=False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button==1:
                click=True
                if canvasRect.collidepoint(mx,my):
                    sx, sy = mouse.get_pos()  # starting position
                    canvasClick=True
                if tool=="Polygon" and canvasRect.collidepoint(mx,my) and fill=="False" or tool=="Polygon" and canvasRect.collidepoint(mx,my) and fill=="No Fill" :
                    verticiesNoFill.append((mx, my))
                if tool=="Polygon" and canvasRect.collidepoint(mx,my) and fill=="True":
                    verticiesFill.append((mx,my))
                screenCap = screen.copy()  # screenshot
            if evt.button==4:
                if tool=="Pencil":
                    pencilThick+=1
                elif tool=="Eraser":
                    if eraserThick<=24:
                        eraserThick+=1
                elif tool=="Rect":
                    if rectThick<=49:
                        rectThick+=1
                elif tool=="Ellipse":
                    if ellipseThick<=49:
                        ellipseThick+=1
                elif tool=="Brush":
                    if brushThick<=24:
                        brushThick+=1
                elif tool=="Line":
                    if lineThick<=19:
                        lineThick+=1

                elif tool=="Polygon":
                    if polyThick<=20:
                        polyThick+=1

                elif tool=="Highlighter":
                    if highlighterThick<=20:
                        highlighterThick+=1

                elif tool=="Spray":
                    if sprayThick<=40:
                        sprayThick+=1
                    
            if evt.button==5:
                if tool=="Pencil":
                    if pencilThick>1:
                        pencilThick-=1
                elif tool=="Eraser":
                    if eraserThick>1:
                        eraserThick-=1
                elif tool=="Rect":
                    if rectThick>1:
                        rectThick-=1
                elif tool=="Ellipse":
                    if ellipseThick>1:
                        ellipseThick-=1
                elif tool=="Brush":
                    if brushThick>10:
                        brushThick-=1
                elif tool=="Line":
                    if lineThick>1:
                        lineThick-=1

                elif tool=="Polygon":
                    if polyThick>1:
                        polyThick-=1

                elif tool=="Highlighter":
                    if highlighterThick>1:
                        highlighterThick-=1

                elif tool=="Spray":
                    if sprayThick>20:
                        sprayThick-=1
                        
        if evt.type == MOUSEBUTTONUP:
            canvasClick=False

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()

    ### Drawing all RECTS

    draw.rect(screen, WHITE, (119, 435, 35, 35), 3)  # box that shows what colour is selected
    draw.rect(screen,BLACK,(textRect),2)

    if tool != "Pencil":
        draw.rect(screen, GREEN, (pencilRect), 2)
        if pencilRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (pencilRect), 2)

    if tool != "Eraser":
        draw.rect(screen, GREEN, (eraserRect), 2)
        if eraserRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (eraserRect), 2)

    if tool != "Rect":
        draw.rect(screen, GREEN, (rectRect), 2)
        if rectRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (rectRect), 2)

    if tool != "Ellipse":
        draw.rect(screen, GREEN, (ellipseRect), 2)
        if ellipseRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (ellipseRect), 2)

    if tool != "Line":
        draw.rect(screen, GREEN, (lineRect), 2)
        if lineRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (lineRect), 2)

    if tool != "Spray":
        draw.rect(screen, GREEN, (sprayRect), 2)
        if sprayRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (sprayRect), 2)

    if tool != "Brush":
        draw.rect(screen, GREEN, (brushRect), 2)
        if brushRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (brushRect), 2)

    if tool != "Polygon":
        draw.rect(screen, GREEN, (polygonRect), 2)
        if polygonRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (polygonRect), 2)

    if tool != "Highlighter":
        draw.rect(screen, GREEN, (highlighterRect), 2)
        if highlighterRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (highlighterRect), 2)

    if tool != "Dropper":
        draw.rect(screen, GREEN, (dropperRect), 2)
        if dropperRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (dropperRect), 2)

    if tool != "Clear":
        draw.rect(screen, GREEN, (clearAllRect), 2)
        if clearAllRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (clearAllRect), 2)

    if fill != "True":
        draw.rect(screen, GREEN, (filledRect), 2)
        if filledRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (filledRect), 2)

    if fill != "False":
        draw.rect(screen, GREEN, (unfilledRect), 2)
        if unfilledRect.collidepoint(mx, my):
            draw.rect(screen, (240, 128, 128), (unfilledRect), 2)

    draw.rect(screen, GREEN, (backwardRect),2)
    if backwardRect.collidepoint(mx, my):
        draw.rect(screen, (240,128,128), (backwardRect),2)

    if play!=False:
        draw.rect(screen, GREEN, (pauseRect),2)
        if pauseRect.collidepoint(mx, my):
            draw.rect(screen, (240,128,128), (pauseRect),2)

    if play!=True:
        draw.rect(screen, GREEN, (playRect),2)
        if playRect.collidepoint(mx, my):
            draw.rect(screen, (240,128,128), (playRect),2)

    draw.rect(screen, GREEN, (forwardRect),2)
    if forwardRect.collidepoint(mx, my):
        draw.rect(screen, (240,128,128), (forwardRect),2)

    draw.rect(screen, GREEN, (undoRect),2)
    if undoRect.collidepoint(mx, my):
        draw.rect(screen, (240,128,128), (undoRect),2)

    draw.rect(screen, GREEN, (redoRect),2)
    if redoRect.collidepoint(mx, my):
        draw.rect(screen, (240,128,128), (redoRect),2)
        

    ### Selecting the TOOLS

    if mb[0] == 1:
        if pencilRect.collidepoint(mx, my) and click:
            tool = "Pencil"
            draw.rect(screen, RED, (pencilRect), 2)

        elif eraserRect.collidepoint(mx, my) and click:
            tool = "Eraser"
            draw.rect(screen, RED, (eraserRect), 2)

        elif rectRect.collidepoint(mx, my) and click:
            tool = "Rect"
            draw.rect(screen, RED, (rectRect), 2)

        elif ellipseRect.collidepoint(mx, my) and click:
            tool = "Ellipse"
            draw.rect(screen, RED, (ellipseRect), 2)

        elif lineRect.collidepoint(mx, my) and click:
            tool = "Line"
            draw.rect(screen, RED, (lineRect), 2)

        elif sprayRect.collidepoint(mx, my) and click:
            tool = "Spray"
            draw.rect(screen, RED, (sprayRect), 2)

        elif brushRect.collidepoint(mx, my) and click:
            tool = "Brush"
            draw.rect(screen, RED, (brushRect), 2)

        elif polygonRect.collidepoint(mx, my) and click:
            tool = "Polygon"
            draw.rect(screen, RED, (polygonRect), 2)
            polyShot=screen.copy()
            verticiesNoFill=[]
            verticiesFill=[]

        elif highlighterRect.collidepoint(mx,my) and click:
            tool = "Highlighter"
            draw.rect(screen,RED,(highlighterRect),2)

        elif dropperRect.collidepoint(mx,my) and click:
            tool = "Dropper"
            draw.rect(screen,RED,(dropperRect),2)

        elif clearAllRect.collidepoint(mx,my) and click:
            tool = "Clear"
            draw.rect(screen, RED, (clearAllRect), 2)
            if clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool=="Clear" and background==False or clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool=="Clear" and changeBackground==4 :
                draw.rect(screen, WHITE, (canvasRect))
                verticiesFill = []
                verticiesNoFill = []
                undoList = []
                redoList = []

            elif clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool == "Clear" and changeBackground ==0 and background==True :
                screen.blit(background1ActualPic,(canvasRect))
                verticiesFill = []
                verticiesNoFill = []
                undoList = []
                redoList = []

            elif clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool == "Clear" and changeBackground ==1:
                screen.blit(background2ActualPic,(canvasRect))
                verticiesFill = []
                verticiesNoFill = []
                undoList = []
                redoList = []

            elif clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool == "Clear" and changeBackground ==2:
                screen.blit(background3ActualPic,(canvasRect))
                verticiesFill = []
                verticiesNoFill = []
                undoList = []
                redoList = []

            elif clearAllRect.collidepoint(mx, my) and mb[0] == 1 and click and tool == "Clear" and changeBackground ==3:
                screen.blit(background4ActualPic,(canvasRect))
                verticiesFill = []
                verticiesNoFill = []
                undoList = []
                redoList = []


            
        elif filledRect.collidepoint(mx, my) and click:
            fill = "True"
            draw.rect(screen, RED, (filledRect), 2)

        elif unfilledRect.collidepoint(mx, my) and click:
            fill = "False"
            draw.rect(screen, RED, (unfilledRect), 2)

    ### Using the TOOLS

    if mb[0] == 1:
        if canvasRect.collidepoint(mx, my):
            screen.set_clip(canvasRect)  # only the canvas can be "updated"
            if tool == "Pencil":
                if pencilThick>5:
                    pencilThick=5
                draw.line(screen, col, (omx, omy), (mx, my),pencilThick)

            elif tool == "Eraser" and background==False:
                dx = mx - omx
                dy = my - omy
                dist = int(sqrt(dx ** 2 + dy ** 2))
                draw.circle(screen, WHITE, (mx, my), eraserThick)
                for i in range(1, dist + 1):
                    dotX = int(omx + i * dx / dist)
                    dotY = int(omy + i * dy / dist)
                    draw.circle(screen, WHITE, (dotX, dotY), eraserThick)
            
            elif tool == "Rect":
                screen.blit(screenCap, (0, 0))
                if fill == "True" or fill == "No Fill":
                    draw.rect(screen, col, (sx, sy, mx - sx, my - sy))
                if fill == "False":
                    drawRect=Rect(sx,sy,(mx-sx),(my-sy))
                    drawRect.normalize()
                    print(drawRect)
                    if rectThick>0 and min(drawRect[2],drawRect[3])>rectThick*2:
                        rectSurface=Surface(drawRect.width,drawRect.height)
                        rectSurface.set_colorkey((1,1,1))
                        rectSurface.fill((1,1,1))
                        draw.rect(rectSurface,col,(0,0,drawRect[2],drawRect[3]))
                        draw.rect(rectSurface,(1,1,1),(rectThick,rectThick,drawRect[2]-rectThick*2,drawRect[3]-rectThick*2))
                        screen.blit(rectSurface,(drawRect[0],drawRect[1]))
                    else:
                        draw.rect(screen,col,(drawRect))

           
            elif tool=="Ellipse":
                screen.blit(screenCap,(0,0))
                w = abs(mx - sx)
                h = abs(my - sy)
                
                if fill=="True" or fill=="No Fill":
                    try:
                        if mx>sx and my>sy:
                            drawEllipseRect=Rect(sx,sy,w,h)
                        if mx<sx and my<sy:
                            drawEllipseRect=Rect(mx,my,w,h)
                        if mx>sx and my<sy:
                            drawEllipseRect=Rect(sx,my,w,h)
                        if mx<sx and my>sy:
                            drawEllipseRect=Rect(mx,sy,w,h)
                        drawEllipseRect.normalize()
                        draw.ellipse (screen,col,(drawEllipseRect))
                    except:
                        pass
                    
                if fill=="False":
                    try:
                        if mx>sx and my>sy:
                            drawEllipseRect=Rect(sx,sy,w,h)
                        if mx<sx and my<sy:
                            drawEllipseRect=Rect(mx,my,w,h)
                        if mx>sx and my<sy:
                            drawEllipseRect=Rect(sx,my,w,h)
                        if mx<sx and my>sy:
                            drawEllipseRect=Rect(mx,sy,w,h)
                        drawEllipseRect.normalize()
                        draw.arc(screen,col,drawEllipseRect,0,360,ellipseThick)

                    except:
                        pass            

            elif tool == "Line":
                screen.blit(screenCap, (0, 0))
                draw.line(screen, col, (sx, sy), (mx, my),lineThick)

            elif tool == "Spray":
                radius = sprayThick
                for i in range (100):
                    randX = randint(-radius, radius)
                    randY = randint(-radius, radius)
                    if sqrt(randX ** 2 + randY ** 2) < radius:
                        draw.circle(screen, col, (randX + mx, randY + my), 0)

            elif tool == "Brush":
                dx = mx - omx
                dy = my - omy
                dist = int(sqrt(dx ** 2 + dy ** 2))
                draw.circle(screen, col, (mx, my), brushThick)
                for i in range(1, dist + 1):
                    dotX = int(omx + i * dx / dist)
                    dotY = int(omy + i * dy / dist)
                    draw.circle(screen, col, (dotX, dotY), brushThick+10)

            elif tool=="Highlighter":
                marker=Surface((20,20),SRCALPHA)
                draw.circle(marker,(r,g,b,10),(10,10),highlighterThick)
                dx = mx - omx
                dy = my - omy
                dist = int(sqrt(dx ** 2 + dy ** 2))
                if mb[0]==1:
                    for i in range(1, dist + 1):
                        dotX = int(omx + i * dx / dist)
                        dotY = int(omy + i * dy / dist)
                        screen.blit(marker,(dotX,dotY))

            elif tool=="Dropper":
                if canvasRect.collidepoint(mx,my):
                   col=screen.get_at((mx,my))

            elif tool=="Clear":
                screen.set_clip(None)
                if clearAllRect.collidepoint(mx,my) and mb[0]==1 and click:
                    draw.rect(screen,WHITE,(canvasRect))
                    verticiesFill=[]
                    verticiesNoFill=[]
                    undoList=[]
                    redoList=[]
                    screen.set_clip(canvasRect)


    screen.set_clip(canvasRect)

    if tool == "Polygon" and canvasRect.collidepoint(mx,my):
        
        if fill=="False" or fill=="No Fill":
            verticiesFill=[]
            polyshotNoFill=screen.copy()
            screen.blit(polyShot, (0, 0))
            screen.blit(polyshotNoFill,(0,0))
            if len(verticiesNoFill)==2:
                draw.line(screen, col,verticiesNoFill[0], verticiesNoFill[1],polyThick)
            elif len(verticiesNoFill) > 2:
                draw.polygon(screen, col, verticiesNoFill , polyThick)

        if fill=="True":
            verticiesNoFill=[]
            polyshotFill=screen.copy()
            screen.blit(polyShot, (0, 0))
            screen.blit(polyshotFill,(0,0))
            if len(verticiesFill)==2:
                draw.line(screen, col, verticiesFill[0], verticiesFill[1])
            elif len(verticiesFill) > 2:
                draw.polygon(screen, col, verticiesFill, 0)

    screen.set_clip(None)

    ### using undo and redo


   # print(len(undoList),len(redoList))
    if mb[0]==1 and canvasRect.collidepoint(mx,my) and click and tool!="Dropper":
        undoList.append(screenCap)
        appendCanvasShot=True
        try:
            for i in range(redoCount):
                redoList.pop()
                redoList.pop()

        except:
            pass
                

            
    if undoRect.collidepoint(mx,my) and mb[0]==1 and click:
        canvasShot=screen.copy()
        verticiesFill=[]
        verticiesNoFill=[]
        if len(undoList)==0:
            draw.rect(screen,WHITE,(canvasRect))
        else:
            screen.blit(undoList[-1],(0,0))
            if len(undoList)!=1:
                redoList.append(undoList[-1])
                undoList.pop()
                redoCount+=1


        if appendCanvasShot:
            redoList.insert(0,canvasShot)
            appendCanvasShot=False
            
            
    if redoRect.collidepoint(mx,my) and mb[0]==1 and click:
        try:
            screen.blit(redoList[-1],(0,0))
            
            if len(redoList)!=1:
                undoList.append(redoList[-1])
                redoList.pop()

        except:
            pass

    if mb[0]==1 and canvasRect.collidepoint(mx,my) and click and tool!="Dropper" and len(undoList)==2 and len(redoList)!=0:
            undoList=[]
            redoList=[]
            undoList.append(screenCap)


    ### playing, pausing, going forward, and going backwards with music

    if play==False:
        draw.rect(screen, RED, (pauseRect),2)

    if play==True:
        draw.rect(screen, RED, (playRect),2)

    if mb[0]==1 and pauseRect.collidepoint(mx,my)and click :
        mixer.music.pause()
        play=False

    if mb[0]==1 and playRect.collidepoint(mx,my) and click :
        mixer.music.unpause()
        play=True

    if mb[0]==1 and forwardRect.collidepoint(mx,my) and click:
        music=["Music/Jingle Bells.mp3","Music/12 Days.mp3","Music/First Noel.mp3","Music/Deck The Halls.mp3","Music/Oh Christmas Tree.mp3","Music/Silent Night.mp3"]
        if songChoice<5:
            songChoice+=1
        else:
            songChoice=0
        mixer.music.load(music[songChoice])
        mixer.music.play()
        

    if mb[0]==1 and backwardRect.collidepoint(mx,my) and click:
        if songChoice>0:
            songChoice-=1
        else:
            songChoice=5
        mixer.music.load(music[songChoice])
        mixer.music.play()

    ### Drawing text for tools

    screen.blit(textBackgroundPic,(770,635))

    widthText=sofiaFont.render ("Thickness: ",True,BLACK)

    if tool=="No Tool":
        noToolText=sofiaFont.render ("None",True,BLACK)
        screen.blit(noToolText,(970,640))

    elif tool=="Pencil":
        pencilWidthText=sofiaFont.render(str(pencilThick),True,BLACK)
        screen.blit(pencilWidthText,(970,640))
        
    elif tool=="Eraser":
        eraserWidthText=sofiaFont.render(str(eraserThick),True,BLACK)
        screen.blit(eraserWidthText,(970,640))
        
    elif tool=="Rect" and fill=="True" or tool=="Rect" and fill=="No Fill":
            rectWidthText=sofiaFont.render("Filled",True,BLACK)
            screen.blit(rectWidthText,(970,640))

    elif tool=="Rect" and fill=="False":
        rectWidthText=sofiaFont.render(str(rectThick),True,BLACK)
        screen.blit(rectWidthText,(970,640))

    elif tool=="Ellipse" and fill=="True" or tool=="Ellipse" and fill=="No Fill":
            ellipseWidthText=sofiaFont.render("Filled",True,BLACK)
            screen.blit(ellipseWidthText,(970,640))
        
    elif tool=="Ellipse" and fill=="False":
            ellipseWidthText=sofiaFont.render(str(ellipseThick),True,BLACK)
            screen.blit(ellipseWidthText,(970,640))

    elif tool=="Brush":
        brushWidthText=sofiaFont.render(str(brushThick),True,BLACK)
        screen.blit(brushWidthText,(970,640))

    elif tool=="Line":
        lineWidthText=sofiaFont.render(str(lineThick),True,BLACK)
        screen.blit(lineWidthText,(970,640))

    elif tool=="Polygon":
        polygonWidthText=sofiaFont.render("2",True,BLACK)
        screen.blit(polygonWidthText,(970,640))

    elif tool=="Spray":
        sprayWidthText=sofiaFont.render("20",True,BLACK)
        screen.blit(sprayWidthText,(970,640))

    elif tool=="Highlighter":
        highlighterWidthText=sofiaFont.render("10",True,BLACK)
        screen.blit(highlighterWidthText,(970,640))

    elif tool=="Dropper":
        dropperWidthText=sofiaFont.render("None",True,BLACK)
        screen.blit(dropperWidthText,(970,640))

    elif tool=="Stamp":
        stampWidthText=sofiaFont.render("None",True,BLACK)
        screen.blit(stampWidthText,(970,640))

    elif tool=="Clear":
        clearWidthText=sofiaFont.render("None",True,BLACK)
        screen.blit(clearWidthText,(970,640))

    screen.blit(widthText,(788,640))
    
    colText=r,g,b
    colourText=sofiaFontSmall.render("Colour: ",True,BLACK)
    screen.blit(colourText,(780,700))
    actualColourText=sofiaFontSmall.render(str(colText),True,BLACK)
    screen.blit(actualColourText,(835,700))

    toolText=sofiaFontSmall.render("Tool: ",True,BLACK)
    screen.blit(toolText,(980,700))
    actualToolText=sofiaFontSmall.render(str(tool),True,BLACK)
    screen.blit(actualToolText,(1030,700))

    musicText=["Jingle Bells","12 Days","First Noel","Deck The Halls","Oh Christmas","Silent Night"]
    songText=sofiaFontSmall.render("Song: ",True,BLACK)
    screen.blit(songText,(970,735))
    actualSongText=sofiaFontSmall.render(str(musicText[songChoice]),True,BLACK)
    screen.blit(actualSongText,(1010,735))

    positionText=sofiaFontSmall.render("Position: ",True,BLACK)
    screen.blit(positionText,(780,735))
    mxmyText=mx,my
    if canvasRect.collidepoint(mx,my):
        positionActualText=sofiaFontSmall.render(str(mxmyText),True,BLACK)
        screen.blit(positionActualText,(845,735))
    else:
        positionActualText=sofiaFontSmall.render("Not On Canvas",True,BLACK)
        screen.blit(positionActualText,(845,735))

    screen.blit(titlePic,(400,0)) #bliting title


    ### Generating and changing stamps displayed and drawing stamps

    if mb[0]==1 and stamp1Rect.collidepoint (mx,my) and click:
        tool="Stamp"
        stamp="1"

    if mb[0]==1 and stamp2Rect.collidepoint(mx,my) and click:
        tool="Stamp"
        stamp="2"

    if mb[0]==1 and stampRightRect.collidepoint(mx,my) and click:
        changeStamp+=1
        screen.blit(textBackgroundPicSmall,(495,640))
        if changeStamp==5:
            changeStamp=0
            
    if mb[0]==1 and stampLeftRect.collidepoint(mx,my) and click:
        changeStamp-=1
        screen.blit(textBackgroundPicSmall,(495,640))
        if changeStamp==-1:
            changeStamp=4
                
    
    if changeStamp==0:
        screen.blit(textBackgroundPicSmall,(495,640))
        screen.blit(leftArrowPic,(500,700)) #bliting the arrows to swtich stamps
        screen.blit(rightArrowPic,(720,700))
        screen.blit(santaStamp,(530,660))
        screen.blit(raindeerSmilingStamp,(632,660))
            
        if mb[0]==1 and stamp=="1" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(santaStamp,(mx,my))

        elif mb[0]==1 and stamp=="2" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(raindeerSmilingStamp,(mx,my))

    if changeStamp==1:
        screen.blit(textBackgroundPicSmall,(495,640))
        screen.blit(leftArrowPic,(500,700))
        screen.blit(rightArrowPic,(720,700))
        screen.blit(christmasTreeStamp,(530,660))
        screen.blit(sledStamp,(632,660))

        if mb[0]==1 and stamp=="1" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(christmasTreeStamp,(mx,my))

        elif mb[0]==1 and stamp=="2" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(sledStamp,(mx,my))

                
    if changeStamp==2:
        screen.blit(textBackgroundPicSmall,(495,640))
        screen.blit(leftArrowPic,(500,700))
        screen.blit(rightArrowPic,(720,700))
        screen.blit(bellsStamp,(530,660))
        screen.blit(snowmanStamp,(632,660))
            
        if mb[0]==1 and stamp=="1" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(bellsStamp,(mx,my))
            
        elif mb[0]==1 and stamp=="2" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(snowmanStamp,(mx,my))


    if changeStamp==3:
        screen.blit(textBackgroundPicSmall,(495,640))
        screen.blit(leftArrowPic,(500,700))
        screen.blit(rightArrowPic,(720,700))
        screen.blit(stockingStamp,(530,660))
        screen.blit(ornamentsStamp,(632,660))

        if mb[0]==1 and stamp=="1" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(stockingStamp,(mx,my))

        elif mb[0]==1 and stamp=="2" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(ornamentsStamp,(mx,my))

    if changeStamp==4:
        screen.blit(textBackgroundPicSmall,(495,640))
        screen.blit(leftArrowPic,(500,700))
        screen.blit(rightArrowPic,(720,700))
        screen.blit(penguinStamp,(530,660))
        screen.blit(presentStamp,(632,660))

        if mb[0]==1 and stamp=="1" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(penguinStamp,(mx,my))

        elif mb[0]==1 and stamp=="2" and tool=="Stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            screen.blit(screenCap,(0,0))
            screen.blit(presentStamp,(mx,my))

    ### Changing the background

    if backgroundRightRect.collidepoint(mx,my) and mb[0]==1 and click:
        changeBackground+=1
        pos+=1
        if pos==5:
            pos=0
        if changeBackground==5:
            changeBackground=0

    if backgroundLeftRect.collidepoint(mx,my) and mb[0]==1 and click:
        changeBackground-=1
        pos-=1
        
        if pos==-1:
            pos=4
        if changeBackground==-1:
            changeBackground=4        
            

    
    if changeBackground==0:
        screen.blit(background1DisplayPic,(backgroundDisplayRect))
        if mb[0]==1 and backgroundDisplayRect.collidepoint(mx,my) and click:
            screen.blit(background1ActualPic,(canvasRect))
            verticiesFill=[]
            verticiesNoFill=[]
            background=True
        if tool=="Eraser" and canvasRect.collidepoint(mx,my) and mb[0]==1 and background==True:
            screen.set_clip(canvasRect)
            try:
                sample=textures[pos].subsurface((mx-275,my-125,eraserThick,eraserThick))
                screen.blit(sample,(mx,my))
            except:
                pass

    if changeBackground==1:
        screen.blit(background2DisplayPic,(backgroundDisplayRect))
        if mb[0]==1 and backgroundDisplayRect.collidepoint(mx,my) and click:
            screen.blit(background2ActualPic,(canvasRect))
            verticiesFill=[]
            verticiesNoFill=[]
            background=True
        if tool=="Eraser" and canvasRect.collidepoint(mx,my) and mb[0]==1 and background==True:
            screen.set_clip(canvasRect)
            try:
                sample=textures[pos].subsurface((mx-275,my-125,eraserThick,eraserThick))
                screen.blit(sample,(mx,my))
            except:
                pass

    if changeBackground==2:
        screen.blit(background3DisplayPic,(backgroundDisplayRect))
        if mb[0]==1 and backgroundDisplayRect.collidepoint(mx,my) and click:
            screen.blit(background3ActualPic,(canvasRect))
            verticiesFill=[]
            verticiesNoFill=[]
            background=True
        if tool=="Eraser" and canvasRect.collidepoint(mx,my) and mb[0]==1 and background==True:
            screen.set_clip(canvasRect)
            try:
                sample=textures[pos].subsurface((mx-275,my-125,eraserThick,eraserThick))
                screen.blit(sample,(mx,my))
            except:
                pass
    if changeBackground==3:
        screen.blit(background4DisplayPic,(backgroundDisplayRect))
        if mb[0]==1 and backgroundDisplayRect.collidepoint(mx,my) and click:
            screen.blit(background4ActualPic,(canvasRect))
            verticiesFill=[]
            verticiesNoFill=[]
            background=True
        if tool=="Eraser" and canvasRect.collidepoint(mx,my) and mb[0]==1 and background==True:
            screen.set_clip(canvasRect)
            try:
                sample=textures[pos].subsurface((mx-275,my-125,eraserThick,eraserThick))
                screen.blit(sample,(mx,my))
            except:
                pass

    if changeBackground==4:
        screen.blit(whiteDisplayPic,(backgroundDisplayRect))
        if mb[0]==1 and backgroundDisplayRect.collidepoint(mx,my) and click:
            verticiesFill = []
            verticiesNoFill = []
            screen.blit(whiteActualPic,(canvasRect))
        background=False

    ### Selecting (changing) the colour
    
    if wheelRect.collidepoint(mx, my) and click:
        col = screen.get_at((mx, my))
        r,g,b,a = screen.get_at((mx, my))
    draw.rect(screen, col, (121, 437, 31, 31))


    # Updating the old mx and my to the one used in the most recent running
    omx = mx 
    omy = my

    display.flip()

quit()
