from tkinter import *
import time
import keyboard
from Car import *
from Frog import *
from Lane import *

tk = Tk()
canvas = Canvas(tk, width = 800, height = 400)
canvas.pack()


start_x = 50
separator_x = 10
frog=Frog(400, 300, 30, 30)
# lane=Lane(0, 50, 800, 70, 5, speed=5, color="red")

lane_start_x = 0
lane_start_y = 50
lane_width = 800
lane_height = 70

lanes = []
for i in range(3):
    lanes.append(Lane(lane_start_x, lane_start_y + lane_height * i, lane_width, lane_height, 5, "red", speed=5))

#TASK 1: Do not allow the Frog to go out from the screen
#TASK 2:
#   - Add a background color to a lane
#   - Create 3 Lanes and store them in a List (like before the list of cars)
#   - Move the class Lane to another file -> "Lane.py"
#   - When a car reaches the last X of the Lane, reposition it to the 
#        beginning  of the lane. (Just change the X of the car)

while True:
    canvas.delete("all")
    for ls in lanes:
        ls.moveVehicles()
        ls.paint(canvas)
    
    if keyboard.is_pressed("up arrow"):
        if frog.y - 5 > 0:  #avoid going out the screen
            frog.y -= 5   #equivalent to frog_y=frog_y-1
    if keyboard.is_pressed("left arrow"):
        if frog.x - 5 > 0:
            frog.x -= 5   
    if keyboard.is_pressed("right arrow"):
        if frog.x + frog.width + 5 < 800:
            frog.x += 5   
    if frog.y<=0:
        print("Top reached")
    frog.paint(canvas)
    canvas.update()  #paints on the screen
    time.sleep(50/1000)