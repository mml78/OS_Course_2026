#!/usr/bin/env python3

import os
import platform
import getpass

def main():

    # Extract and display OS name and kernel version
    sys_info = platform.uname()
    print(f"Operating System: {sys_info.system}")
    print(f"Kernel Version:   {sys_info.release}")
    print(f"Full Details:     {platform.platform()}")

    # Display the current logged-in user
    print(f"Current Logged-in User: {getpass.getuser()}")
  
    # Display the current working directory
    print(f"Current Working Directory: {os.getcwd()}")

if __name__ == "__main__":
    main()
