

import shutil
import string
import tkinter
from tkinter import *
from tkinter import filedialog

from threading import Thread

import os


from BasicMethods import get2DArrayFromFile , getDicFromFile
from Gui.TkinterTable import TableView


class FlowerGui(Frame):

    def __init__(self,master,config):
        self.master = master
        self.config = config

        Frame.__init__(self, master)
        self.grid()



        self.XstartPixel = 60
        self.YstartPixel = 10


        label_0 = Label(self.master, text="Flower Classification", width=20, font=("bold", 30))
        label_0.place( x = self.XstartPixel + 20, y = self.YstartPixel + 40)


        label_folderPath = Label(self.master, text="Folder path:", width=10, font=("bold", 10))
        label_folderPath.place( x = self.XstartPixel + 50, y = self.YstartPixel + 130)
        self.entry_folderPath_text = StringVar()
        # self.entry_folderPath_text.set(config.get__corpusPath())
        self.entry_folderPath = Entry(self.master, textvariable=self.entry_folderPath_text, width=30)
        self.entry_folderPath.place(x =self.XstartPixel + 180, y =self.YstartPixel + 130)


        label_modelPath = Label(self.master, text="Model path:", width=10, font=("bold", 10))
        label_modelPath.place( x = self.XstartPixel + 50,  y = self.YstartPixel + 160)
        self.entry_modelPath_text = StringVar()
        # self.entry_modelPath_text.set(config.get__savedFileMainFolder())
        self.entry_modelPath = Entry(self.master, textvariable=self.entry_modelPath_text, width=30)
        self.entry_modelPath.place(x =self.XstartPixel + 180, y =self.YstartPixel + 160)


        def folderPath():
            print("Choose folder path...")
            corpus_path = filedialog.askdirectory()
            self.entry_folderPath_text.set(corpus_path)

            print(corpus_path)

        def modelPath():
            print("Choose model path...")
            posting_path = filedialog.askopenfile()
            self.entry_modelPath_text.set(posting_path)



        self.folderPathButton = Button(self.master, text='Find', width=5, fg='black', command= folderPath)
        self.folderPathButton.place(x =self.XstartPixel + 380, y =self.YstartPixel + 125)
        self.modelPathButton = Button(self.master, text='Find', width=5, fg='black', command= modelPath)
        self.modelPathButton.place(x =self.XstartPixel + 380, y =self.YstartPixel + 155)




        #
        self.LoadModelButton = Button(self.master, text='Load Model', width=10, bg='blue', fg='white', command= self.loadModel)
        self.LoadModelButton.place(x =self.XstartPixel + 200, y =self.YstartPixel + 220)


        self.predictButton = Button(self.master, text='Predict', width=10, bg='green', fg='white', command= self.predictCommand)
        self.predictButton.place(x =self.XstartPixel + 200, y =self.YstartPixel + 250)




        self.label_results = Label(self.master, text="", width=50, font=("bold", 10))
        self.label_results.place(x =self.XstartPixel + 50, y =self.YstartPixel + 300)



        Label(self.master, text="Results:", width=10, font=("bold", 10)).place( x = self.XstartPixel + 20, y = self.YstartPixel + 300)

        from tkinter import scrolledtext
        self.results_textBox = scrolledtext.ScrolledText(width = 45, height = 15)
        self.results_textBox.place(x =self.XstartPixel + 60, y =self.YstartPixel + 330)


        # ***   Status bar    ***

        self.statusLabel = Label(self.master, text="Status: Ready", width = 40, font = ("bold", 10))
        self.statusLabel.place( x = self.XstartPixel + 60, y = self.YstartPixel + 600)





    def displayResults(self, textToDisplay):
        self.results_textBox.insert(END, textToDisplay)
        pass



    def predictCommand(self):
        self.disableButtons()
        toPredictFolderPath = self.entry_folderPath_text

        # todo - set target to loadModel method
        predictThread = Thread(target=None, args=toPredictFolderPath)
        self.listener(predictThread,self.enableButtons)
        pass


    def loadModel(self):

        self.disableButtons()
        modelPath = self.entry_modelPath_text

        # todo - set target to loadModel method
        loadModelThread = Thread(target=None, args=modelPath)
        self.listener(loadModelThread,self.enableButtons)
        pass




    @ staticmethod
    def listener(thread,action):
        thread.join()
        action()






    def enableButtons(self):
        self.predictButton.configure(state = NORMAL)
        self.LoadModelButton.configure(state = NORMAL)



    def disableButtons(self):
        self.predictButton.configure(state = DISABLED)
        self.LoadModelButton.configure(state = DISABLED)





def setWindowSizeAndPosition(root):

    w = 600  # width for the Tk root
    h = 650  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    return root

















