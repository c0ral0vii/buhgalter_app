from ui.add_order.area import Ui_area_form
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot

class AreaWidget(QWidget):
    
    def __init__(self):
        super(AreaWidget, self).__init__()

        self.ui = Ui_area_form()

        self.ui.setupUi(self)

    def get_text(self):
        '''Получение текста из колонок'''

        area_name = self.ui.area_lineEdit.text()
        count = self.ui.count_lineEdit.text()

        return {area_name: count}


    def set_text(self, area_name: str, count: str | int):
        self.ui.area_lineEdit.setText(area_name)
        self.ui.count_lineEdit.setText(count)