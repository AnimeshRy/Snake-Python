import turtle
import os
import time
import random

"""Snake game"""
score = 0
high_score = 0
delay = 0.1


wn = turtle.Screen()
wn.title('Snakyyyy')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)  # turns off the screen updates

# snake heads
head = turtle.Turtle()
head.speed(0)  # animation speed set to fastest
head.shape('square')
head.color('black')
head.penup()  # does not draw any lines
head.goto(0, 0)
head.direction = "stop"  # starts in the middle when the game begins

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 High Score: 0', align="center",
          font=("Courier", 18, "normal"))

# function


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def close():  # quit
    global running
    running = False


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(close, "q")
running = True

# main loop
while running:
    wn.update()

    # check for border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        # score reset
        pen.clear()
        score = 0
        pen.write('Score: {} High Score: {}'.format(score, high_score), align="center",
                  font=("Courier", 18, "normal"))
        delay = 0.1
    # check for collision

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)  # random x and y coordinates

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed()
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write('Score: {} High Score: {}'.format(score, high_score), align="center",
                  font=("Courier", 18, "normal"))

    # move the end segment first in reverse order
    # all the segments move to the previous one's index
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            # score reset
            pen.clear()
            score = 0
            pen.write('Score: {} High Score: {}'.format(score, high_score), align="center",
                      font=("Courier", 18, "normal"))
            delay = 0.1

    time.sleep(delay)  # to delay the update screen
