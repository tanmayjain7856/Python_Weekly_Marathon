# Link for exercise
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

#Function for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Function for clearing a hurdle
def cross_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        cross_hurdle()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################