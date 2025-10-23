# turtle game with GUI
import turtle
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox
class TurtleGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Turtle Catch Game")
        self.screen.setup(width=600, height=600)
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.penup()
        self.score = 0
        self.time_left = 30
        self.is_running = True

        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(-250, 260)
        self.update_score()

        self.time_display = turtle.Turtle()
        self.time_display.hideturtle()
        self.time_display.penup()
        self.time_display.goto(200, 260)
        self.update_time()

        self.screen.onclick(self.catch_turtle) # Bind mouse click to catch_turtle method and what onclick does is it listens for mouse clicks on the screen and calls the specified function when a click is detected

        threading.Thread(target=self.countdown).start() # Start countdown in a separate thread and what threading does is it allows multiple operations to run concurrently in the same program
        self.move_turtle()

        turtle.done() # Start the turtle graphics event loop and what done does is it tells the turtle graphics system to enter its main event loop, waiting for user interactions such as mouse clicks or key presses

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def update_time(self):
        self.time_display.clear()
        self.time_display.write(f"Time: {self.time_left}", font=("Arial", 16, "normal"))

    def move_turtle(self):
        if not self.is_running:
            return
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.turtle.goto(x, y)
        self.screen.ontimer(self.move_turtle, 1000) # Move turtle every second and what ontimer does is it sets a timer to call a function after a specified amount of time and in this case we are calling move_turtle again after 1000 milliseconds which is 1 second

    def catch_turtle(self, x, y):
        if not self.is_running:
            return
        if self.turtle.distance(x, y) < 20: # Check if click is within 20 pixels of turtle and what distance does is it calculates the distance between the turtle's current position and the point (x, y) where the user clicked
            self.score += 1
            self.update_score()

    def countdown(self):
        while self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
            self.update_time()
        self.is_running = False
        messagebox.showinfo("Game Over", f"Time's up! Your final score is {self.score}.")
        turtle.bye() # Close the turtle graphics window
if __name__ == "__main__":
    TurtleGame()