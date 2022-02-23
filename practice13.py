price_child = 0
price_young = 990
price_old = 1390

tc = None

while True:
    try:
        tc = int(input("Введите количество билетов: "))
    except ValueError:
        print("Неверное значение")
    else:
        if tc > 0:
            break
        else:
            print("Неверное значение")

disc = 10 if tc > 3 else 0

ac = {}
for m in range(tc):
    while True:
        try:
            age = int(input(f"Введите возраст {m + 1} посетителя: "))
            if age > 0:
                if age in ac.keys():  
                    ac[age] += 1  
                else:
                    ac[age] = 1
            else:
                print("Неверное значение")
                continue
        except ValueError:
            print("Неверное значение")
        else:
            break

for k, v in ac.items():
    count_people = ac[k] 
    if k < 18:      
        ac[k] = price_child * ac[k]
    elif k >= 25:   
        ac[k] = price_old * ac[k]
    else:           
        ac[k] = price_young * ac[k]
    end = "ей" if count_people % 100 == 11 or count_people % 10 != 1 else "я"  
    print(f"Цена для {count_people} посетител{end} возрастом {k} лет - {ac.get(k)} руб.")

# Итоговая сумма с учетом или без учета скидки
print(f"Сумма заказа с учетом скидки {disc}% - " + str(sum(ac.values()) - sum(ac.values()) * disc / 100) + " руб.")
    
