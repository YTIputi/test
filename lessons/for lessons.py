import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QLabel, QDialog, QDialogButtonBox
from PyQt6.QtCore import Qt, QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример создания кнопки")
        self.line = QLineEdit(self)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Левая кнопка мыши
            dlg = CustomDialog(self)

            if dlg.exec():
                new_button = DraggableButton('erferfre', self)
                position = event.pos()
                new_button.move(position)
                new_button.show()


class DraggableButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setMouseTracking(True)
        self.dragging = False
        self.offset = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Левая кнопка мыши
            self.dragging = True
            self.offset = event.pos()


    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToParent(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Левая кнопка мыши
            self.dragging = False


class CustomDialog(QDialog):
    def __init__(self, parents):
        super().__init__(parents)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())