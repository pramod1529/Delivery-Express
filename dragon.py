import turtle

turtle.speed(0) 
turtle.hideturtle() 
wn=turtle.Screen() 
wn.bgcolor("black") 
turtle.pencolor("red") 
 
def dragoncurve(l,n): 
  for i in range(1): 
    def x(n): 
            if n==0: 
                    return 
            x(n-1) 
            turtle.circle(-4, 90, 36) 
            y(n-1) 
            turtle.forward(l) 
    def y(n): 
            if n==0: 
                    return 
            turtle.forward(l) 
            x(n-1) 
            turtle.circle(4, 90, 36) 
            y(n-1) 
    turtle.fd(l) 
    x(n) 
dragoncurve(5,15)