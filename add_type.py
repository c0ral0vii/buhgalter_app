from ui.add_order.add_type import Ui_Form
from PySide6.QtWidgets import QWidget
from model.orders import get_types, create_type, delete_type
from PySide6.QtCore import Signal


class AddFormWidget(QWidget):
    add_form_signal = Signal(True)

    def __init__(self):
        super(AddFormWidget, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.add_type_pushButton.clicked.connect(self.add_type)
        self.ui.delete_pushButton.clicked.connect(self.delete)
        self.load()
        self.ui.status_label.setText('Здесь будет отображаться статус добавления')

    def delete(self):
        delete_type(self.ui.all_types_comboBox.currentText())
        self.ui.status_label.setText('Тип удалён')
        self.load()

    def add_type(self):
        status = self.ui.status_text_lineEdit.text()
        types = get_types()
        print(types)
        if status.lower() in types:
            self.ui.status_label.setText('Такой тип уже есть в базе')
            return

        else:
            self.ui.status_label.setText('Добавление типа')
            status = create_type(name=status)
            self.add_form_signal.emit()

            if status:
                self.ui.status_label.setText('Тип добавлен')
                self.load()
            else:
                self.ui.status_label.setText('Такой тип уже есть в базе')

    def load(self):
        self.ui.all_types_comboBox.clear()
        self.types = get_types()

        for type in self.types:
            self.ui.all_types_comboBox.addItem(type.name)