from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from GUI.style import CONST_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Мониторинг сети")
        self.setFixedSize(250, 150)
        self.setStyleSheet(CONST_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.png"))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        
        analysis = QLabel(text="Получить данные скорости")
        get_data = QPushButton(text="Получить")
        
        control_UI.addWidget(analysis, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(get_data)
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
