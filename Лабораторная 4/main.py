class Building:
    """Базовый класс здания"""
    def __init__(self, address: str, org_list: list):
        """
        Инициализируем экземпляр класса Building

        :param address: адрес здания
        :param org_list: список организаций в здании
        """
        if not isinstance(address, str):
            raise TypeError("Адрес здания должен быть типа str")
        self._address = address
        if not isinstance(org_list, list):
            raise TypeError("Список организаций должен быть типа list")
        self.org_list = org_list

    def __str__(self) -> str:
        """
        Магический метод отвечает за читабельный вывод экземпляра класса

        :return: строка формата - Здание по адресу: адрес здания.
        """
        return f"Здание по адресу: {self.address}."

    def __repr__(self) -> str:
        """
        Магический метод отвечает за вывод экземпляра класса, по которому можно инициализировать экземпляр класса

        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(address={self.address!r}, org_list={self.org_list!r})"

    def add_org(self, org: str):
        """
        Метод позволяет добавить организацию в список

        :param org: добавляемая организация
        :return:
        """
        self.org_list.append(org)

    def remove_org(self, org: str):
        """
        Метод позволяет убрать организацию из списка

        :param org: удаляемая организация
        :return:
        """
        self.org_list.remove(org)

    @property
    def address(self) -> str:
        """
        Свойство возвращает защищенный атрибут - адрес здания
        Причина инкапсуляции - адрес здания не может меняться

        :return: значение _address
        """
        return self._address


class ResidentialBuilding(Building):
    """Дочерний от Building класс жилой дом"""
    def __init__(self, address: str, org_list: list, number_of_offices: int, number_of_app: int):
        """
        Инициализируем экземпляр класса ResidentialBuilding с конструктором родительского класса

        :param address: адрес здания
        :param org_list: список организаций в здании
        :param number_of_offices: количество офисов под коммерческие организации
        :param number_of_app: количество квартир в жилом доме
        """
        super().__init__(address, org_list)
        if not isinstance(number_of_offices, int):
            raise TypeError("Количество офисов должно быть типа int")
        if number_of_offices < len(self.org_list):
            raise ValueError("Количество офисов не может быть меньше количества организаций в списке")
        self._number_of_offices = number_of_offices
        if not isinstance(number_of_app, int):
            raise TypeError("Количество квартир должно быть типа int")
        if number_of_app <= 0:
            raise ValueError("Количество квартир должно быть больше 0")
        self._number_of_app = number_of_app

    def __repr__(self) -> str:
        """
        Магический метод отвечает за вывод экземпляра класса, по которому можно инициализировать экземпляр класса

        :return: валидный код на Python
        """
        return f"{self.__class__.__name__}(address={self.address!r}, org_list={self.org_list!r}, number_of_offices={self.number_of_offices}, number_of_app={self.number_of_app})"

    def add_org(self, org: str):
        """
        Метод позволяет добавить организацию в список
        Причина перегрузки метода - органзаций в здании не может быть больше, чем количество офисов

        :param org: добавляемая организация
        :return:
        """
        if len(self.org_list) < self.number_of_offices:
            self.org_list.append(org)

    def available_offices(self) -> int:
        """
        Метод возвращает количество свободных офисов

        :return: количество свободных офисов
        """
        return self._number_of_offices - len(self.org_list)

    @property
    def number_of_offices(self) -> int:
        """
        Свойство возвращает защищенный атрибут - количество офисов под коммерческие организации
        Причина инкапсуляции - количество офисов фиксировано

        :return: значение _number_of_offices
        """
        return self._number_of_offices

    @property
    def number_of_app(self) -> int:
        """
        Свойство возвращает защищенный атрибут - количество квартир в жилом доме
        Причина инкапсуляции - количество квартир фиксировано

        :return: значение _number_of_app
        """
        return self._number_of_app


if __name__ == "__main__":
    building_1 = Building("Политехническая ул., 29Б", ["Второй учебный корпус"])
    print(building_1)
    print(repr(building_1))
    org_1 = "Кафедра ядерной физики"
    building_1.add_org(org_1)
    print(building_1)
    print(repr(building_1))
    building_1.remove_org(org_1)

    building_2 = ResidentialBuilding("Пр-кт Луначарского, 98к1", ["Мацони"], 10, 200)
    print(building_2)
    print(repr(building_2))
    org_2 = "Нотариус Нелюбина Н. В."
    building_2.add_org(org_2)
    print(building_2)
    print(repr(building_2))
    print("Количество свободных офисов:", building_2.available_offices())
    building_2.remove_org(org_2)
