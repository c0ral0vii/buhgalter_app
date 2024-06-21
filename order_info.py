from curses.ascii import isdigit
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QTreeView
from PySide6.QtCore import Slot, Signal, QModelIndex, Qt
from ui.order_info.order_info import Ui_CustomerWidget
from model.orders import get_order_info, change_order


class OrderInfoWidget(QWidget):
    order_info_changed = Signal(bool)

    def __init__(self, order_id: int):
        super(OrderInfoWidget, self).__init__()

        self.ui = Ui_CustomerWidget()
        
        self.order_id = order_id

        self.ui.setupUi(self)

        self.ui.save_pushButton.clicked.connect(self.save)

        self.model = QStandardItemModel()

        self.get_order_data()

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
        self.ui.type_label.setText(self.order_data.get('type'))
        self.ui.status_label.setText(self.order_data.get('status'))

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

    def iterItems(self, root):
        def recurse(parent):
            for row in range(parent.rowCount()):
                for column in range(parent.columnCount()):
                    child = parent.child(row, column)
                    if child is not None:
                        yield child
                        if child.hasChildren():
                            yield from recurse(child)
        if root is not None:
            yield from recurse(root)

    def get_data(self):
        root = self.ui.cities_treeView.model().invisibleRootItem()
        data = {}
        counts = []
        current_city = None
        current_district = None

        for item in self.iterItems(root):
            parent_of_child = item.parent()

            if parent_of_child is not None:
                print(item.text())
                current_city = parent_of_child.text()
                
                if current_city not in data:
                    data[current_city] = {}
                
                if not any(i.isdigit() for i in item.text()):
                    current_district = item.text()
                    print(current_district)
                    if current_district == 'Итого':
                        continue
                    if current_district not in data[current_city]:
                        data[current_city][current_district] = []
                else:
                    counts.append(item.text())
                    if len(counts) == 3:
                        data[current_city][current_district] = counts[:]
                        print(data)
                        counts.clear()
        print(data)
        return data
    
    def clear_tree(self):
        self.model.clear()

    def save(self):
        data = self.get_data()
        customer_name = self.ui.customer_lineEdit.text()

        self.ui.status.setText('Происходит добавление')
        try:
            change_order(id=self.order_id, data=data, customer=customer_name)
            
            self.ui.status.setText('Заказ изменён')
            self.clear_tree()
            self.get_order_data()
        except Exception as e:
            self.ui.status.setText(f'Произошла ошибка {e}')
