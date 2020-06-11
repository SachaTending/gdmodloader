import gd.memory
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    pass

def set_x_pos(x):
    memory.set_x_pos(x)
    
def set_y_pos(y):
    memory.set_y_pos(y)

def set_pos(x, y):
    memory.set_x_pos(x)
    memory.set_y_pos(y)
    
def set_speed_value(value):
    memory.set_speed_value(value)
    
def set_size(size):
    memory.set_size(size)
    
def set_attempt(attempt):
    memory.set_attempt(attempt)