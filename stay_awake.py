import pyautogui
import time


DEFAULT_TIME_INTERVAL_IN_SEC = 60
direction_delta = [[1, 0], [-1, 0], [0, 1], [0, - 1]]
move_ratio = 0.1

while(True):
    for each_direction in direction_delta:
        delta_x = each_direction[0] * move_ratio
        delta_y = each_direction[1] * move_ratio
        pyautogui.move(delta_x, delta_y)
        print("Mouse moved.")
        time.sleep(DEFAULT_TIME_INTERVAL_IN_SEC)