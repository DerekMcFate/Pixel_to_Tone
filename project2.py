#Select Image to transform
image = makePicture(pickAFile())

#list declaration
note = []
colorlist = []

#Retrive data from image
width = getWidth(image)
height = getHeight(image)
for x in range(0,width):
  for y in range(0,height):
  
     pixel = getPixel(image, x, y)  
     color = getColor(pixel)  
      
     myRed = getRed(pixel)
     myGreen = getGreen(pixel)
     myBlue = getBlue(pixel)
     
     note.append((myRed + myGreen + myBlue)/5)
     colorlist.append(color)

end=len(note)-1
speed = 1000

canvas = makeEmptyPicture(width,height)

for i in range(1,end):
  if(note[i]-note[i-1]>5):
  
    playNote(note[i],speed,64)
    setAllPixelsToAColor(canvas, colorlist[i])
    repaint(canvas)
    