import sys
import os
from PyQt5 import QtWidgets
from array import*
import matplotlib.pyplot as plt

class window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ul()

    def init_ul(self):

        #Create variables
        self.hours = 24
        self.increment = 0

        #Create a list to store description and hours
        self.activityList = [24]
        self.nameList = []
        self.hourList = []

        #Create a Label
        self.Title = QtWidgets.QLabel()
        self.Title.setText("Time Calculator")
        self.description = QtWidgets.QLabel()
        self.description.setText('Description')
        self.time = QtWidgets.QLabel()
        self.time.setText("Time Spent: ")
        self.hour = QtWidgets.QLabel()
        self.hour.setText("Hours Left:   "  + str(self.hours))
        self.end = QtWidgets.QLabel()
        self.end.setText("You are finish!!!")
        self.fileName = QtWidgets.QLabel()
        self.fileName.setText('File Name: ')

        #Create line edit
        self.description_input = QtWidgets.QLineEdit()
        self.time_input = QtWidgets.QLineEdit()
        self.fileName_input = QtWidgets.QLineEdit()

        #Create submit button
        self.submit_button = QtWidgets.QPushButton()
        self.submit_button.setText("Submit")
        self.save_button = QtWidgets.QPushButton()
        self.save_button.setText("Finish")
        self.showGraph = QtWidgets.QPushButton()
        self.showGraph.setText("Graph")

        #Create Horizontal layout
        h_box_description = QtWidgets.QHBoxLayout()
        h_box_button = QtWidgets.QHBoxLayout()
        h_box_time = QtWidgets.QHBoxLayout()
        h_box_file = QtWidgets.QHBoxLayout()

        #Add horizontal widget
        h_box_description.addWidget(self.description)
        h_box_description.addWidget(self.description_input)
        h_box_button.addWidget(self.submit_button)
        h_box_button.addWidget(self.save_button)
        h_box_button.addWidget(self.showGraph)
        h_box_time.addWidget(self.time)
        h_box_time.addWidget(self.time_input)
        h_box_file.addWidget(self.fileName)
        h_box_file.addWidget(self.fileName_input)

        #Vertical widget
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.Title)
        v_box.addWidget(self.hour)
        v_box.addLayout(h_box_description)
        v_box.addLayout(h_box_time)
        v_box.addLayout(h_box_file)
        v_box.addLayout(h_box_button)

        #Set layout
        self.setLayout(v_box)

        #Add functionality to button
        self.submit_button.clicked.connect(self.addActivity)
        self.save_button.clicked.connect(self.save)
        self.showGraph.clicked.connect(self.graph)

        #Display Window
        self.show()

    #Graph function
    def graph(self):

        fig1, ax1 = plt.subplots()
        ax1.pie(self.hourList,  labels=self.nameList, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

    #Add activities
    def addActivity(self):
        #Get name and description
        name = self.description_input.text()
        hours = self.time_input.text()

        #Computation and setting hours
        timeLeft = float(self.hours) - float(hours)

        if self.hours > 0:
            self.hours = timeLeft

            #Set the hour left on the window
            self.hour.setText("Hours Left:   "  + str(timeLeft))

            self.nameList.insert(self.increment, name)
            self.hourList.insert(self.increment, hours)

            #Save the activity in a list
            self.activityList.insert(self.increment, [name, hours])

            #print(self.hours)
            #print(self.increment)
            #print(self.activityList[self.increment])
            #print(" ")
            #print(self.activityList.__len__() - 1)
            #print(" ")
            print(self.nameList)
            print(self.hourList)
            self.increment = self.increment + 1

    #Save the activity
    def save(self):
        numbersOfActivty = self.activityList.__len__() - 1
        fileName = self.fileName_input.text()
        with open('fileName', 'w') as f:
            for x in range(numbersOfActivty):
                activity = self.activityList[x]
                f.write(str(activity) + "\n")


#Create menu bar
class menuB(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = window()
        self.setCentralWidget(self.form_widget)

        self.init_ul()

    def init_ul(self):
        #Create a bar menu
        bar = self.menuBar()

        #Add menu to bar menu
        file = bar.addMenu('File')
        backgroundcolor = bar.addMenu('Background Color')
        foregroundcolor = bar.addMenu('Foreground Color')

        #Create Subsection for file
        new_action = QtWidgets.QAction('New', self)
        save_action = QtWidgets.QAction('&Save', self)
        open_action = QtWidgets.QAction('&Open', self)
        quit_action = QtWidgets.QAction('Quit', self)

        #Create Subsection for Backgroundcolor
        bg_red_action = QtWidgets.QAction('Red', self)
        bg_blue_action = QtWidgets.QAction('Blue', self)
        bg_green_action = QtWidgets.QAction('Green', self)
        bg_yellow_action = QtWidgets.QAction('Yellow', self)
        bg_orange_action = QtWidgets.QAction('Orange', self)
        bg_gray_action = QtWidgets.QAction('Grey', self)
        bg_black_action = QtWidgets.QAction('Black', self)
        bg_white_action = QtWidgets.QAction('White', self)
        bg_purple_action = QtWidgets.QAction('Purple', self)
        bg_pink_action = QtWidgets.QAction('Pink', self)

        # Create Subsection for Backgroundcolor
        fg_red_action = QtWidgets.QAction('Red', self)
        fg_blue_action = QtWidgets.QAction('Blue', self)
        fg_green_action = QtWidgets.QAction('Green', self)
        fg_yellow_action = QtWidgets.QAction('Yellow', self)
        fg_orange_action = QtWidgets.QAction('Orange', self)
        fg_gray_action = QtWidgets.QAction('Grey', self)
        fg_black_action = QtWidgets.QAction('Black', self)
        fg_white_action = QtWidgets.QAction('White', self)
        fg_purple_action = QtWidgets.QAction('Purple', self)
        fg_pink_action = QtWidgets.QAction('Pink', self)



        #Set shorcuts
        new_action.setShortcut('Ctrl+N')
        save_action.setShortcut('Ctrl+s')
        quit_action.setShortcut('Ctrl+Q')

        #add it to the file menu
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        #Add it to color menu
        backgroundcolor.addAction(bg_red_action)
        backgroundcolor.addAction(bg_blue_action)
        backgroundcolor.addAction(bg_green_action)
        backgroundcolor.addAction(bg_yellow_action)
        backgroundcolor.addAction(bg_orange_action)
        backgroundcolor.addAction(bg_gray_action)
        backgroundcolor.addAction(bg_black_action)
        backgroundcolor.addAction(bg_white_action)
        backgroundcolor.addAction(bg_purple_action)
        backgroundcolor.addAction(bg_pink_action)
        foregroundcolor.addAction(fg_red_action)
        foregroundcolor.addAction(fg_blue_action)
        foregroundcolor.addAction(fg_green_action)
        foregroundcolor.addAction(fg_yellow_action)
        foregroundcolor.addAction(fg_orange_action)
        foregroundcolor.addAction(fg_gray_action)
        foregroundcolor.addAction(fg_black_action)
        foregroundcolor.addAction(fg_white_action)
        foregroundcolor.addAction(fg_purple_action)
        foregroundcolor.addAction(fg_pink_action)

        #Create action command
        quit_action.triggered.connect(self.quit_trigger)
        backgroundcolor.triggered.connect(self.setbgColor)
        foregroundcolor.triggered.connect(self.setfgColor)
        self.show()

    #Quit Application
    def quit_trigger(self):
        QtWidgets.qApp.quit()

    #Set background color
    def setbgColor(self, q):
        self.setAutoFillBackground(True)
        signal = q.text()
        if signal == "Red":
            self.setStyleSheet("background-color:Red")
        elif signal == "Blue":
            self.setStyleSheet("background-color:Blue")
        elif signal == "Green":
            self.setStyleSheet("background-color:Green")
        elif signal == "Yellow":
            self.setStyleSheet("background-color:Yellow")
        elif signal == "Purple":
            self.setStyleSheet("background-color:Purple")
        elif signal == "Black":
            self.setStyleSheet("background-color:Black")
        elif signal == "White":
            self.setStyleSheet("background-color:White")
        elif signal == "Pink":
            self.setStyleSheet("background-color:Pink")
        elif signal == "Orange":
            self.setStyleSheet("background-color:Orange")
        elif signal == "Grey":
            self.setStyleSheet("background-color:Grey")

    def setfgColor(self, q):
        self.setAutoFillBackground(True)
        signal = q.text()
        if signal == "Red":
            self.setStyleSheet("foreground-color:Red")
        elif signal == "Blue":
            self.setStyleSheet("foreground-color:Blue")
        elif signal == "Green":
            self.setStyleSheet("foreground-color:Green")
        elif signal == "Yellow":
            self.setStyleSheet("foreground-color:Yellow")
        elif signal == "Purple":
            self.setStyleSheet("foreground-color:Purple")
        elif signal == "Black":
            self.setStyleSheet("foreground-color:Black")
        elif signal == "White":
            self.setStyleSheet("foreground-color:White")
        elif signal == "Pink":
            self.setStyleSheet("foreground-color:Pink")
        elif signal == "Orange":
            self.setStyleSheet("foreground-color:Orange")
        elif signal == "Grey":
            self.setStyleSheet("foreground-color:Grey")


app = QtWidgets.QApplication(sys.argv)
a = menuB()
a.setWindowTitle("Energy Analysis")
sys.exit(app.exec())