from core.bot import RoKBot

def main():
    print("========================================")
    print("   Rise of Kingdoms Autonomous Bot      ")
    print("========================================")
    
    # Check for connected devices
    bot = RoKBot()
    devices = bot.adb.get_devices()
    
    if not devices:
        print("Error: No ADB devices found. Please connect your emulator.")
        return

    print(f"Connecting to: {devices[0]}")
    bot.adb.serial = devices[0]
    
    bot.start()

if __name__ == "__main__":
    main()
