# http://www.codeskulptor.org/#user21_4vsRqDxBUR6cYHq.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
successful_stop = 0
total_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = t // 600
    second = (t % 600) // 10
    tenth_second = t % 10
    if second < 10:
        str_second = "0" + str(second)
    else:
        str_second = str(second)
    return str(minute) + ":" + str_second + "." + str(tenth_second)
  
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total_stop, successful_stop
    if timer.is_running():
        total_stop = total_stop + 1
        timer.stop()
        if time % 10 == 0:
            successful_stop = successful_stop + 1
    
def reset():
    global time, successful_stop, total_stop
    time = 0
    successful_stop = 0
    total_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [100, 100], 40, "red")
    canvas.draw_text(str(successful_stop) + "/" + str(total_stop), 
                     [250, 40], 20, "red")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
start_button = frame.add_button("Start", start, 200)
stop_button  = frame.add_button("Stop",  stop,  200)
reset_button = frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()