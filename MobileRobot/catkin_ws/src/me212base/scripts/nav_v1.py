# robot navigation for task b

import me212bot, apriltag_navi

# •	Check if task has been completed or not (or number of tasks left to be completed in queue)
# o	Input parameters: what tasks need to be completed
# ♣	Also possibly key words/start and stop commands (voice? image?) Dependent on Sensors team final design
# o	Return: either boolean or integer
def task_completed():

# •	Get current robot and motor positions, velocities
# o	Input: readings from vision and encoder
# ♣	Object center (coordinates) from vision
# ♣	Distance from object
# ♣	Past positions, velocities if possible
# ♣	0 if starting from standstill or “start” zone
# o	Return current robot and motor positions, velocities
def get_pos_vel():

# •	Find/calculate paths, return path for robot
# o	Input: object location/destination
# ♣	Current robot and motor positions, velocities from previous function
# ♣	Task to be completed
# o	Return: 0/null if not possible   Consider potential error states
# ♣	Otherwise return optimal path (shortest distance, no obstacles)
def calculate_path():

# •	Robot move (forward, backward), turn (left, right)
# o	Input: path from calculate path function above
# ♣	Task to be completed?
# o	Incorporate weighted average (50-50) of position/errors to output
# o	No return value, command robot to move
def bot_move():

# •	Arm base (joint) + gripper (open, close, twist or rotate)
# o	Input: position/velocities from vision and encoder values
# ♣	Grab current values, store them as well as past values
# o	No return value, command grabber to move
def gripper_move():

# •	Timing - record time to complete task (add an estimate of time to complete task?)
# o	Input: none
# o	Timer to record and store length of time to complete task
def timing():
