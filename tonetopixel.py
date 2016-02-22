image = makePicture("C:/Users/aeria_000/Desktop/CST205/Projects/Project2/(7).jpeg")
note=[]
width = getWidth(image)
height = getHeight(image)
for x in range(0,width):
  for y in range(0,height):
     pixel = getPixel(image, x, y)    
      
     myRed = getRed(pixel)
     myGreen = getGreen(pixel)
     myBlue = getBlue(pixel)
     
     note.append((myRed + myGreen + myBlue)/5)

end=len(note)-1
speed = 1000
for i in range(1,end):
  if(note[i]-note[i-1]>5):
    playNote(note[i],speed,64)
    
#draw the picture as it is playing.