### 444
class kolor:
    r = 0
    g = 0
    b = 0

white = kolor()
white.r = 255
white.g = 255
white.b = 255

### 450
class kolor:
    r = 0
    g = 0
    b = 0
    def __init__(self, r, g, b):
	self.r = r
	self.g = g
	self.b = b
	
white = kolor(255, 255, 255)
green = kolor(0, 255, 0)
blue = kolor(0, 0, 255)
print (blue)

### 460
class kolor:
    r = 0
    g = 0
    b = 0
    def __init__(self, r, g, b):
	self.r = r
	self.g = g
	self.b = b
    def __str__(self):
	return 'red: ' + str(self.r) + ', green: ' + str(self.g) + ', blue: ' + str(self.b)

white = kolor(255, 255, 255)
green = kolor(0, 255, 0)
blue = kolor(0, 0, 255)
print (blue)


