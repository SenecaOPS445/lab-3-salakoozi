#!/usr/bin/env python3
# Purpose: The purpose of this script is to create a Python function that can return the free disk space on a Linux system's root directory.
# Author ID: salakoozi

import os

def free_space(): 
    output = os.popen("df -h | grep '/$' | awk '{print $4}'").read().strip() #This finally works, the issue was with the quotation
    return output

if __name__ == '__main__':
    print(free_space())
