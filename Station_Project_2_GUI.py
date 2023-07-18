# 1.Please install and activate venv(virtual environment). Steps below (write in terminal)
#       py -m venv venv
#       .\venv\Scripts\activate         for windows
#       source ./venv/bin/activate      for Mac or Linux
# 2.Install PyQt6 library
#       pip install PyQt6


import sys
from PyQt6.QtGui import QIcon, QCursor, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout
from random import randint

# Creating window with all details--------------------------------

class Main(QWidget):
    def __init__(self) -> None:
        super(Main, self).__init__()

        self.setWindowTitle("Dice Game")
        self.setFixedWidth(1000)
        self.setStyleSheet("background: white")
        self.setWindowIcon(QIcon(".\Images\window_icon.png"))

        self.scores = [0, 0]

        self.box = QVBoxLayout()

        self.reset_btn = QPushButton(text="Reset Score")
        self.reset_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_btn.clicked.connect(self.reset)
        self.reset_btn.setStyleSheet(
            """
            *{
                margin-top: 20px;
                color: #555;
                font-family: 'Lato';
                font-size: 20px;
                text-transform: uppercase;
                font-weight: 300px;
                border: none
            }
            *:hover{
                font-size: 30px;
            }
            """
        )

        self.box.addWidget(self.reset_btn)
        self.setLayout(self.box)

        self.player = QLabel(self, text="Player")
        self.casino = QLabel(self, text="Casino")
        self.player.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.casino.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player.setStyleSheet(
            """
            *{
                color: #555;
                font-size: 40px;
                text-transform: uppercase;
                font-weight: 100px;
                margin-top: 20px;
                margin-bottom: 10px;
                letter-spacing: 2px;
            }
            """
        )
        self.casino.setStyleSheet(
            """
            *{
                color: #555;
                font-size: 40px;
                text-transform: uppercase;
                font-weight: 100px;
                margin-top: 20px;
                margin-bottom: 10px;
                letter-spacing: 2px;
            }
            """
        )

        self.score_player = QLabel(self, text=str(self.scores[0]))
        self.score_casino = QLabel(self, text=str(self.scores[1]))
        self.score_player.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_casino.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_player.setStyleSheet(
            """
            *{
                color: red;
                font-size: 80px;
                font-weight: 100px;
                margin-bottom: 130px;
            }
            """
        )
        self.score_casino.setStyleSheet(
            """
            *{
                color: red;
                font-size: 80px;
                font-weight: 100px;
                margin-bottom: 130px;
            }
            """
        )
        self.image_1 = QPixmap(".\Images\dice-6.png")
        self.image_1 = self.image_1.scaled(90, 90)
        self.image_1_label = QLabel(self)
        self.image_1_label.setPixmap(self.image_1)
        self.image_2 = QPixmap(".\Images\dice-6.png")
        self.image_2 = self.image_2.scaled(90, 90)
        self.image_2_label = QLabel(self)
        self.image_2_label.setPixmap(self.image_2)
        self.image_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_1_label.setStyleSheet("padding-top: 80px")

        self.roll_first_btn = QPushButton(self, text="Roll")
        self.roll_btn = QPushButton(self, text="Roll")
        self.new_game_btn = QPushButton(self, text="New Game")
        self.roll_first_btn.clicked.connect(self.dice_first_roll)
        self.roll_btn.clicked.connect(self.dice_roll)
        self.roll_first_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roll_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.roll_btn.hide()
        self.new_game_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.new_game_btn.clicked.connect(self.new_game)
        self.new_game_btn.setStyleSheet(
            """
            *{
                color: #555;
                margin-top: 20px;
                margin-bottom: 20px;
                font-family: 'Lato';
                font-size: 20px;
                text-transform: uppercase;
                font-weight: 300px;
                border: none
            }
            *:hover{
                font-size: 30px;
            }
            """
        )
        self.roll_first_btn.setStyleSheet(
            """
            *{
                color: #555;
                font-family: 'Lato';
                font-size: 20px;
                text-transform: uppercase;
                font-weight: 300px;
                border: none
            }
            *:hover{
                font-size: 30px;
            }
            """
        )

        self.roll_btn.setStyleSheet(
            """
            *{
                color: #555;
                font-family: 'Lato';
                font-size: 20px;
                text-transform: uppercase;
                font-weight: 300px;
                border: none
            }
            *:hover{
                font-size: 30px;
            }
            """
        )

        self.text_for_player = QLabel(self)
        self.text_for_casino = QLabel(self)
        self.dice_total = QLabel(self)
        self.text_for_player.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_for_casino.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dice_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.text_for_player.setStyleSheet(
            """
            *{
                color: red;
                font-size: 18px;
                text-transform: uppercase;
                font-weight: 80px;
                letter-spacing: 2px;
            }
            """
        )
        self.text_for_casino.setStyleSheet(
            """
            *{
                color: red;
                font-size: 18px;
                text-transform: uppercase;
                font-weight: 80px;
                letter-spacing: 2px;
            }
            """
        )
        self.dice_total.setStyleSheet(
            """
            *{
                font-size: 18px;
                text-transform: uppercase;
                font-weight: 80px;
                letter-spacing: 2px;
                margin-bottom: 20px;
            }
            """
        )


        self.grid = QGridLayout()
        self.grid.addWidget(self.player, 0, 0)
        self.grid.addWidget(self.casino, 0, 2)
        self.grid.addWidget(self.score_player, 1, 0)
        self.grid.addWidget(self.score_casino, 1, 2)
        self.grid.addWidget(self.image_1_label, 0, 1)
        self.grid.addWidget(self.image_2_label, 1, 1)
        self.grid.addWidget(self.roll_first_btn, 3, 1)
        self.grid.addWidget(self.roll_btn, 3, 1)
        self.grid.addWidget(self.new_game_btn, 4, 1)
        self.grid.addWidget(self.text_for_player, 2, 0)
        self.grid.addWidget(self.text_for_casino, 2, 2)
        self.grid.addWidget(self.dice_total, 2, 1)

        self.box.addLayout(self.grid)

