from ui.add_order.area import Ui_area_form
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot


class AreaWidget(QWidget):
    delete = Signal(int)

    def __init__(self, id: int, area_name: str = None, count: str = None, limit: str = None, city_name: str = None):
        super(AreaWidget, self).__init__()

        self.ui = Ui_area_form()
        self.ui.setupUi(self)
        self.id_widget = id
        self.ui.delete_area_pushButton.clicked.connect(self.press_del)
        self.area_name = area_name
        self.limit = limit
        self.count = count

        if self.area_name is not None:
            self.set_text()

    def get_text(self):
        '''Получение текста из колонок'''

        area_name = self.ui.area_lineEdit.text()
        limit = self.ui.limit_lineEdit.text()
        count = self.ui.count_lineEdit.text()

        return {area_name: [count, limit]}

    def set_text(self):
        self.ui.area_lineEdit.setText(self.area_name)
        self.ui.count_lineEdit.setText(self.count)
        self.ui.limit_lineEdit.setText(self.limit)

    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)