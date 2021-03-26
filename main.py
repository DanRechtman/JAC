from pyautogui import click,position,leftClick
import sys

class Click(object):

    def __init__(self,move=False):
        self.move = move
    def click(self):
        if (self.move):
            self.pos = position()
            while self.pos == position():
                click(clicks=10)
        else:
            #TODO: Implement the click function when move is false
            print("Not implemented")


if __name__ == "__main__":
    c = Click(move=True)
    c.click()
        