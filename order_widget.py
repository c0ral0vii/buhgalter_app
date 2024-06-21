from cache_func import RedisCache
from ui.add_order.add_order import Ui_AddForm
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from model.orders import create_order
from area_widget import AreaWidget

class AddOrderWidget(QWidget):
    add_order_signal = Signal(bool)

    def __init__(self):
        super(AddOrderWidget, self).__init__()

        self.ui = Ui_AddForm()
        self.ui.setupUi(self)

        self.counter_id = 0
        self.cache = RedisCache()

        self.ui.add_order_pushbutton.clicked.connect(self.add_order)
        self.ui.add_area_pushButton.clicked.connect(self.add_area)
        self.ui.add_city_pushButton.clicked.connect(self.add_city)
        self.ui.city.currentTextChanged.connect(self.save_to_cache)

        self.current_city = self.ui.city.currentText()

    @Slot()
    def add_area(self):
        '''Добавление региона к заказу'''

        if self.ui.city.currentText():
            self.counter_id += 1
            self.city = self.ui.city.currentText()

            self.area_widget = AreaWidget(id=self.counter_id, city_name=self.city)
            self.ui.verticalLayout_2.addWidget(self.area_widget)
            self.area_widget.delete.connect(self.delete_area)
        else:
            self.ui.status.setText('Добавьте город для работы')

    @Slot()
    def add_city(self):
        self.city_name = self.ui.city_lineEdit.text()
        if len(self.city_name) >= 2:
            self.ui.city.addItem(self.city_name)
            self.current_city = self.ui.city.currentText()

            self.cache.add(self.city_name, {})
            self.ui.status.setText('Город добавлен')

            if not self.ui.city.currentText():
                self.ui.city.setCurrentText(self.city_name)

            self.ui.city_lineEdit.clear()
            return True

        self.ui.status.setText('У города должно быть больше 2 букв в названии')

    @Slot()
    def save_to_cache(self):
        layout = self.ui.verticalLayout_2
        self.areas = {}

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, AreaWidget):
                self.areas.update(widget.get_text())

        self.cache.add(key=self.current_city, value=self.areas)
        self.current_city = self.ui.city.currentText()

        self.refresh_areas()


    @Slot()
    def refresh_areas(self):
        layout = self.ui.verticalLayout_2
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()

        areas = self.cache.get(key=self.ui.city.currentText())
        print(areas)
        for name, item in areas.items():
            self.counter_id += 1
            area_widget = AreaWidget(self.counter_id, area_name=name, count=str(item[0]), limit=str(item[1]))
            self.ui.verticalLayout_2.addWidget(area_widget)
            area_widget.delete.connect(self.delete_area)

    @Slot(int)
    def delete_area(self, wid: int):
        widget = self.sender()
        self.ui.verticalLayout.removeWidget(widget)
        widget.deleteLater()

    @Slot()
    def add_order(self):
        '''Добавление заказа'''

        layout = self.ui.verticalLayout_2
        self.areas = {}

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, AreaWidget):
                self.areas.update(widget.get_text())

        self.cache.add(key=self.current_city, value=self.areas)

        self.type = self.ui.type_comboBox.currentText()
        self.customer = self.ui.order_lineEdit.text()
        self.city = self.ui.city_lineEdit.text().strip().split(',')
        self.data = self.cache.get_all()
        print(self.data)

        if self.type and self.customer and self.data:
            self.ui.status.setText('Просходит добавление...')
            create_order(customer=self.customer, type=self.type, data=self.data)
            self.ui.status.setText('Добавлен')
            self.add_order_signal.emit(True)
        else:
            self.ui.status.setText('Не все обязательные поля заполнены')