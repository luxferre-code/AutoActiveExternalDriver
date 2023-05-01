import os, sys
from functions import *

if __name__ != "__main__": 
    print("This is not a module. Please run AAED.py directly.")
    sys.exit(1)

if(len(sys.argv) != 3):
    print("Usage: python AAED.py <path of external driver> <to>")
    sys.exit(1)

external_driver_path: str = sys.argv[1]
to: str = sys.argv[2]

if(not os.path.exists(to)):
    print("Error: Destination path does not exist.")
    sys.exit(1)

drivers = Drivers()
to_mount: list = []

for driver in drivers.get():
    if(driver.__contains__(external_driver_path)):
        to_mount.append(driver)
        
for driver in to_mount:
    print("Mounting " + driver + "...")
    os.system("sudo mount /dev/" + driver + " " + to)

print("Done.")