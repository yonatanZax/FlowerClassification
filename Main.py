

import os
from datetime import datetime

import copy

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from Configuration import ConfigClass

import threading

from BasicMethods import writeListToFile, getDicFromFile, get2DArrayFromFile

config = None

def main():

    mainManager = MainClass()
    mainManager.GUIRun()








class MainClass:

    def __init__(self, config=None):

        if config is None:
            self.config = ConfigClass()
        else:
            self.config = config


    def GUIRun(self):
        from Gui import GuiMainView

        print("***   Main Start   ***")
        root = GuiMainView.Tk()
        root = GuiMainView.setWindowSizeAndPosition(root)
        root.title("Flower Classification")

        guiFrame = GuiMainView.FlowerGui(root, config=self.config)
        guiFrame.mainloop()







if __name__ == "__main__":
    main()