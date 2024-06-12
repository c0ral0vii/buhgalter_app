from ui.add_order.stop_order import Ui_Form
from PySide6.QtWidgets import QWidget
from model.orders import change_status

class StopOrderWidget(QWidget):
    def __init__(self, order_id: int):
        super(StopOrderWidget, self).__init__()


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.id = order_id

        self.ui.pushButton.clicked.connect(self.change_status)

    def change_status(self):
        self.status_checkbox = self.ui.pause_comboBox.currentText()
        self.comment = self.ui.plainTextEdit.text()

        change_status(id=self.id, status=self.status_checkbox, comment=self.comment)
