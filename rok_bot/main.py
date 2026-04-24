import os
import sys
from pathlib import Path

# Ensure imports and relative paths (assets/, adb) work when launched from any cwd
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
os.chdir(_ROOT)

from core.bot import RoKBot

def main():
    print("========================================")
    print("   Rise of Kingdoms Autonomous Bot      ")
    print("========================================")
    
    # Check for connected devices
    bot = RoKBot()
    devices = bot.adb.get_devices()
    
    if not devices:
        print(
            "Error: No ADB devices found. Install Android Platform Tools, add adb "
            "to PATH, enable USB debugging, and connect an emulator or device."
        )
        return

    print(f"Connecting to: {devices[0]}")
    bot.adb.serial = devices[0]
    
    bot.start()

if __name__ == "__main__":
    main()
