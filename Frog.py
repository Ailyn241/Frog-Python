class Frog:
    
    def __init__(self,x,y,w,h):
        self.x = x #400
        self.y = y #300
        self.width = w #30
        self.height = h #30
        
    def paint(self,w):
        w.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,fill="green")