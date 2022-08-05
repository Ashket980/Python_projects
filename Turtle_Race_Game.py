import random, turtle

myscreen= turtle.Screen()

myscreen.bgcolor('light blue')
myscreen.setup(1.0,1.0)
myscreen.title('Turtle Race Game')

pen=turtle.Turtle()

pen.speed(0) # so it moves with fastest speed
pen.penup() #pen goes up as we don't want to draw on line.
pen.goto(-200,200) #this is x and y position from center of the screen
pen.pendown() # pen placed down again

for i in range(1,11): # this will run from 1 to 10 
	pen.write(i,font=('Arial',10)) #writing the race track number before each line
	pen.setheading(-90) #this will point pen in downward direction
	pen.forward(250) #draw a line of 250 pixels length.
	if i==10: # this if condition will be true only if the iterating variable is 10 
		pen.write(" FINISH",font=('Arial',14))
	pen.back(250) #goes back
	pen.penup() #pen goes up as we don't want to draw on line
	pen.setheading(0) #pen points in right direction
	pen.forward(50)  #space of 50 pixes between each line
	pen.down() #pen down again

finishLineX=250

def createTurtlePlayer(color, startx, starty): 
	player=turtle.Turtle()
	player.color(color) # set the color of turtle
	player.shape("turtle") #set the shape as turtle
	player.penup() #pen moves up
	player.goto(startx, starty) #place player at mentioned position on race track.
	player.pendown() #pen placed down
	return player #returns the turtle player object.

p1=createTurtlePlayer('red',-210,150) #red colored turtle at x position before 1st Line and y position 150
p2=createTurtlePlayer('blue',-210,100) #blue colored turtle at x position before 1st Line and y position 100
p3=createTurtlePlayer('orange',-210,50) #orange colored turtle at x position before 1st Line and y position 50
p4=createTurtlePlayer('green',-210,0) #green colored turtle at x position before 1st Line and y position 0

while True:
	p1.forward(random.randint(5,10))
	if p1.pos()[0]>=finishLineX:
		p1.write(' I won the race!!',font=('Arial',30))
		break
	p2.forward(random.randint(5,10))
	if p2.pos()[0]>=finishLineX:
		p2.write(' I won the race!!',font=('Arial',30))
		break
	p3.forward(random.randint(5,10))
	if p3.pos()[0]>=finishLineX:
		p3.write(' I won the race!!',font=('Arial',30))
		break
	p4.forward(random.randint(5,10))
	if p4.pos()[0]>=finishLineX:
		p4.write(' I won the race!!',font=('Arial',30))
		break

turtle.done()
