import modloader

modloader.setup_logging()

try:
    state = modloader.create_state()
except RuntimeError:
    print("Geometry Dash is not running!")
    exit(1)

if state.inject_dll(input("Enter DLL path: ")):
    print("DLL successfully injected!")
else:
    print("Could not inject DLL.")
