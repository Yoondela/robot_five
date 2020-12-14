from world import obstacles

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
obsts = obstacles.get_obstacles()
blocked = False

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
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
    return False

def is_position_allowed(new_x, new_y):
    
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    # a = False
    # if obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False:
    #     a = True
    #     return False
    # if obstacles.is_position_blocked(new_x,new_y):
    #     print("Sorry, There is an obstacle in the way to the position")
    #     return False
    # elif obstacles.is_position_blocked(new_x, new_y) == False or a == False:

    global blocked
    blocked = False
    if obstacles.is_position_blocked(new_x, new_y):
        blocked = True
        return False
    if obstacles.is_path_blocked(position_x, position_y, new_x,new_y):
        blocked = True 
        return False
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def show_text_obstacles():
    sorted_obstacles = sort_obstacles()
    print("There are some obstacles:")
    for i in sorted_obstacles:
        print("- At position {},{} (to {},{})".format(i[0][0],i[0][1], i[1][0],i[1][1]))

def sort_obstacles():
    pairs = []
    pairs.append([(obsts[0]), (obsts[1])])
    pairs.append([(obsts[2]), (obsts[3])])
    pairs.append([(obsts[4]), (obsts[5])])
    pairs.append([(obsts[6]), (obsts[7])])
    pairs.append([(obsts[8]), (obsts[9])])
    pairs.append([(obsts[10]), (obsts[11])])
    pairs.append([(obsts[12]), (obsts[13])])
    pairs.append([(obsts[14]), (obsts[15])])
    pairs.append([(obsts[16]), (obsts[17])])
    pairs.append([(obsts[18]), (obsts[19])])
    return pairs