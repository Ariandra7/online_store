from order import Order  # Импорт класса Order для использования в Customer

class Customer:
    def __init__(self, name):
        # Инициализация атрибутов: имя клиента и список его заказов
        self.name = name
        self.orders = []

    def add_order(self, order):
        # Добавление заказа в список заказов клиента
        self.orders.append(order)

    def total_orders_amount(self):
        # Подсчет общей суммы всех заказов клиента
        return sum(order.total_price() for order in self.orders)

    def __str__(self):
        # Возвращает строковое представление объекта для пользователя
        return f"Customer: {self.name}, Orders: {len(self.orders)}"

    def __repr__(self):
        # Возвращает строковое представление объекта для разработчиков
        return f"Customer(name={self.name}, orders={len(self.orders)})"
