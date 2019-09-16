import math, datetime, re, os
nCols = 5
nRows = 5
grid = []
cellStroke = 0
selectedX = selectedY = 0
mouseToggled = True

def setup():    
    global nCols, nRows, grid
    
    size(1280, 750)
    # size(1000, 750)
    # size (500,800)
    
    background(0)    
    
    print "Arrow keys select R, G, B color to control"
    print "Mouse movement controls selected color"
    print "Mouse click turns on/off RGB indentifier tool"
    print "Mouse drage to move the indentifier"
    print "'+'/'-' to add/remove colums and rows"
    text("Created by Andrew Donato", width*0.01, height*0.98)
    
def mouseClicked():
    global mouseToggled
    mouseToggled = not mouseToggled

def keyReleased():
    global nCols, nRows

    if key == "=" or key == "+" :      
        nCols += 1
        nRows += 1
    elif key == "-" or key == "_" :
        if nCols > 1 and nRows > 1 :      
            nCols -= 1
            nRows -= 1
    elif key == "s" or key == "S" :        
        time = datetime.datetime.now()
        time = re.sub(":", "-", str(time))
        time = re.sub(" ", ".", str(time))
        fileName= "rgb-cell-map-and-identifier.%s.png" %(time)
        
        print "Currently located in : %s" %(os.getcwd())
        print "Saving as : %s" % fileName
        saveFrame(fileName)
    else:
        print "Key is " + str(key)
            
def mouseDragged():
# def mouseMoved():
    global selectedX, selectedY
    selectedX = mouseX
    selectedY = mouseY         
    return selectedX, selectedY   

def draw():
    global nCols, nRows, grid, mouseToggled, cellStroke
    background(0)
    noCursor()
    cellWidth = width/int(round(nCols))
    cellHeight = height/int(round(nRows))
    
    grid = makeGrid()
    for i in range(nCols):
        for j in range(nRows):
            # print i, j
            grid[i][j] = Cell(i, j, i*cellWidth, j*cellHeight, cellWidth, cellHeight, 0, 0, 0)
    
      
    # if key == "=" or key == "+" :
    #     print "key pressed"
    # else :
        # print "other key"

    for i in range(nCols):
        for j in range(nRows):
            strokeWeight(cellStroke)
            grid[i][j].colorCell()
            # grid[i][j].cellGlow(selectedX, selectedY)
            grid[i][j].display()
            grid[i][j].cellGlow(selectedX, selectedY)
            ## to check cell values to see if I'm slightly color blind
            # print i, j
            # print grid[i][j].r, grid[i][j].g, grid[i][j].b

    colorPositions = colorFromPosition(mouseX, mouseY)
    # print colorPositions
    
    stroke(255-colorPositions['colorPositionY'], 255-colorPositions['colorFromHypotenuse'], 255-colorPositions['colorPositionX'])  
    strokeWeight(8)
    line(mouseX, mouseY, pmouseX, pmouseY)       
    
    # def mouseClicked():
    # if mousePressed and mouseButton==RIGHT:
    #     mouseToggled = not mouseToggled
    # fill(255)
    # text("Created by Andrew Donato", width*0.01, height*0.98)

def colorFromPosition(x, y):
    colorPositionX=x*255/width
    colorPositionY=y*255/height
    mouseHypotenuse = math.sqrt(mouseX**2 + mouseY**2)
    # mouseHypotenuse = math.sqrt(x**2 + y**2)
    totalHypotenuse = math.sqrt(width**2 + height**2)    
    colorFromHypotenuse = mouseHypotenuse*255/totalHypotenuse
    
    colorPositions = {
                      "colorPositionX": colorPositionX,
                      "colorPositionY": colorPositionY,
                      "colorFromHypotenuse": colorFromHypotenuse,
                      "totalHypotenuse": totalHypotenuse
                      }                                        
    return colorPositions
        
def makeGrid():
    global nCols, nRows, grid    
    for i in range(nRows):
        grid.append([])
        for j in range(nRows):
            grid[i].append(0)
    return grid
    
