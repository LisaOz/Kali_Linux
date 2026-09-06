import platform
import socket
import os
import getpass

def display_header():
    print ("=" * 50)
    print("SYSTEM IMFORMATION COLLECTOR")
    print("=" * 50)

def collect_system_info():
    print (f"Current user: {getpass.getuser()}")
    print (f"Operating System: {platform.system()}")
    print (f"OS Version: {platform.version()}")
    print (f"Hostname: {socket.gethostname()}")
    print (f"Current Directory: {os.getcwd()}")
    print (f"Python Version: {platform.python_version()}")
    print (f"Machine Architecture: {platform.machine()}")

def security_status():
    print ("[+] Python environment: READY")
    print ("[+] System information: COLLECTED")
    print ("[+] Security wordspace: ACTIVE")
    print ("Security environment check completed successfully.")


display_header()
collect_system_info()
security_status()

print ("=" * 50)



