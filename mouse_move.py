import pyautogui
import time
import subprocess
import datetime

TIME_IN_HOURS = 4
TIME_IN_MINUTES = 0

CALC_TIME = int(((TIME_IN_HOURS * 60) + TIME_IN_MINUTES) / 3)
begin_time = datetime.datetime.now()


def mouse_run(timerange, shutdown=False):
    iteration = 0

    for _ in range(timerange):
        pyautogui.FAILSAFE = False
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.click(500, 350, button='right')
        pyautogui.click(400, 550, button='left')

        iteration += 1
        print(f"Iteration # {iteration} of {CALC_TIME} and 'work time' is {round(iteration / 0.333 / 60, 2)} h.")

        time.sleep(180)

    print("Done")
    print(datetime.datetime.now() - begin_time)

    if shutdown:
        cmd = "shutdown -h"
        subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)


# mouse_run(CALC_TIME, True)
mouse_run(CALC_TIME)
