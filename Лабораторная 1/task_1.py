from typing import Union
from time import sleep
import doctest


class Fridge:
    def __int__(self, temp: float, voltage: Union[int, float]):
        """
        Инициализация экземпляра класса "Холодильник"

        :param temp: температура в холодильнике в градусах Цельсия
        :param voltage: напряжение сети в вольтах

        Пример:
        >>> fridge = Fridge(0, 220)  # Создаем экземпляр класса Fridge с температурой 0 и напряжением сети 220
        """
        if not isinstance(temp, float):
            raise TypeError("Значение температуры должно быть типа int или float")
        if temp >= 5 or temp <= -10:
            raise ValueError("Температура в холодильнике должна быть от -10 до 5 градусов")
        self.temp = temp

        if not isinstance(voltage, (int, float)):
            raise TypeError("Напряжение сети должно быть типа int или float")
        if abs(voltage - 220) >= 10:
            raise ValueError("Напряжение сети не должно отличаться от 220 В более, чем на 10 В")
        self.voltage = voltage

    def set_the_recommenended_temp(self) -> None:
        """
        Функция устанавливает рекомендуемую температуру в холодильнике
        Пример:
        >>> fridge = Fridge(0, 220)  # Создаем экземпляр класса Fridge
        >>> fridge.set_the_recommenended_temp()  #Устанавливаем рекомендуемую температуру в холодильнике
        """
        ...

    def change_temp(self, value: float) -> None:
        """
        Функция меняет температуру в холодильнике на заданную величину
        :param value: величина изменения температуры

        :raise ValueError: Если при изменении температура выйдет за рабочий предел

        Пример:
        >>> fridge = Fridge(0, 220)  # Создаем экземпляр класса Fridge
        >>> fridge.change_temp(-5)  # Уменьшаем темпаратуру в холодильнике на 10 градусов
        """
        ...


class Stikers:
    def __int__(self, quantity: int, note: str):
        """
        Инициализация экземпляра класса "Стикеры"

        :param quantity: количество стикеров
        :param note: запись на стикерах

        Пример:
        >>> stiker = Stikers(1, 'Сделать лабу по прогам')  # Создаем экземпляр класса Stikers
        """
        if not isinstance(quantity, int):
            raise TypeError("Количество стикеров должно быть целым числом")
        self.quantity = quantity

        if not isinstance(note, str):
            raise TypeError("Запись на стикерах должна быть типа str")
        if (len(note) / quantity) >= 50:
            raise ValueError("На каждом стикере умещается не более 50 символов")
        self.note = note

    def check_stikers(self) -> int:
        """
        Функция проверяет количество символов в записи на стикерах

        :return: количество символов в записи на стикерах

        Пример:
        >>> stiker = Stikers(1, 'Сделать лабу по прогам')  # Создаем экземпляр класса Stikers
        >>> size_of_note = stiker.check_stikers()
        """
        ...

    def add_note(self, addition: str) -> None:
        """
        Функция добавляет запись в стикеры

        :param addition: дополнительная запись

        :raise ValueError: Если для добавления записи не хватает места на стикерах

        Пример:
        >>> stiker = Stikers(1, 'Сделать лабу по прогам')  # Создаем экземпляр класса Stikers
        >>> stiker.add_note('И сварить суп')
        """
        ...

    def add_stikers(self, value: int) -> None:
        """
        Функция добавляет заданное количество стикеров

        :param value: количество добавленных стикеров

        Пример:
        >>> stiker = Stikers(1, 'Сделать лабу по прогам')  # Создаем экземпляр класса Stikers
        >>> stiker.add_stikers(2)
        """
        ...


class Timer:
    def __int__(self, switch: bool, time: Union[int, float]):
        """
        Инициализация экземпляра класса "Таймер"

        :param switch: включатель таймера, если True, таймер включится сразу после создания, если False, будет выключен
        до момента запуска
        :param time: выставленное время таймера

        Пример:
        >>> timer = Timer(False, 5)  # Создаем таймер на 5 секунд, который не включится сразу после создания
        """
        if not isinstance(switch, bool):
            raise TypeError("Значение включателя должно быть типа bool")
        self.switch = switch

        if not isinstance(time, (int, float)):
            raise TypeError("Выставляемое время должно быть типа int или float")
        if time <= 0:
            raise ValueError("Выставляемое время должно быть больше 0")
        self.time = time

    def switch_on(self) -> None:
        """
        Функция включает таймер

        :raise ValueError: если таймер уже запущен

        Пример:
        >>> timer = Timer(False, 5)  # Создаем таймер на 5 секунд, который не включится сразу после создания
        >>> timer.switch_on()
        """
        ...

    def check_time(self) -> float:
        """
        Функция проверяет cколько прошло времени с момента запуска таймера и включен ли еще таймер

        :return: количество времени, которое прошло с момента запуска таймера, если таймер выключен возвращает 0

        Пример:
        >>> timer = Timer(True, 5)  # Создаем таймер на 5 секунд, который не включится сразу после создания
        >>> sleep(1)
        >>> timer.check_time()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
