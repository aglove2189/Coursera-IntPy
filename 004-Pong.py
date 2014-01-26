# http://www.codeskulptor.org/#user23_zH7s62ZlbG5Ohb8_0.py

# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 15
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
vel = 6
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, score1, score2, RIGHT, LEFT # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
       ball_vel = [random.randrange(120, 240) / 50, random.randrange(60, 180) / 50]
    elif direction == LEFT:
       ball_vel = [-random.randrange(120, 240) / 50, random.randrange(60, 180) / 50]
     
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, RIGHT  # these are numbers
    global score1, score2  # these are ints
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    RIGHT = True
    spawn_ball(RIGHT)
    
def restart():
    global ball_vel, paddle1_pos, paddle2_pos, score1, score2
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    ball_vel = [0, 0]
    new_game()
        
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, LEFT, RIGHT
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (abs(paddle1_pos - ball_pos[1]) <= HALF_PAD_HEIGHT):
        ball_vel[0] = - ball_vel[0] * 1.1
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and (abs(paddle1_pos - ball_pos[1]) > HALF_PAD_HEIGHT):
        RIGHT = True
        spawn_ball(RIGHT)
        score2 += 1
        
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (abs(paddle2_pos - ball_pos[1]) <= HALF_PAD_HEIGHT):
        ball_vel[0] = - ball_vel[0] * 1.1
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and (abs(paddle2_pos - ball_pos[1]) > HALF_PAD_HEIGHT):
        RIGHT = False
        LEFT = True
        spawn_ball(LEFT)
        score1 += 1
        
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel
    
    if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    
    if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    elif paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw score
    c.draw_text(str(score1), (150,20), 20, "White")
    c.draw_text(str(score2), (450,20), 20, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += vel
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += vel    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 200)

# start frame
new_game()
frame.start()