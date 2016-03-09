image = makePicture("C:/Users/Aromas197/Desktop/Rainbow.jpg")
redList = []
greenList = []
blueList = []
noteList = []
width = getWidth(image)
height = getHeight(image)
blank = makeEmptyPicture(width, height)
a = -1
for y in range(0,height):
  for x in range(0,width):
    pixel = getPixel(image, x, y)
    newPixel = getPixel(blank, x, y)
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    redList.append(r)
    greenList.append(g)
    blueList.append(b)
    a = a + 1
    redValue = redList[a]
    greenValue = greenList[a]
    blueValue = blueList[a]
    noteList.append((r+g+b)/5)
    if(a > 0):
      if(noteList[a]-noteList[a-1]>0):
        playNote(noteList[a], 10, 64)
    setRed(newPixel, redValue)
    setGreen(newPixel, greenValue)
    setBlue(newPixel, blueValue)
    repaint(blank)