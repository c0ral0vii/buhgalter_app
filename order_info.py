from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal
from ui.order_info.order_info import Ui_CustomerWidget
from model.orders import get_order_info, change_order
from area_widget import AreaWidget

class OrderInfoWidget(QWidget):
    order_info_changed = Signal(bool)

    def __init__(self, order_id: int):
        super(OrderInfoWidget, self).__init__()

        self.ui = Ui_CustomerWidget()
        
        self.order_data = get_order_info(order_id)
        self.order_id = order_id

        self.ui.setupUi(self)
        self.counter_id = 0
        if self.order_data:
            self.create_area()
            self.create_order_labels()
            self.ui.save_pushButton.clicked.connect(self.get_changes)


    def create_order_labels(self):
        '''Лэйбел заказа'''

        if not self.order_data:
            self.ui.status.setText('Данные заказа не были подгружены, попробуйте ещё раз')
            return False

        self.ui.date_layer.setText(self.order_data.get('datetime')[:16])
        self.ui.customer_lineEdit.setText(self.order_data.get('customer_name'))
        self.ui.city_lineEdit.setText(self.order_data.get('city')[0])
        self.ui.status_label.setText(self.order_data.get('status'))
        self.ui.type_label.setText(self.order_data.get('type'))
        self.ui.status.setText('Данные заказа загружены')

    @Slot()
    def get_changes(self):
        customer_name = self.ui.customer_lineEdit.text()
        city = self.ui.city_lineEdit.text()

        all_area = {}
        print(self.ui.verticalLayout.count())
        for i in range(self.ui.verticalLayout.count()):
            widget = self.ui.verticalLayout.itemAt(i).widget()
            if isinstance(widget, AreaWidget):
                all_area.update(widget.get_text())

        data = {'customer_name': customer_name, 'city': city, 'areas': all_area}
        try:
            change_order(id=self.order_id, data=data)
            self.ui.status.setText('Заказ изменён')
            self.order_info_changed.emit(True)
        except Exception as e:
            self.ui.status.setText(f'Ошибка - {str(e)}')
    @Slot()
    def create_area(self):
        area = self.order_data.get('areas')
        for name, item in area.items():
            self.counter_id += 1
            area_widget = AreaWidget(self.counter_id, area_name=name, count=str(item[0]), limit=str(item[1]))
            self.ui.verticalLayout.addWidget(area_widget)
            area_widget.delete.connect(self.delete_area)

    @Slot(int)
    def delete_area(self, wid: int):
        widget = self.sender()
        self.ui.verticalLayout.removeWidget(widget)
        widget.deleteLater()