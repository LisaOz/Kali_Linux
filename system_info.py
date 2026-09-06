import platform
import socket
import os
import getpass

print ("=" * 50)
print("SYSTEM IMFORMATION COLLECTOR")
print("=" * 50)

print (f"Operating System: {platform.system()}")
print (f"OS Version: {platform.version()}")
print (f"Hostname: {socket.gethostname()}")
print (f"Current User: {getpass.getuser()}")
print (f"Current Directory: {os.getcwd()}")
print (f"Python Version: {platform.python_version()}")
print (f"Machine Architecture: {platform.machine()}")

print ("=" * 50)
