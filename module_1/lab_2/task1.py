money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0  # Месяца

while money_capital + salary >= spend:
    money_capital = money_capital + salary - spend
    months += 1
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
