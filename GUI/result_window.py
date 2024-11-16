from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from Logic.speed import get_data_internet
from GUI.style import CONST_RESULT_WINDOW


class ResultWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Скорость сети")
        self.setFixedSize(500, 500)
        self.setStyleSheet(CONST_RESULT_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.png"))

        internet = get_data_internet()
        self.start = None

        control_UI_V = QVBoxLayout()
        central_widget = QWidget()

        download_layout = QHBoxLayout()
        download_label = QLabel("Скорость загрузки из интернета: ")
        self.download_speed = QLabel(f"{internet[0]} Мбит/с")
        
        download_layout.addWidget(download_label, alignment=Qt.AlignmentFlag.AlignCenter)
        download_layout.addWidget(self.download_speed, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI_V.addLayout(download_layout)

        upload_layout = QHBoxLayout()
        upload_label = QLabel("Скорость загрузки в интернет: ")
        self.upload_speed = QLabel(f"{internet[1]} Мбит/с")
        
        upload_layout.addWidget(upload_label, alignment=Qt.AlignmentFlag.AlignCenter)
        upload_layout.addWidget(self.upload_speed, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI_V.addLayout(upload_layout)

        ping_layout = QHBoxLayout()
        ping_label = QLabel("Пинг в миллисекундах: ")
        self.ping_speed = QLabel(f"{internet[2]} мс")
        
        ping_layout.addWidget(ping_label, alignment=Qt.AlignmentFlag.AlignCenter)
        ping_layout.addWidget(self.ping_speed, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI_V.addLayout(ping_layout)

        buttons_layout = QHBoxLayout()
        to_main_menu = QPushButton("Вернуться на главное меню")
        recheck = QPushButton("Проверить снова")
        
        to_main_menu.clicked.connect(self.to_main)
        recheck.clicked.connect(self.rech)
        
        buttons_layout.addWidget(to_main_menu)
        buttons_layout.addWidget(recheck)
        control_UI_V.addLayout(buttons_layout)

        central_widget.setLayout(control_UI_V)
        self.setCentralWidget(central_widget)
        self.show()

    def to_main(self):
        from GUI.main_wondow import MainWindow
        self.hide()
        self.start = MainWindow()

    def rech(self):
        internet = get_data_internet()
        self.download_speed.setText(f"{internet[0]} Мбит/с")
        self.upload_speed.setText(f"{internet[1]} Мбит/с")
        self.ping_speed.setText(f"{internet[2]} мс")