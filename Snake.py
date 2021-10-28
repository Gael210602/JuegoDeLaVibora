"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""
import random

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
food_count = 0

colors = ["blue", "orange", "yellow", "green", "black"]


def move_food():
    global food_count
    if food_count == 25:
        if random.choice([True, False]):
            if food.x == 150:
                food.x = food.x - 10
            elif food.x == -150:
                food.x = food.x + 10
            else:
                if random.choice([True, False]):
                    food.x = food.x - 10
                else:
                    food.x = food.x + 10
            food_count = 0
        else:
            if food.y == 150:
                food.y = food.y - 10
            elif food.y == -150:
                food.y = food.y + 10
            else:
                if random.choice([True, False]):
                    food.y = food.y - 10
                else:
                    food.y = food.y + 10
            food_count = 0


def selectRandom(colors):
    color = random.choice(colors)
    colors.remove(color)
    return color


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    global food_count
    food_count += 1
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_col)
    move_food()
    square(food.x, food.y, 9, food_col)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")
snake_col = selectRandom(colors)
food_col = selectRandom(colors)
move()
done()