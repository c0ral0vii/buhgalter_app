from PySide6.QtWidgets import QWidget
from ui.order_info.order_info import Ui_CustomerWidget
from model.orders import get_order_info

class OrderInfoWidget(QWidget):
    def __init__(self, order_id: int):
        super(OrderInfoWidget, self).__init__()

        self.ui = Ui_CustomerWidget()
        
        self.order_data = get_order_info(order_id)

        self.ui.setupUi(self)

        self.create_order_labels()

    def create_order_labels(self):
        '''Лэйбел заказа'''

        print(self.order_data)
        if not self.order_data:
            return False

        self.ui.customer_lineEdit.setText(self.order_data.get('customer_name'))
        self.ui.city_lineEdit.setText('1')
