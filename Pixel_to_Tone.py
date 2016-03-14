image = makePicture("C:/Users/Aromas197/Desktop/Black.jpg")
redList = []
greenList = []
blueList = []
noteList = []
width = getWidth(image)
height = getHeight(image)
blank = makeEmptyPicture(width, height)
a = -1
for y in range(0,height):
  counter = 0
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
    if(counter == 100):
      if(a > -1):
        playNote(noteList[a], 1, 64)
        counter = -1
    counter += 1
    setRed(newPixel, redValue)
    setGreen(newPixel, greenValue)
    setBlue(newPixel, blueValue)
    repaint(blank)