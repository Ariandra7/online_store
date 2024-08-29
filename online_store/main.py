from product import Product  # Импорт класса Product
from customer import Customer  # Импорт класса Customer
from order import Order  # Импорт класса Order
from discount import Discount  # Импорт класса Discount

# Создание нескольких продуктов
product1 = Product("Laptop", 1200)
product2 = Product("Smartphone", 800)
product3 = Product("Tablet", 400)

# Создание нескольких клиентов
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Создание заказов и добавление их клиентам
order1 = Order([product1, product2])  # Заказ из ноутбука и смартфона
order2 = Order([product2, product3])  # Заказ из смартфона и планшета
order3 = Order([product3])  # Заказ только с планшетом

# Добавление заказов клиентам
customer1.add_order(order1)
customer2.add_order(order2)
customer2.add_order(order3)

# Применение различных видов скидок
discount = Discount("Seasonal Discount", 10)  # Сезонная скидка 10%
order1_price_with_discount = Discount.seasonal_discount(order1.total_price())
order2_price_with_discount = Discount.promo_code_discount(order2.total_price())

# Вывод информации о клиентах, заказах и применении скидок
print(customer1)  # Вывод информации о клиенте 1
print(customer2)  # Вывод информации о клиенте 2
print(order1)  # Вывод информации о первом заказе
print(order2)  # Вывод информации о втором заказе
print(f"Order 1 price with discount: ${order1_price_with_discount:.2f}")  # Цена заказа 1 со скидкой
print(f"Order 2 price with discount: ${order2_price_with_discount:.2f}")  # Цена заказа 2 со скидкой
print(f"Total orders: {Order.total_orders_count()}")  # Общее количество заказов
print(f"Total amount for {customer1.name}: ${customer1.total_orders_amount():.2f}")  # Общая сумма заказов клиента 1
print(f"Total amount for {customer2.name}: ${customer2.total_orders_amount():.2f}")  # Общая сумма заказов клиента 2
