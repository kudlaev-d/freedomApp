import random

import pyautogui as pg

screenWidth, screenHeight = pg.size()
current_position: pg.Point = pg.position()

class Positions:
    @staticmethod
    def get_new_position():
        return random.randint(0, screenHeight), random.randint(0, screenWidth)

ps = Positions()

while True:
    new_x, new_y = ps.get_new_position()

    if new_x != current_position.x or new_y != current_position.y:
        pg.moveTo(new_x, new_y)
        break

pg.press('alt')

