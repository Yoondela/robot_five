import turtle
import world.obstacles as obstacles

# from world.text import world as a

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -150, 150
min_x, max_x = -250, 250
bob = turtle.Turtle()
obsts = obstacles.get_obstacles()
blocked = False

# s = turtle.Screen()

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    return robot_name


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
    
    while True:
        if directions[current_direction_index] == 'forward':
            new_y = new_y + steps
        elif directions[current_direction_index] == 'right':
            new_x = new_x + steps
        elif directions[current_direction_index] == 'back':
            new_y = new_y - steps
        elif directions[current_direction_index] == 'left':
            new_x = new_x - steps
        if is_position_allowed(new_x, new_y):
            position_x = new_x
            position_y = new_y
            return True
        else:
            return False
        turtle.done()
        return False

def is_position_allowed(new_x, new_y):
    
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    global blocked
    blocked = False
    if obstacles.is_position_blocked(new_x, new_y):
        blocked = True
        return False
    if obstacles.is_path_blocked(position_x, position_y, new_x,new_y):
        blocked = True 
        return False
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def draw_border():
    y = turtle.Turtle()
    y.penup()
    y.pensize(4)
    y.pencolor("green")
    y.setposition(-150, -250)
    y.pendown()
    y.forward(300)
    y.left(90)
    y.forward(500)
    y.left(90)
    y.forward(300)
    y.left(90)
    y.forward(500)
    y.hideturtle()

obstacle = obstacles.obstacles
def draw_obstacles():
    pencil = turtle.Turtle()
    for obst in obstacle:
        if obst[1] > 0:
            y = -obst[1]
        else:
            y = obst[1] * -1
        x = obst[0]
        pencil.penup()
        pencil.setposition(x,y)
        pencil.pensize(5)
        pencil.pencolor("green")
        pencil.pendown()
        pencil.hideturtle()
        pencil.speed(0)
        for i in range(4):
            pencil.forward(5)
            pencil.left(90)

draw_border()# calling
draw_obstacles()
