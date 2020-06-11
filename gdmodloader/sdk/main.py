import gd.memory
try:
    memory = gd.memory.get_memory()
except RuntimeError:
    pass
def main(code):
    exec(code)

def reload_memory():
    memory.reload()