class Cell():
    def __init__(self, celli, cellj, cellX, cellY, cellW, cellH, r, g, b ):
        self.i = celli
        self.j = cellj
        self.x = cellX
        self.y = cellY
        self.w = cellW
        self.h = cellH        
        self.r = r
        self.g = g
        self.b = b
        
    def colorCell(self):
        cellPositions = colorFromPosition(self.x, self.y)
        ## print cellPositions
        
        ## if statements for switching color template based on mouse directionality
        # if mouseX != pmouseX and mouseY == pmouseY : ## This one was too sensitive since a pixel different technically counts
        # if abs(mouseX-pmouseX)>width/100 and abs(mouseY-pmouseY)<=height/100 :
        # elif abs(mouseX-pmouseX)<=width/100 and abs(mouseY-pmouseY)>height/100 :
        # elif abs(mouseX-pmouseX)>width/200 and abs(mouseY-pmouseY)>height/200 :

        # if mousePressed :
        #     # mouseToggled()
        #     print mouseToggled
        
        # if mouseToggled==True :
        #     self.r = 0
        #     self.g = 0
        #     self.b = 0
        
        self.r = cellPositions['colorPositionY']
        self.g = cellPositions['colorFromHypotenuse']
        self.b = cellPositions['colorPositionX']      
        if key == CODED:                        
            if keyCode == LEFT:
                self.r = cellPositions['colorFromHypotenuse']
                self.g = cellPositions['colorPositionY']
                self.b = cellPositions['colorPositionX']
            elif keyCode == UP:
                self.r = cellPositions['colorPositionX']
                self.g = cellPositions['colorFromHypotenuse']
                self.b = cellPositions['colorPositionY']
            elif keyCode == RIGHT:
                self.r = cellPositions['colorPositionY']
                self.g = cellPositions['colorPositionX']
                self.b = cellPositions['colorFromHypotenuse']                                        
            elif keyCode == DOWN:
                # self.r = 0
                # self.g = 0    
                # self.b = 0        
                
                self.r = cellPositions['colorPositionY']
                
                # self.r = 255
                # self.g = 255  
                self.b = 255
                
                # self.r = cellPositions['colorFromHypotenuse']
                self.g = cellPositions['colorFromHypotenuse']
                # self.b = cellPositions['colorFromHypotenuse']    
            # elif keyCode == 's' or keyCode == 'S':
            #     time = datetime.datetime.now()
    
            #     time = re.sub(" ", ".", str(time))
            #     fileName= "rgb-cell-map-and-identifier.%s.png" %(time)
                
            #     print "Currently located in : %s" %(os.getcwd())
            #     print "Saving as : %s" % fileName
            #     saveFrame(fileName)
            # else:
                # pass            
        else:
            pass
            # self.r = cellPositions['colorPositionY']
            # self.g = cellPositions['colorFromHypotenuse']
            # self.b = cellPositions['colorPositionX']       
                        
    def display(self):
        stroke(0)
        fill(self.r, self.g, self.b)
        # print(self.r, self.g, self.b)
        rect(self.x, self.y, self.w, self.h)
        
    def cellGlow(self, selectedX, selectedY):        
        selectedX = selectedX
        selectedY = selectedY
        # if (mouseX >= self.x and mouseX < self.x + self.w) and (mouseY >= self.y and mouseY < self.y + self.h) :
        
        ## if the position selected by dragging the mouse is in within the cell's domain 
        cellSelected = (selectedX >= self.x and selectedX < self.x + self.w) and (selectedY >= self.y and selectedY < self.y + self.h)
        if mouseToggled==True :
            if cellSelected == True:
                # print "Cell[%s][%s] : RGB(%s, %s, %s)" %(self.i,self.j, self.r, self.g, self.b)   
                fill(255, 255, 255)            
                rect( self.x, self.y,  self.w,  self.h)
                fill(self.r, self.g, self.b)
                
                if width <= height:
                    border = self.w*0.1
                else:
                    border = self.h*0.1
                rect( self.x+border, self.y+border,  self.w-border*2,  self.h-border*2)            
                fill(255, 255, 255)
                
                textSize(border*2)
                text(int(round(self.r)), self.x+border*2, self.y + self.h*0.35)
                text(int(round(self.g)), self.x+border*2, self.y + self.h*0.55)
                text(int(round(self.b)), self.x+border*2, self.y + self.h*0.75)
                
                # rect( self.x+self.w*0.1, self.y+self.h*0.1,  self.w*0.8,  self.h*0.8)
                # ellipseMode(CORNER)
                # ellipse( self.x, self.y,  self.w,  self.h)
                # self.r = 255
                # self.g = 255
                # self.b = 255
        

    
