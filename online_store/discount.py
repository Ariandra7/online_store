class Discount:
    def __init__(self, description, discount_percent):
        # Инициализация атрибутов: описание скидки и процент скидки
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        # Статический метод для применения скидки к цене
        return price * (1 - discount_percent / 100)

    @classmethod
    def seasonal_discount(cls, price):
        # Метод класса для сезонной скидки (например, 10%)
        return cls.apply_discount(price, 10)

    @classmethod
    def promo_code_discount(cls, price):
        # Метод класса для скидки по промокоду (например, 15%)
        return cls.apply_discount(price, 15)

    def __str__(self):
        # Возвращает строковое представление объекта для пользователя
        return f"Discount: {self.description}, {self.discount_percent}%"

    def __repr__(self):
        # Возвращает строковое представление объекта для разработчиков
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"
