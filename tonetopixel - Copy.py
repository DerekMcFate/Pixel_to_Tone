#Select Image to transform
image = makePicture(pickAFile())

#Retrive data from image
width = getWidth(image)
height = getHeight(image)
canvas = makeEmptyPicture(width,height)
use = makeEmptyPicture(1,1)
#setAllPixelsToAColor(canvas, black)

#declarations
note = 0
hold = getPixel(use, 0, 0)
setColor(hold, makeColor(255,255,255))
speed = 100


for x in range(0,width):
  for y in range(0,height):
     pixel = getPixel(image, x, y)
     newPixel = getPixel(canvas, x, y)
     color = getColor(pixel)
     myRed = getRed(pixel)
     myGreen = getGreen(pixel)
     myBlue = getBlue(pixel)
     
     holdColor = getColor(hold)   
     
     setColor(newPixel,color)
     print y
     repaint(canvas)
     note = ((myRed + myGreen + myBlue)/6)
     if(note < 127):
       if(color != holdColor):
          playNote(note,speed,64)
     setColor(hold,holdColor)
    
     