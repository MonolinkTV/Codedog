from PyQt5.QtWidgets import QApplication
import sys

from .window import Window


# this function should be called by another file
# to open the window
def main():
	# much like `System.out.println()` in java
	print("Opening window.")
	# create an app (all i know is that is needed)
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	# create a window, from are custom class in window.py
	window = Window()
	# set window title
	window.setWindowTitle("Window")
	# set the smallest size the window can be realized to
	window.setMinimumSize(550, 600)
	# initialize the ui, we defined this function in window.py
	window.initUI()
	# then show the window
	window.show()

	# `sys.exit()` is same as `exit()`
	# `app.exec_()` will run the app and wait until all windows
	# are closed, and then return an error code that is
	# normally `0` for no error's
	sys.exit(app.exec_())
