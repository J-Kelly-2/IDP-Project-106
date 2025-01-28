#main script of the robot
import Motor from motor
import LineSensor from linesensor

motor_left = Motor()
motor_right = Motor()

#assuming 4 sensors in a row as kevin suggested

flls = LineSensor() #far left line sensor
lls = LineSensor() #left line sensor
rls = LineSensor()
frls = LineSensor()

def find_type_of_line(): #tells us if we are on a line, veering off, at a junction(left,right,T)
    if flls == 0 and lls == 0 and rls == 0 and frls == 0:
        return 'OFFTHEGRID'
    
    #then other logic that turns the bot

def move_forward():
    pass

def turn(direction):
    pass

def adjust(direction):
    pass
#main loop:
while True:
    state = find_type_of_line() #where robot is
    match state:
        case 'OFFTHEGRID':
            break
        case 'LINE':
            move_forward()
        case 'RIGHTOFFLINE':
            adjust('right')