# Only first roll button and funcion-----------------------------------------------------------

    def dice_first_roll(self):
        self.text_for_player.hide()
        self.text_for_casino.hide()
        self.dice_1 = randint(1,6)
        self.dice_2 = randint(1,6)
        self.total = self.dice_1 + self.dice_2
        self.image_1_label.setPixmap(QPixmap(".\Images\dice-"+str(self.dice_1)+".png").scaled(90,90))
        self.image_2_label.setPixmap(QPixmap(".\Images\dice-"+str(self.dice_2)+".png").scaled(90,90))

        if self.total == 7 or self.total == 11:
            self.text_for_player.setText("Congratulations you win")
            self.text_for_player.show()
            self.scores[0] += 1
            self.score_player.setText(str(self.scores[0]))
            self.score_casino.setText(str(self.scores[1]))
            self.dice_total.setText("Total " + str(self.total))
            self.dice_total.show()
            self.roll_first_btn.hide()
        elif self.total == 2 or self.total == 3 or self.total == 12:
            self.text_for_casino.setText("Craps! Sorry Casino Wins")
            self.text_for_casino.show()
            self.scores[1] += 1
            self.score_player.setText(str(self.scores[0]))
            self.score_casino.setText(str(self.scores[1]))
            self.dice_total.setText("Total " + str(self.total))
            self.dice_total.show()
            self.roll_first_btn.hide()
        else:
            self.goal = self.total
            self.dice_total.setText("Goal number is " + str(self.goal))
            self.dice_total.show()
            self.roll_first_btn.hide()
            self.roll_btn.show()

# All next rolls button and function-----------------------------------------------

    def dice_roll(self):
        self.text_for_player.hide()
        self.text_for_casino.hide()
        self.dice_1 = randint(1,6)
        self.dice_2 = randint(1,6)
        self.total = self.dice_1 + self.dice_2
        self.image_1_label.setPixmap(QPixmap(".\Images\dice-"+str(self.dice_1)+".png").scaled(90,90))
        self.image_2_label.setPixmap(QPixmap(".\Images\dice-"+str(self.dice_2)+".png").scaled(90,90))
        

        if self.total == 7:
            self.text_for_casino.setText("Ups! Casino Wins")
            self.text_for_casino.show()
            self.scores[1] += 1
            self.score_player.setText(str(self.scores[0]))
            self.score_casino.setText(str(self.scores[1]))
            self.dice_total.setText("Total " + str(self.total))
            self.roll_btn.hide()

        elif self.total == self.goal:
            self.text_for_player.setText("Congratulations you win")
            self.text_for_player.show()
            self.scores[0] += 1
            self.score_player.setText(str(self.scores[0]))
            self.score_casino.setText(str(self.scores[1]))
            self.dice_total.setText("GOAL " + str(self.total))
            self.roll_btn.hide()


    def new_game(self):
        self.roll_first_btn.show()
        self.text_for_player.hide()
        self.text_for_casino.hide()
        self.dice_total.hide()

    def reset(self):
        self.scores = [0, 0]
        self.roll_first_btn.show()
        self.text_for_player.hide()
        self.text_for_casino.hide()
        self.dice_total.hide()
        self.roll_btn.hide()
        self.score_player.setText(str(self.scores[0]))
        self.score_casino.setText(str(self.scores[1]))


# Run application------------------------------------------

def application():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()

