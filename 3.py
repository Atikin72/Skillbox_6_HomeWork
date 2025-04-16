print('Задача 3. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
# Дополнительно: сделайте так, чтобы жена не звонила Максиму, если он уже хотя бы раз ответил на звонок в течение рабочего дня.

# Пример  1
# (основная задача):
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 3-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 4-й час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 5-й час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 6-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 7-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 8-й час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин.


# Пример 2
# (с дополнительным условием)
# Начался восьмичасовой рабочий день.
# 1-й час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 0
# 2-й час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1 — да, 0 — нет): 1
# 3-й час
# Сколько задач решит Максим? 1
# 4-й час
# Сколько задач решит Максим? 2
# 5-й час
# Сколько задач решит Максим? 3
# 6-й час
# Сколько задач решит Максим? 4
# 7-й час
# Сколько задач решит Максим? 1
# 8-й час
# Сколько задач решит Максим? 1
# Рабочий день закончился. Всего выполнено задач: 15
# Нужно зайти в магазин.

time = 0
callWife = False
questWork = 0 
allWork = 0

while time < 8:
    questWork = int(input("Сколько задач решит Максим? "))
    allWork += questWork
    time += 1 
    if callWife == False:
        call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
        if call == 1:
            callWife = True
            continue
        elif call == 0:
            callWife = False
            continue
        else:
            print("Неверный вариант")
            callWife == False 

print("Рабочий день закончился. Всего выполнено задач: ", allWork )
if callWife == True:
    print("Нужно зайти в магазин." )
else:
    print("В магазин не нужно. Но дома вас будет ждать сюрприз!)" )    