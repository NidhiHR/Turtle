from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("pong")
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.goup,"Up")
screen.onkeypress(r_paddle.godown,"Down")

screen.onkeypress(l_paddle.goup,"w")
screen.onkeypress(l_paddle.godown,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    

    #collision detection with wall
    if ball.ycor()> 280 or ball.ycor()<-280:
        #we need to bounce the ball
        ball.y_bounce()
    
    #collision of ball with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or  ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()

    #if right paddle misses ball
    if ball.xcor()>370:
        ball.reset()
        scoreboard.l_point()
        # scoreboard.update_scoreboard()

    if ball.xcor()<-370:
        ball.reset()
        scoreboard.r_point()
        # scoreboard.update_scoreboard()

screen.exitonclick()
