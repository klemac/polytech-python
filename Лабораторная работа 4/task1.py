if __name__ == "__main__":
    class WristWatch:
        """
        Базовый класс наручных часов

        dial_size : float
        case_color : str
        strap_color : str
        price : float
        watch_type : str
        """

        def __init__(self, dial_size: float, case_color: str, strap_color: str, price: float, watch_type: str):
            """
            Конструктор класса WristWatch
            """
            if not isinstance(dial_size, (int, float)) or dial_size <= 0:
                raise TypeError('Размер циферблата должен быть положительным числом')
            if not isinstance(case_color, str):
                raise TypeError('Цвет корпуса должен быть строкой')
            if not isinstance(strap_color, str):
                raise TypeError('Цвет ремешка должен быть строкой')
            if not isinstance(price, (int, float)) or price <= 0:
                raise TypeError('Цена должна быть положительным числом')
            if not isinstance(watch_type, str) or watch_type not in ['электронный', 'механический']:
                raise TypeError('Тип часов должен быть строкой: "электронный" или "механический"')

            self.dial_size = dial_size
            self.case_color = case_color
            self.strap_color = strap_color
            self.price = price
            self.watch_type = watch_type

        def __str__(self) -> str:
            return (f"Наручные часы: тип={self.watch_type}, размер циферблата={self.dial_size} мм, "
                    f"цвет корпуса={self.case_color}, цвет ремешка={self.strap_color}, цена={self.price} руб.")

        def __repr__(self) -> str:
            return (f"WristWatch(dial_size={self.dial_size}, case_color='{self.case_color}', "
                    f"strap_color='{self.strap_color}', price={self.price}, watch_type='{self.watch_type}')")

        def get_description(self) -> str:
            return self.__str__()


    class Casio(WristWatch):
        """
        Дочерний класс для часов фирмы Casio

        water_resistant : bool
        backlight : bool
        """

        def __init__(self, dial_size: float, case_color: str, strap_color: str, price: float, watch_type: str,
                     water_resistant: bool, backlight: bool):
            """
            Конструктор класса Casio
            """
            super().__init__(dial_size, case_color, strap_color, price, watch_type)

            if not isinstance(water_resistant, bool):
                raise TypeError('Водонепроницаемость должна быть значением True или False')
            if not isinstance(backlight, bool):
                raise TypeError('Наличие подсветки должно быть значением True или False')

            self.water_resistant = water_resistant
            self.backlight = backlight

        def __str__(self) -> str:
            return (f"Casio: тип={self.watch_type}, размер циферблата={self.dial_size} мм, "
                    f"цвет корпуса={self.case_color}, цвет ремешка={self.strap_color}, цена={self.price} руб., "
                    f"водонепроницаемость={self.water_resistant}, подсветка={self.backlight}")

        def __repr__(self) -> str:
            return (f"Casio(dial_size={self.dial_size}, case_color='{self.case_color}', "
                    f"strap_color='{self.strap_color}', price={self.price}, watch_type='{self.watch_type}', "
                    f"water_resistant={self.water_resistant}, backlight={self.backlight})")

        def match_case_strap(self) -> bool:
            """
            Проверяет, совпадает ли цвет корпуса и ремешка
            """
            return self.case_color == self.strap_color

        def is_affordable(self, budget: float) -> bool:
            """
            Проверяет, доступны ли часы для заданного бюджета
            """
            return self.price <= budget

    class Aviator(WristWatch):
        """
        Дочерний класс для часов российской(!) фирмы Aviator

        flight_features : bool
        chronograph : bool
        """

        def __init__(self, dial_size: float, case_color: str, strap_color: str, price: float, watch_type: str,
                     flight_features: bool, chronograph: bool):
            """
            Конструктор класса Aviator
            """
            super().__init__(dial_size, case_color, strap_color, price, watch_type)

            if not isinstance(flight_features, bool):
                raise TypeError('Наличие функций для пилотов должно быть значением True или False')
            if not isinstance(chronograph, bool):
                raise TypeError('Наличие хронографа должно быть значением True или False')

            self.flight_features = flight_features
            self.chronograph = chronograph

        def __str__(self) -> str:
            return (f"Aviator: тип={self.watch_type}, размер циферблата={self.dial_size} мм, "
                    f"цвет корпуса={self.case_color}, цвет ремешка={self.strap_color}, цена={self.price} руб., "
                    f"функции для пилотов={self.flight_features}, хронограф={self.chronograph}")

        def __repr__(self) -> str:
            return (f"Aviator(dial_size={self.dial_size}, case_color='{self.case_color}', "
                    f"strap_color='{self.strap_color}', price={self.price}, watch_type='{self.watch_type}', "
                    f"flight_features={self.flight_features}, chronograph={self.chronograph})")

        def match_case_strap(self) -> bool:
            """
            Проверяет, совпадает ли цвет корпуса и ремешка
            """
            return self.case_color == self.strap_color

        def is_luxury(self) -> bool:
            """
            Проверяет, стоят ли часы больше 25000 рублей
            """
            return self.price > 25000
