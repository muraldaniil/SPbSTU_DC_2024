import doctest
class Donor:
    def __init__(self, name: str, blood_type: str, age: int):
        """
        Инициализация объекта "Донор".

        :param name: Имя донора
        :param blood_type: Группа крови донора
        :param age: Возраст донора

        :raise ValueError: Если возраст донора не в пределах 18-65 лет
        Примеры:
        >>> donor = Donor("Иван Иванов", "O+", 30)
        """
        if not 18 <= age <= 65:
            raise ValueError("Возраст донора должен быть от 18 до 65 лет.")
        self.name = name
        self.blood_type = blood_type
        self.age = age

    def donate_blood(self) -> str:
        """
        Метод для сдачи крови.

        Возвращает:
            str: Подтверждение сдачи крови.
        """
        ...

    def check_eligibility(self) -> bool:
        """
        Метод для проверки, может ли донор сдать кровь.

        Возвращает:
            bool: True, если донор может сдать кровь, иначе False.
        """
        ...


class Donation:
    def __init__(self, donor_id: int, donation_date: str, volume_ml: int):
        """
        Инициализация объекта "Донация".

        :param donor_id: ID донора
        :param donation_date: Дата сдачи крови
        :param volume_ml: Объем сданной крови в миллилитрах

        :raise ValueError: Если объем сдачи крови не в пределах 1-500 мл
        Примеры:
        >>> donation = Donation(1, "2024-12-01", 450)  # Создание объекта
        """
        if volume_ml <= 0 or volume_ml > 500:
            raise ValueError("Объем сдачи крови должен быть от 1 до 500 мл.")
        self.donor_id = donor_id
        self.donation_date = donation_date
        self.volume_ml = volume_ml

    def record_donation(self) -> None:
        """
        Метод для записи события сдачи крови.

        Возвращает:
            None
        """
        ...

    def generate_receipt(self) -> str:
        """
        Метод для создания квитанции о сдаче крови.

        Возвращает:
            str: Информация о квитанции.
        """
        ...


class BloodCenter:
    def __init__(self, name: str, location: str):
        """
        Инициализация объекта "Центр крови".

        :param name: Название центра
        :param location: Местоположение центра
        >>> center = BloodCenter("Центр крови", "г. Москва")  
        """
        self.name = name
        self.location = location

    def schedule_donation(self, donor_id: int, date: str) -> bool:
        """
        Метод для записи донора на сдачу крови.

        Аргументы:
            donor_id (int): ID донора.
            date (str): Запланированная дата сдачи крови.

        Возвращает:
            bool: True, если запись прошла успешно, иначе False.
        """
        ...

    def list_available_dates(self) -> list[str]:
        """
        Метод для получения списка доступных дат для сдачи крови.

        Возвращает:
            list[str]: Список доступных дат.
        """
        ...

if __name__ == "__main__":
    doctest.testmod()