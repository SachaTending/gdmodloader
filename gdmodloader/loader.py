import gd
import os
import gdmodloader.sdk
import threading
class Loader:
    def __init__(self):
        try:
            self.memory = gd.memory.get_memory() # initalize memory, if something goes wrong, pass
        except RuntimeError:
            pass
        # this just adds some variables that are useful
        self.localappdata = os.getenv("localappdata") + "\\GeometryDash\\" 
        self.modlist = os.listdir(f"{self.localappdata}mods\\")
    def load(self):
        for mod in self.modlist:
            modpath = self.localappdata + "mods\\" + mod
            if mod.endswith(".dll"):
                self.memory.inject_dll(modpath)
            elif mod.endswith(".py"):
                f = open(modpath, "r")
                t = threading.Thread(target=gdmodloader.sdk.main, args=(f.read))
                t.setDaemon(True)
                t.start()
def start_loader():
    MOD_LOADER_DIR = os.getenv("localappdata") + "\\.gdmodloader\\"
    if not os.path.exists(MOD_LOADER_DIR):
        os.mkdir(MOD_LOADER_DIR)
    # this creates the .gdmodloader path, but im not sure what to put in there yet
    MOD_DIR = os.getenv("localappdata") + "\\Geometry Dash\\mods\\"
    if not os.path.exists(MOD_DIR):
        os.mkdir(MOD_DIR)
    # this creates the mods directory for users to put their mods in
    loader = Loader()
    loader.load()
    # initalize the loader