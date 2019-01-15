daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
import turtle
 #pixel pra
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
 
 
# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
                
 
boxSize = 5       
#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)
 
 
##Here is an example of how to draw a box        
#box(boxSize)
 
 
##Here are some instructions on how to move "myPen" around before drawing a box.
#myPen.setheading(0) #point to the right, 90 to go up, 180 to go to the left 270 to go down
#myPen.penup()
#myPen.forward(boxSize)
#myPen.pendown()
 
#Here is how your PixelArt is stored (using a "list of lists")
colourPalette=["#ffffff","#EA67F3","#000000","#278B1B","#EA051C","#FAEE1C","#D059DB"]
pixels =     [[0,0,0,0,0,1,3,3,1,1,3,3,1,0,0,0,0,0]]
pixels.append([0,0,0,0,0,1,3,2,1,1,2,3,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,4,4,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,4,4,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,4,1,1,1,1,4,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,4,0,4,4,4,4,0,4,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,4,0,0,0,0,4,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,4,4,4,4,1,1,0,0,0,0,0])
pixels.append([1,1,1,1,6,1,1,1,1,1,1,1,1,6,1,1,1,1])
pixels.append([1,5,1,1,6,5,5,1,1,5,1,1,1,6,1,1,5,1])
pixels.append([1,1,1,1,6,5,5,1,1,1,1,1,1,6,1,1,1,1])
pixels.append([1,1,5,1,6,1,1,1,1,1,1,1,1,6,1,5,1,1])
pixels.append([1,1,1,1,6,5,1,1,5,5,1,1,1,6,1,1,1,1])
pixels.append([1,1,5,5,6,1,1,1,5,5,1,1,5,6,5,1,1,1])
pixels.append([1,1,5,5,6,1,1,1,1,1,1,1,5,6,5,1,1,1])
pixels.append([1,5,1,1,6,5,5,1,1,1,1,5,1,6,1,5,1,1])
pixels.append([1,1,5,1,6,5,5,1,1,5,5,1,1,6,5,1,1,1])
pixels.append([6,6,6,6,6,1,1,1,1,5,5,1,1,6,6,6,6,6])
pixels.append([1,1,1,1,6,1,1,5,1,1,1,1,1,6,1,1,1,1])
pixels.append([1,1,1,1,6,1,1,1,1,1,1,5,1,6,1,1,1,1])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,5,5,1,1,5,5,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,5,5,1,1,5,5,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,5,1,1,1,1,1,1,5,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,5,5,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,5,5,1,1,5,5,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,5,5,1,1,5,5,1,0,0,0,0,0])
pixels.append([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0])


for i in range (0,len(pixels)):
    for j in range (0,len(pixels[i])):
                                myPen.color(colourPalette[pixels[i][j]])
                                box(boxSize)
                                myPen.penup()
                                myPen.forward(boxSize)
                                myPen.pendown()         
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()
