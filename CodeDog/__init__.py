from PyQt5.QtWidgets import QApplication
import sys

from .window import Window


def main():
	print("Opening window.")
	app = QApplication(sys.argv)
	app.setStyle("Fusion")

	window = Window()
	window.setWindowTitle("Window")
	window.setMinimumSize(550, 600)
	window.initUI()
	window.show()

	sys.exit(app.exec_())
