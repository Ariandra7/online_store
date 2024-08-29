from product import Product

class Order:
    """
    Класс Order

    Этот класс представляет заказ в интернет-магазине.

    Атрибут класса _total_orders:
        Счетчик всех созданных заказов. Это атрибут класса, а не экземпляра, поэтому он общий для всех объектов Order.

    Метод __init__:
        Конструктор принимает список товаров (products) и инициализирует объект Order.
        Увеличивает счетчик _total_orders на 1 каждый раз при создании нового заказа.
        Пример: order1 = Order([product1]) создаст заказ, содержащий один товар.

    Метод calculate_discounted_price:
        Статический метод, который принимает цену и скидку в процентах и возвращает цену после применения скидки.
        Пример: Order.calculate_discounted_price(1000, 10) вернет 900.0.

    Метод total_orders:
        Метод класса, который возвращает общее количество созданных заказов.
        Пример: Order.total_orders() вернет общее количество заказов.

    Метод total_price:
        Вычисляет общую стоимость всех товаров в заказе, суммируя их цены.
        Пример: order1.total_price() вернет 1000, если в заказе один товар с ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
        Пример: print(order1) выведет Order(total_price=1000).
    """
    total_orders = 0  # Статическая переменная для подсчета общего числа заказов

    def __init__(self, products):
        # Инициализация атрибута: список продуктов в заказе
        self.products = products
        Order.total_orders += 1  # Увеличиваем общее количество заказов при каждом новом заказе

    def total_price(self):
        # Подсчет общей стоимости всех продуктов в заказе
        return sum(product.price for product in self.products)

    @classmethod
    def total_orders_count(cls):
        # Метод класса для получения общего количества заказов
        return cls.total_orders

    def __str__(self):
        # Возвращает строковое представление объекта для пользователя
        products_str = ', '.join([product.name for product in self.products])
        return f"Order: [{products_str}], Total price: ${self.total_price():.2f}"

    def __repr__(self):
        # Возвращает строковое представление объекта для разработчиков
        return f"Order(products={self.products})"
