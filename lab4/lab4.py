import random


class Character:
    def __init__(self, name: str, health: int, level: int, armor: int = 0) -> None:
        """
        Базовый класс персонажа.

        :param name: Имя персонажа
        :param health: Очки здоровья персонажа (должно быть > 0)
        :param level: Уровень персонажа (должно быть >= 1)
        :param armor: Значение брони персонажа (по умолчанию 0, не может быть отрицательным)
        :raise ValueError: если переданы некорректные значения параметров
        """
        if health <= 0:
            raise ValueError("Здоровье должно быть положительным числом.")
        if level < 1:
            raise ValueError("Уровень должен быть не меньше 1.")
        if armor < 0:
            raise ValueError("Броня не может быть отрицательной.")

        self.name: str = name
        self.health: int = health
        self.level: int = level
        self.armor: int = armor
        self.skills: list[str] = []
        self.inventory: list[str] = []

    def level_up(self) -> None:
        """
        Повышение уровня персонажа.
        """
        self.level += 1
        print(f"{self.name} поднял уровень до {self.level}!")

    def take_damage(self, damage: int) -> None:
        """
        Получение урона с учетом брони.

        :param damage: Входящее значение урона (должно быть >= 0)
        :raise ValueError: если урон отрицательный
        """
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным.")

        reduced_damage = max(damage - self.armor, 0)
        self.health -= reduced_damage
        print(f"{self.name} получил {reduced_damage} урона. Здоровье: {self.health}")
        if self.health <= 0:
            print(f"{self.name} погиб!")

    def add_skill(self, skill: str) -> None:
        """
        Добавление нового навыка.

        :param skill: Название навыка
        :raise ValueError: если навык пуст
        """
        if not skill:
            raise ValueError("Название навыка не может быть пустым.")
        self.skills.append(skill)
        print(f"{self.name} освоил новый навык: {skill}")

    def heal(self, amount: int) -> None:
        """
        Исцеление персонажа.

        :param amount: Количество восстанавливаемого здоровья (должно быть > 0)
        :raise ValueError: если значение исцеления некорректно
        """
        if amount <= 0:
            raise ValueError("Количество исцеления должно быть положительным.")
        self.health += amount
        print(f"{self.name} исцелился на {amount}. Текущее здоровье: {self.health}")

    def add_item(self, item: str) -> None:
        """
        Добавление предмета в инвентарь.

        :param item: Название предмета
        :raise ValueError: если предмет пуст
        """
        if not item:
            raise ValueError("Название предмета не может быть пустым.")
        self.inventory.append(item)
        print(f"{self.name} получил предмет: {item}")

    def __str__(self) -> str:
        return f"{self.name} (Уровень {self.level}, Здоровье: {self.health}, Броня: {self.armor})"


class Warrior(Character):
    def __init__(self, name: str, health: int, level: int, weapon: str, armor: int = 5) -> None:
        """
        Класс Воина.
        """
        if not weapon:
            raise ValueError("Оружие не может быть пустым.")
        super().__init__(name, health, level, armor)
        self.weapon: str = weapon

    def attack(self, target: Character) -> None:
        """
        Атака врага.
        """
        base_damage = self.level * 2
        crit_bonus = base_damage * 0.5 if random.random() < 0.2 else 0
        total_damage = base_damage + crit_bonus
        print(f"{self.name} атакует {target.name} с оружием {self.weapon} и наносит {total_damage} урона!")
        target.take_damage(int(total_damage))

    def __str__(self) -> str:
        return super().__str__() + f", Оружие: {self.weapon}"


class Mage(Character):
    def __init__(self, name: str, health: int, level: int, magic_power: int, mana: int = 100) -> None:
        """
        Класс Мага.
        """
        if magic_power <= 0:
            raise ValueError("Сила магии должна быть положительной.")
        if mana < 0:
            raise ValueError("Мана не может быть отрицательной.")
        super().__init__(name, health, level)
        self.magic_power: int = magic_power
        self.mana: int = mana

    def cast_spell(self, target: Character) -> None:
        """
        Использование магического заклинания.
        """
        if self.mana < 10:
            print(f"{self.name} не хватает маны для заклинания!")
            return
        damage = self.level * 3 + self.magic_power // 2
        self.mana -= 10
        print(f"{self.name} кастует заклинание на {target.name} и наносит {damage} урона!")
        target.take_damage(damage)

    def restore_mana(self, amount: int) -> None:
        """
        Восстановление маны.
        """
        if amount <= 0:
            raise ValueError("Количество восстанавливаемой маны должно быть положительным.")
        self.mana += amount
        print(f"{self.name} восстановил {amount} маны. Текущая мана: {self.mana}")

    def __str__(self) -> str:
        return super().__str__() + f", Сила магии: {self.magic_power}, Мана: {self.mana}"


class Archer(Character):
    def __init__(self, name: str, health: int, level: int, bow_type: str) -> None:
        """
        Класс Лучника.
        """
        if not bow_type:
            raise ValueError("Тип лука не может быть пустым.")
        super().__init__(name, health, level)
        self.bow_type: str = bow_type

    def shoot_arrow(self, target: Character) -> None:
        """
        Выстрел из лука.
        """
        damage = self.level * 2
        print(f"{self.name} стреляет из {self.bow_type} по {target.name} и наносит {damage} урона!")
        target.take_damage(damage)

    def __str__(self) -> str:
        return super().__str__() + f", Тип лука: {self.bow_type}"


if __name__ == "__main__":
    warrior = Warrior("Геральт", 100, 1, "Меч")
    mage = Mage("Мерлин", 80, 1, 50)
    archer = Archer("Леголас", 90, 1, "Длинный лук")

    warrior.attack(mage)
    mage.cast_spell(archer)
    archer.shoot_arrow(warrior)

    warrior.level_up()
    mage.restore_mana(30)
    warrior.add_item("Зелье здоровья")
    warrior.heal(20)
