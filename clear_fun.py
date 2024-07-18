import os
import platform

try:
    os_name = platform.system()
except Exception as e:
    print(f"OS not detected: {e}")
else:
    def clear():
        if os_name == "Linux":
            os.system("clear")
        elif os_name == "Darwin":
            os.system("clear")
        elif os_name == "Windows":
            os.system("cls")
        else:
            print("Your OS is not recognized.")