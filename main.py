from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong-Game")
screen.setup(width=800,height=600)
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score =Score()

screen.listen()
screen.onkeypress(r_paddle.paddle_up,"Up")
screen.onkeypress(r_paddle.paddle_down,"Down")
screen.onkeypress(l_paddle.paddle_up,"w")
screen.onkeypress(l_paddle.paddle_down,"s")

game_is_on  = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()


    # ! Detect collision with upper and lower wall
    if ball.ycor() >290 or ball.ycor() < -290:
        ball.bounce_y()
        
    # !Detect collision with paddle  

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330  or ball.distance(l_paddle) <50 and ball.xcor() < -330 : 
        ball.bounce_x()
        
        
    # !detect when paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()