import os
import shutil

dir = os.path.dirname(os.path.realpath(__file__)) + "\\"
copyto = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
shutil.copy(dir + "start.pyw", copyto)
try:
    os.sytem("py" + dir + "start.pyw")
except:
    print("Failed to start modloader process, please restart your computer. You do not need to run the installer again.")