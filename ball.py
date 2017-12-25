class Ball:        
    def __init__(self,x=0,y=0,c=0,r=5,vx=0,vy=0,ay=0,grow=0,):
        self.x=x
        self.y=y
        self.c=c
        self.r=r        
        self.vx=vx
        self.vy=vy
        self.ay=ay
        self.grow=grow
        self.e=-1
        self.stale=0
        self.stalelimit=300
    
        
    def render(self):
        fill(self.c)
        ellipse(self.x,self.y,self.r,self.r)
        
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        
    def update(self):
        if (self.x+self.r)>width-1:
            self.x=width-1-self.r
            self.vx=self.e*self.vx
            
        if(self.x-self.r)<0:
            self.x=self.r
            self.vx=self.e*self.vx
            
        self.vy+=self.ay
        self.r+=self.grow
        
        
        
        if self.y+self.r>699 and self.y+self.r<705 and (self.x)>(mouseX) and (self.x)<(mouseX+100):
            self.y=699-self.r
            self.vy=self.vy*self.e
        
    
    
    def isStale(self):
        return self.stale>self.stalelimit
        
