import subprocess
import os
import time
from PIL import Image
import io

class ADBClient:
    def __init__(self, serial=None):
        self.serial = serial
        self.adb_path = "adb" # Assumes adb is in PATH

    def run_command(self, args):
        cmd = [self.adb_path]
        if self.serial:
            cmd.extend(["-s", self.serial])
        cmd.extend(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def tap(self, x, y):
        self.run_command(["shell", "input", "tap", str(x), str(y)])

    def swipe(self, x1, y1, x2, y2, duration=500):
        self.run_command(["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration)])

    def screen_cap(self):
        # Capture screen using adb and return as PIL Image
        # Using pipe for speed
        cmd = [self.adb_path]
        if self.serial:
            cmd.extend(["-s", self.serial])
        cmd.extend(["shell", "screencap", "-p"])
        
        result = subprocess.run(cmd, capture_output=True)
        if result.returncode != 0:
            return None
        
        # ADB screencap -p output often has \r\n on Windows which breaks PNG format
        # We need to clean the byte stream
        data = result.stdout.replace(b'\r\n', b'\n')
        return Image.open(io.BytesIO(data))

    def get_devices(self):
        output = self.run_command(["devices"])
        lines = output.splitlines()[1:]
        devices = [line.split()[0] for line in lines if "device" in line]
        return devices

if __name__ == "__main__":
    client = ADBClient()
    devices = client.get_devices()
    print(f"Devices found: {devices}")
    if devices:
        client.serial = devices[0]
        img = client.screen_cap()
        if img:
            print("Screenshot successful")
            img.save("test_cap.png")
