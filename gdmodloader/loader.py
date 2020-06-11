import gd
import os
import gdmodloader.errors
import gdmodloader.sdk
class Loader:
    def __init__(self):
        try:
            self.memory = gd.memory.get_memory()
        except RuntimeError:
            pass
        self.localappdata = os.getenv("localappdata") + "\\GeometryDash\\"
        self.mods = os.listdir(f"{self.localappdata}mods\\")
    def load(self):
        for mod in self.mods:
            modpath = self.localappdata + "mods\\" + mod
            if mod.endswith(".dll"):
                self.memory.inject_dll(modpath)
            elif mod.endswith(".py"):
                f = open(modpath, "r")
                gdmodloader.sdk.main(f.read())
def start_loader():
    MOD_LOADER_DIR = os.getenv("localappdata") + "\\.gdmodloader\\"
    if not os.path.exists(MOD_LOADER_DIR):
        os.mkdir(MOD_LOADER_DIR)
    loader = Loader()
    loader.load()