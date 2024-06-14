from ui.add_order.add_order import Ui_AddForm
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from model.orders import create_order
from area_widget import AreaWidget
    

class AddOrderWidget(QWidget):
    def __init__(self):
        super(AddOrderWidget, self).__init__()

        self.ui = Ui_AddForm()
        self.ui.setupUi(self)

        self.counter_id = 0

        self.ui.add_order_pushbutton.clicked.connect(self.add_order)
        self.ui.add_area_pushButton.clicked.connect(self.add_area)

    @Slot()
    def add_area(self):
        '''Добавление региона к заказу'''

        self.counter_id += 1
        area_widget = AreaWidget(self.counter_id)
        self.ui.verticalLayout_2.addWidget(area_widget)
        area_widget.delete.connect(self.delete_area)

    @Slot(int)
    def delete_area(self, wid: int):
        widget = self.sender()
        self.ui.verticalLayout.removeWidget(widget)
        widget.deleteLater()

    def add_order(self):
        '''Добавление заказа'''

        layout = self.ui.verticalLayout_2
        self.data = {}

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, AreaWidget):
                self.data.update(widget.get_text())

        self.type = self.ui.type_comboBox.currentText()
        self.customer = self.ui.order_lineEdit.text()
        self.city = self.ui.city_lineEdit.text().strip().split(',')


        if self.type and self.customer and self.city and self.data:
            create_order(customer=self.customer, type=self.type, city=self.city, area=self.data)
        else:
            raise 'Не все обязательные поля заполнены'