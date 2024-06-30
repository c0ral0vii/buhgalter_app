from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal
from order_widget import AddOrderWidget
from ui.order_info.order_info import Ui_CustomerWidget
from model.orders import get_order_info, change_order, get_types


class OrderInfoWidget(QWidget):
    order_info_changed = Signal(bool)

    def __init__(self, order_id: int):
        super(OrderInfoWidget, self).__init__()

        self.ui = Ui_CustomerWidget()

        self.order_id = order_id

        self.ui.setupUi(self)

        self.ui.save_pushButton.clicked.connect(self.save)
        self.ui.change_order_pushButton.clicked.connect(self.change_order_ui)

        self.model = QStandardItemModel()

        self.set_types()
        self.get_order_data()

    def set_types(self):
        self.ui.type_comboBox.clear()
        self.types = get_types()

        for type in self.types:
            self.ui.type_comboBox.addItem(type.name)

    def change_order_ui(self):
        self.add_order = AddOrderWidget(order_id=self.order_id)
        self.add_order.show()
        self.add_order.change_order_signal.connect(self.change_order)

    @Slot(bool)
    def change_order(self):
        try:
            self.clear_tree()
            self.get_order_data()
            self.ui.status.setText('Заказ изменён')
        except Exception as e:
            self.ui.status.setText(f'Ошибка - {e}')

    def get_order_data(self):
        try:
            self.order_data = get_order_info(self.order_id)

            self.set_laybels()
            self.set_cities_tree()
            self.ui.status.setText('Заказ загружен')
        except Exception as e:
            print(e)

    def set_laybels(self):
        self.ui.date_layer.setText(self.order_data.get('datetime')[0:16])
        self.ui.customer_lineEdit.setText(self.order_data.get('customer_name'))
        self.ui.type_comboBox.setCurrentText(self.order_data.get('type'))
        self.ui.status_comboBox.setCurrentText(self.order_data.get('status'))
        self.ui.lineEdit.setText(self.order_data.get('comment'))

    def set_cities_tree(self):
        self.model.setHorizontalHeaderLabels(["Город/Район", 'Количество', 'Лимит', 'Остатки'])
        self.ui.cities_treeView.setModel(self.model)
        self.ui.cities_treeView.setUniformRowHeights(True)
        items = [QStandardItem(f'Общее кол-во-{self.order_data.get("count")}/{self.order_data.get("limit")}')]
        for city_name, areas in self.order_data.get('cities').items():
            item = QStandardItem(city_name)

            for area_name, counts in areas.items():
                text = area_name
                item.appendRow([QStandardItem(text), QStandardItem(str(counts[0])), QStandardItem(str(counts[1])), QStandardItem(str(counts[-1]))])
            items.append(item)

        for i in items:
            self.model.appendRow(i)

        self.ui.cities_treeView.expandAll()

    def clear_tree(self):
        self.model.clear()

    def save(self):
        customer_name = self.ui.customer_lineEdit.text()
        status = self.ui.status_comboBox.currentText()
        type = self.ui.type_comboBox.currentText()
        comment = self.ui.lineEdit.text()

        self.ui.status.setText('Происходит добавление')
        try:
            change_order(id=self.order_id, customer=customer_name, status=status, type=type, comment=comment)

            self.ui.status.setText('Заказ изменён')
            self.clear_tree()
            self.get_order_data()
        except Exception as e:
            self.ui.status.setText(f'Произошла ошибка {e}')
