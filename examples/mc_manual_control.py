#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script show control Z when hovering by means of MotionCommander class.
"""
import logging
import time
import curses
import sys

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/80/250K'
# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

TIME_SEC = 1
Z_STEP = 0.3
X_STEP = 0.5
Y_STEP = 0.5
CW_STEP = 90

def main():

    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        damn = curses.initscr()
        damn.nodelay(1)
        curses.noecho()

        # We take off when the commander is created
        print("\rStart motion commander:")
        print("\r  u/d - up/down")
        print("\r  l/r - left/right")
        print("\r  f/b - forward/back")
        print("\r  c/w - turn left/right 90 degrees")
        print("\r  i/I - circle left/right 360 degrees")
        print("\r  q - quit")

        with MotionCommander(scf) as mc:
            time.sleep(TIME_SEC)

            while True:
                c = damn.getch()
                if c == ord('u'): # u - up
                    mc.up(Z_STEP)
                elif c == ord('d'): # d - down
                    mc.down(Z_STEP)
                elif c == ord('l'): # l - left
                    mc.left(X_STEP)
                elif c == ord('r'): # r - right
                    mc.right(X_STEP)
                elif c == ord('f'): # f - forward
                    mc.forward(X_STEP)
                elif c == ord('b'): # b - backward
                    mc.back(X_STEP)
                elif c == ord('w'): # clockwise
                    mc.turn_right(CW_STEP)
                elif c == ord('c'): # counter clockwise
                    mc.turn_left(CW_STEP)
                elif c == ord('i'):
                    mc.circle_left(0.3)
                elif c == ord('I'):
                    mc.circle_right(0.3)
                elif c == ord('q'): # q - quit
                    break

            curses.echo()
            curses.endwin()

if __name__ == '__main__':
    main()
