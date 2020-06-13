import gd
import time
import subprocess
def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call, shell=True).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())
while True:
    try:
        memory = gd.memory.get_memory()
    except RuntimeError:
        print("GD is not running!")
    else:
        import gdmodloader.loader
        gdmodloader.loader.start_loader()
        print("Loaded mods!")
        while True:
            if process_exists("GeometryDash.exe") == False:
                print("Game closed")
                break
    time.sleep(5)