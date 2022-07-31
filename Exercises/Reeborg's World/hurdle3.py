# Link for exercise
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#Function for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Function for moving left    
def move_left():
    turn_left()

#Function for moving right    
def move_right():
    move()
    turn_right()

#Function for clearing a hurdle
def cross_hurdle():
    move_left()
    move_right()
    move_right()
    move()
    move_left()

while at_goal() != True:
    if wall_in_front():
        cross_hurdle()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################