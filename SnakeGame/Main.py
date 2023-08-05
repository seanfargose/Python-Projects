from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)


food = Food()
snake = Snake()
scoreBoard = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
        


    #detect collisions using distancs method of python
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segments()
        scoreBoard.increaseScore()
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreBoard.reset()
        snake.reset()
        #game_is_on = False
        #scoreBoard.gameOver()
        
        
        
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()
            #game_is_on = True
            #scoreBoard.gameOver()

screen.exitonclick()

