import random


occupied = []
y_change = False

def generate_obstacles():
    obstacles = []
    for i in range(10):
        x = random.randint(-150, 150)
        y = random.randint(-250, 250)
        obstacles.append((x,y))
    return obstacles

obstacles = generate_obstacles()

def is_position_blocked(y,x):
    pos = (y,x)
    for i in range(len(obstacles)):
        obstacle = obstacles[i]
        helper(obstacle)
    if pos in occupied:
        return True
    else:
        return False


def helper(obstacle):
    global occupied, y_change
    (x,y) = obstacle
    x_marker = x
    
    for i in range(5):
        for j in range(5):
            occupied.append((y,x))              
            if y_change:
                x = x_marker
                occupied.append((y,x))
                y_change = False
            x = x + 1
        y = y - 1
        y_change = True


def is_path_blocked(y1,x1,y2,x2):
    start = (y1,x1)
    end = (y2,x2)
    start_y = start[0]
    end_y = end[0]
    start_x = start[1]
    end_x = end[1]
    blocked = False
    if start_y <= end_y:
        for i in range(start_y, end_y+1):
            if start_x <= end_x:
                for j in range(start_x, end_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    if (start_y,start_x) in occupied:
                        blocked = True
                    # print("{},{}".format(start_y, start_x))

            elif start_x > end_x:
                for j in range(end_x, start_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    # print("this is start_y/x TWO {}".format(start_y,start_x))
                    if (start_y,start_x) in occupied:
                        blocked = True
            #         print("{},{}".format(start_y, start_x))
            # print("{},{}".format(start_y, start_x))



            if start_y < end_y:
                start_y = start_y + 1
            elif start_y > end_y:
                start_y = start_y - 1
            if (start_y, start_x) in occupied:
                blocked = True

    elif start_y > end_y:
        for i in range(end_y, start_y+1):
            if start_x <= end_x:
                for j in range(start_x, end_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    # print("this is start_y/x THREE {}".format(start_y,start_x))
                    if (start_y,start_x) in occupied:
                        blocked = True
                    # print("{},{}".format(start_y, start_x))

            elif start_x > end_x:
                for j in range(end_x, start_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    # print("this is start_y/x FOUR {}".format(start_y,start_x))
                    if (start_y,start_x) in occupied:
                        blocked = True
                #     print("{},{}".format(start_y, start_x))
                # print("{},{}".format(start_y, start_x))

            if start_y < end_y:
                start_y = start_y + 1
            elif start_y > end_y:
                start_y = start_y - 1
            if (start_y, start_x) in occupied:
                blocked = True
    return blocked


def get_obstacles():
    end_obstacle = []
    for i in obstacles:
        st_x = i[0]
        st_y = i[1]
        end_obstacle.append((st_y,st_x))
        y = i[0] + 4
        x = i[1] - 4
        end_obstacle.append((x,y))
    return end_obstacle