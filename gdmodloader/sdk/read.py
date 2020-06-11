import gd.memory
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    pass

def get_percent():
    return memory.get_percent()

def get_resolution():
    return memory.resolution()

def get_level_id_fast():
    return memory.get_level_id_fast()

def get_user_name():
    return memory.get_user_name()

def is_dead():
    return memory.is_dead()

def get_object_count():
    return memory.get_object_count()

def get_level_length():
    return memory.get_level_length()

def get_x_pos():
    return memory.get_x_pos()

def get_y_pos():
    return memory.get_y_pos()
    
def get_speed_value():
    return memory.get_speed_value()

def get_speed():
    return memory.get_speed()
    
def get_size():
    return memory.get_size()
    
def get_gravity():
    return memory.get_gravity()
    
def get_level_id():
    return memory.get_level_id()
    
def get_level_name():
    return memory.get_level_name()
    
def get_level_creator():
    return memory.get_level_creator()
    
def get_editor_level_name():
    return memory.get_editor_level_name
    
def get_level_stars():
    return memory.get_level_stars
    
def is_level_demon():
    return memory.is_level_demon()
    
def is_level_auto():
    return memory.is_level_auto()
    
def get_level_diff_value():
    return memory.get_level_diff_value()
    
def get_level_demon_diff_value():
    return memory.get_level_demon_diff_value()

def get_level_difficulty():
    return memory.get_level_difficulty()
    
def get_attempts():
    return memory.get_attempts()
    
def get_jumps():
    return memory.get_jumps()
    
def get_normal_percent():
    return memory.get_normal_percent()
    
def get_practice_percent():
    return memory.get_practice_percent()
    
def get_level_type_value():
    return memory.get_level_type_value()
    
def get_level_type():
    return memory.get_level_type()
    
def is_in_level():
    return memory.is_in_level()
    
def get_song_id():
    return memory.get_song_id()
    
def get_attempt():
    return memory.get_attempt()