CONST_WINDOW = """
QMainWindow {
    background-color: #1e1e2f;
    color: #ffffff;
}

QLabel {
    font-size: 16px;
    font-weight: bold;
    color: #00d4ff;
}

QPushButton {
    background-color: #323249;
    color: #ffffff;
    border: 1px solid #00d4ff;
    border-radius: 5px;
    padding: 5px 10px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #404057;
}

QPushButton:pressed {
    background-color: #2a2a3c; 
}

QWidget {
    font-family: Arial, sans-serif;
}
"""

CONST_RESULT_WINDOW = """
QMainWindow {
    background-color: #1e1e2f;
    color: #ffffff;
}

QLabel {
    font-size: 16px;
    font-weight: bold;
    color: #00d4ff;
    padding: 40px 50px; /* Увеличиваем отступы: сверху/снизу 40px, слева/справа 50px */
    border: 2px solid #00d4ff;
    border-radius: 5px;
    background-color: #2a2a3c;
    margin: 10px; /* Добавляем немного внешних отступов для аккуратности */
}

QPushButton {
    background-color: #323249;
    color: #ffffff;
    border: 1px solid #00d4ff;
    border-radius: 5px;
    padding: 15px 20px; /* Оставляем кнопки в прежнем размере */
    font-size: 14px;
    font-weight: bold;
    min-width: 120px;
}

QPushButton:hover {
    background-color: #404057;
}

QPushButton:pressed {
    background-color: #2a2a3c;
    border-color: #008cbf;
}

QWidget {
    font-family: Arial, sans-serif;
    padding: 10px;
    border: 2px solid #00d4ff;
    border-radius: 10px;
    background-color: #1e1e2f;
}
"""