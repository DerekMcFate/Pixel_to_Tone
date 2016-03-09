#Select Image to transform
image = makePicture(pickAFile())

#declarations
note = 0
hold = 0
speed = 50

#Retrive data from image
width = getWidth(image)
height = getHeight(image)
canvas = makeEmptyPicture(width,height)
#setAllPixelsToAColor(canvas, black)

for x in range(0,width):
  for y in range(0,height):
     pixel = getPixel(image, x, y)
     newPixel = getPixel(canvas, x, y)
     color = getColor(pixel)
     myRed = getRed(pixel)
     myGreen = getGreen(pixel)
     myBlue = getBlue(pixel)
     
     #newColor =  makeColor(myRed,myGreen,myBlue)
     setColor(newPixel,color)
     print y
     repaint(canvas)
     note = ((myRed + myGreen + myBlue)/6)
     if(note < 127):
       if (note - hold > 15):
         playNote(note,speed,64)
     hold = note
    
     