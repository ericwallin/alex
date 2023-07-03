#! /usr/bin/python3
import sys
import time
from datetime import datetime

def print_time_date(times, firstTime):
    if times == 0:
        while True:
            if firstTime == False:
                time.sleep(1)

            print (datetime.now(), flush=True)
            firstTime = False
    else:
        for _ in range(times):
            if firstTime == False:
                time.sleep(1)

            print(datetime.now(), flush=True)
            firstTime = False

def main():
    if len(sys.argv) != 2:
        print_time_date(1, True)
    else:
        try:
            arg = int(sys.argv[1])
            print_time_date(arg, True)
        except ValueError:
            print(f"Invalid argument: {sys.argv[1]}. Argument should be an integer.")
            sys.exit(1)

if __name__ == "__main__":
    main()
