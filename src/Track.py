from math import sin,cos,pi
class Track():
    color = (0,255,0)
    lineColor = (255,255,255)
    ycoords = []
    xcoords = []
    loop = []
    border = []
    def __init__(self, display, width):#Modify this to be the equation of a semi random closed surface.
        points = list(range(display.height))
        self.loop = []
        for i in points:#Generate half
            sine = (sin(pi*i/(display.height-width))+1)
            cosine = (cos(pi*i/(display.height-width))+1)
            self.xcoords.append(int(display.width*sine/2))
            self.ycoords.append(int((display.height-2*width)*cosine/2+width/2))
            self.loop.append([self.xcoords[-1],self.ycoords[-1]+width])
        for i in points[::-1]:#Generate other half
            sine = (sin(-pi*i/(display.height-width))+1)
            cosine = (cos(pi*i/(display.height-width))+1)
            self.xcoords.append(int(display.width*sine/2))
            self.ycoords.append(int((display.height-2*width)*cosine/2+width/2))
            self.loop.append([self.xcoords[-1],self.ycoords[-1]+width])
        #loop = array(self.loop)
        for i in self.loop:
            if(i[1]>1/2*display.height):
                if(i[0]>1/2*display.width):
                    self.border.append([abs(i[0]-width),abs(i[1]-width)])
                else:
                    self.border.append([abs(i[0]+width),abs(i[1]-width)])
            else:
                if(i[0]>1/2*display.width):
                    self.border.append([abs(i[0]-width),abs(i[1]+width)])
                else:
                    self.border.append([abs(i[0]+width),abs(i[1]+width)])
        for i in self.loop[::-1]:
            self.border.append([abs(-i[0]),abs(i[1])])
        #print(self.loop)
    def render(self, pygame, display):
        pygame.draw.polygon(display, self.color, self.loop, width = 4)
        #pygame.draw.lines(display, self.lineColor, False, self.loop)
