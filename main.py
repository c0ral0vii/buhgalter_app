import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem

from ui.main_page.main_page import Ui_MainWindow
from order_widget import AddOrderWidget
from stop_order import StopOrderWidget
from order_info import OrderInfoWidget
from add_type import AddFormWidget

from model.orders import get_all_orders, get_orders, delete_order, get_archive, archivate, get_order_info, create_city, \
    create_order
from model.model import Orders, create_db



class Application(QMainWindow):
    def __init__(self, data: Orders):
        super(Application, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_order_button.clicked.connect(self.add_order)
        self.ui.reload_button.clicked.connect(self.reload)
        self.ui.all_orders_pushButton.clicked.connect(self.all_orders)
        self.ui.delete_order_button.clicked.connect(self.delete_order)
        self.ui.archive_button.clicked.connect(self.archive)
        self.ui.stop_pushButton.clicked.connect(self.change_status_order)
        self.ui.add_types_pushButton.clicked.connect(self.add_type)
        self.ui.order_limit_pushButton.clicked.connect(self.reload)
        self.ui.tableView.doubleClicked.connect(self.open_order_info)
        self.ui.unload_order_pushButton.clicked.connect(self.unload_order)
        self.model = QStandardItemModel()
        
        self.data = data
        self.reload()

    def create_file(self, data: dict):
        print(data)
        filename = f'ВЫГРУЖЕНЫЙ ЗАКАЗ.txt'

        with open(filename, 'w') as f:
            f.write(data.get('datetime')[:16])
            f.write(f'\nСпрут {data.get('type')} - {data.get('customer_name')}\n')

            for city, areas in data.get('cities').items():
                city_count = areas.get('Итого')
                f.write(f'\n⭐️{city}:')

                for area, count in areas.items():
                    if area == 'Итого':
                        continue
                    f.write(f'\n•{area} - {count[0]}/{count[1]}')
                f.write(f'\nИтого: {city_count[0]}/{city_count[1]}')
                f.write(f'\nОстаток - {city_count[2]}\n')

            f.write(f'\nИтого: {data.get('count')}/{data.get('limit')}')
            f.write(f'\nОстаток - {data.get('remainder')}')
        return filename

    def unload_order(self):
        current_index = self.ui.tableView.currentIndex()
        if current_index.isValid():
            row_data = [self.model.data(self.model.index(current_index.row(), column)) for column in
                        range(self.model.columnCount())]
            self.ui.status.setText('Создаём файл с заказом...')
            self.create_file(data=get_order_info(id=row_data[0]))


    def add_type(self):
        self.add_order_ui = AddFormWidget()
        self.add_order_ui.show()

    def open_order_info(self, index):
        if index.isValid():
            row_data = [self.model.item(index.row(), column).text() for column in range(self.model.columnCount())]
            self.order_info = OrderInfoWidget(order_id=row_data[0])
            self.order_info.show()
            self.order_info.order_info_changed.connect(self.reload)

    def change_status_order(self):
        current_index = self.ui.tableView.currentIndex()
        self.ui.status.setText('Изменение статуса заказа')

        if current_index.isValid():
            row_data = [self.model.data(self.model.index(current_index.row(), column)) for column in range(self.model.columnCount())]

            self.stop_order = StopOrderWidget(order_id=row_data[0])
            self.stop_order.show()
            self.stop_order.change_status_order.connect(self.reload)

    def add_header_tableView(self):
        self.model.setHorizontalHeaderLabels(['Номер заказа', 'Заказчик', 'Статус', 'Количество', 'Лимит', 'Комментарий', 'Тип', 'Город', 'Район'])
        self.ui.tableView.setShowGrid(True)

    def add_order(self):
        '''Добавление заказа'''

        self.add_order_widget = AddOrderWidget()
        self.add_order_widget.show()
        self.add_order_widget.add_order_signal.connect(self.reload)

    def all_orders(self):
        '''Отображение всех заказов'''
        
        orders = get_all_orders()
        self.model.clear()
        self.add_header_tableView()

        for row_data in orders:
            print(row_data)
            self.row_items = [QStandardItem(item) for item in row_data]
            self.model.appendRow(self.row_items)
        
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.status.setText('Отображаются все заказы')

    def archive(self):
        '''Отображение всех заказов'''
        
        orders = get_archive()
        self.model.clear()
        self.add_header_tableView()

        for row_data in orders:
            print(row_data)
            self.row_items = [QStandardItem(item) for item in row_data]
            self.model.appendRow(self.row_items)
        
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.status.setText('Отображается архив заказов')

    @Slot(bool)
    def reload(self):
        '''Перезагрузка заказов'''

        orders = get_orders()

        self.model.clear()
        self.add_header_tableView()

        for row_data in orders:
            print(row_data)
            self.row_items = [QStandardItem(item) for item in row_data]
            self.model.appendRow(self.row_items)
        
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.status.setText('Произошла перезагрузка')


    def delete_order(self):
        '''Удаление заказ'''

        current_index = self.ui.tableView.currentIndex()
        try:
            if current_index.isValid():
                    row_data = [self.model.data(self.model.index(current_index.row(), column)) for column in range(self.model.columnCount())]

                    delete_order(id=row_data[0])
                    self.reload()
                    self.ui.status.setText('Заказ удалён')
        except Exception as e:
            self.ui.status.setText('Произошла ошибка при удалении, возможно вы не выбрали заказ')


if __name__ == '__main__':
    create_db()

    app = QApplication(sys.argv)

    window = Application(data=Orders)
    window.show()

    sys.exit(app.exec())

