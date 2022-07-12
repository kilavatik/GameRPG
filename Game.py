import random
import os
import time
class Monsters:
    def __init__(self, mobLvl, mobName, mobDamage, mobHP):
        self.mobLvl = mobLvl
        self.mobName = mobName
        self.mobDamage = mobDamage
        self.mobHP = mobHP
    def Getinfo(self):
        return f'{self.mobName} {self.mobLvl} {self.mobHP}, {self.mobDamage}'
class Weapon:
    def __init__(self, title, damage, price):
        self.title = title
        self.damage = damage
        self.price = price
    def GetInfo(self):
        return f"{self.title}, цена: {self.price}, урон: {self.damage}"
    def GetInfoInv(self):
        return f"{self.title}, урон: {self.damage}"
class Armor:
    def __init__(self, title, armorstats, price):
        self.title = title
        self.armorstats = armorstats
        self.price = price
    def GetInfo(self):
        return f'{self.title}, цена: {self.price}, защита: {self.armorstats}'
    def GetInfoInv(self):
        return f'{self.title}, защита: {self.armorstats}'
class Potion:
    def __init__(self, title, regen, price):
        self.title = title
        self.regen = regen
        self.price = price
    def GetInfo(self):
        return f'{self.title}, цена: {self.price}, лечение: {self.regen}'
    def GetInfoInv(self):
        return f'{self.title}, лечение: {self.regen}'
weapons = [Weapon('обычный клинок', 1, 15), Weapon('клинок Алекса', 3, 45), Weapon('клинок Гудини', 5, 75),
           Weapon("обычный лук", 2, 30), Weapon('лук Алекса', 4, 60), Weapon('лук Гудини', 6, 90)]
armors = [Armor('Обычный доспех', 1, 15), Armor('Доспех воина', 3, 45), Armor('Доспех короля', 5, 75),
          Armor('Божественный доспех', 7, 105), Armor('Доспех Алекса', 9, 135,), Armor('Доспех Гудини', 10, 150)]
potions = [Potion('маленькое лечебное зелье', 20, 10), Potion('среднее лечебное зелье', 45, 15), Potion('большое лечебное зелье', 80, 20)]
money = 1000
weaponlist = list()
armorlist = list()
potionlist = list()
lvl = 1
mobLvl = int(random.uniform(lvl-1, lvl+2))
playerWeapon = 0
damage = 5+(5/10*lvl)+playerWeapon
hp =100
exp = 0
needExp = 50
playerArmor = 0
while True:
    if mobLvl == 0:
         mobLvl = int(random.uniform(lvl - 1, lvl + 2))
    else:
         break
mobName = ["Слизь", "Зомби", "Скелет", "Паук"]
mobDamage = [int(1+(1/10*mobLvl))-playerArmor, int(8+(8/10*mobLvl))-playerArmor, int(10+(10/10*mobLvl))-playerArmor,
             int(7+(7/10*mobLvl))-playerArmor]
mobHP = [int(10+(10/10*mobLvl)), int(20+(20/10*mobLvl)), int(20+(20/10*mobLvl)),
         int(15+(15/10*mobLvl))]
clear = lambda: os.system('cls')
while True:
    print("------------------------------------------------")
    while True:
        try:
            menu = int(input("\t1.Вход\n\t2.Выход\n\tВвод: "))
            break
        except ValueError:
            print("Повторите попытку!")
    if menu == 1:
        print("------------------------------------------------")
        name = input("Введите ваше имя: ")
        print("Игра началась.")
        print("------------------------------------------------")
        while True:
            while True:
                try:
                    menu2 = int(
                        input("\t1.В бой\n\t2.В лавку\n\t3.Домой\n\t4.В таверну\n\t5.Персонаж\n\t6.Меню\n\tВвод:"))
                    break
                except ValueError:
                    print("------------------------------------------------")
                    print("Повторите попытку!")
                    print("------------------------------------------------")
            print("------------------------------------------------")
            if menu2 == 1:
                mobLvl = int(random.uniform(lvl - 1, lvl + 2))
                monsters = [Monsters(mobLvl, 'Слизь', int(1 + (1 / 10 * mobLvl) - playerArmor), int(10 + (10 / 10 * mobLvl))), Monsters(mobLvl, 'Зомби', int(8 + (8 / 10 * mobLvl)-playerArmor), int(20 + (20 / 10 * mobLvl))), Monsters(mobLvl, 'Скелет', int(10 + (10 / 10 * mobLvl)) - playerArmor,int(20 + (20 / 10 * mobLvl))), Monsters(mobLvl, 'Паук', int(10 + (10 / 10 * mobLvl)) - playerArmor, int(15 + (15 / 10 * mobLvl)))]
                mob = int(random.uniform(0, 3))
                print("на вас напал ", monsters[mob].mobName)
                print("------------------------------------------------")
                while monsters[mob].mobHP > 0:
                    if hp <= 0:
                        hp = 0
                        print("Ваша жизнь на грани")
                        break
                    while True:
                        try:
                            print(f"{monsters[mob].mobName} Ур.{monsters[mob].mobLvl} ХП: {monsters[mob].mobHP}")
                            print(f"{name} Ур.{lvl} {exp}/{needExp} ХП: {hp}")
                            print("------------------------------------------------")
                            print("\t1. Атака.\n\t2. Уклонение.\n\t3. Инвентрь\n\t4. Побег")
                            menu3 = int(input("Ваши действия: "))
                            break
                        except ValueError:
                            print("------------------------------------------------")
                            print("Повторите попытку!")
                            print("------------------------------------------------")
                    print("------------------------------------------------")
                    if menu3 == 1:
                        monsters[mob].mobHP -= damage
                        if monsters[mob].mobHP <= 0:
                            getExp = int(random.uniform(5, 15))
                            exp += getExp
                            getMoney = int(random.uniform(1+mobLvl**mobLvl, 10+mobLvl**mobLvl))
                            money = money + getMoney
                            if exp > needExp:
                                lvl=lvl+1
                                exp= exp -needExp
                                needExp=int(needExp+needExp/10)
                            print(f"Победа! \nПолучено {getExp} опыта и {getMoney} золота.")
                            print("------------------------------------------------")
                        else:
                            if monsters[mob].mobDamage > 0:
                                hp -= monsters[mob].mobDamage
                                print(f"Вы получили {monsters[mob].mobDamage} урона!")
                            else:
                                print("Вы избежали урона, ваша защита великолепна!")
                            print("------------------------------------------------")
                    elif menu3 == 2:
                        if int(random.uniform(0, 100))>50:
                            print("Вы удачно уклонились!")
                            print("------------------------------------------------")
                        else:
                            print(f"Враг оказался коварнее и предвидел ваши движения!\nВы получили"
                                  f" {monsters[mob].mobDamage - playerArmor} урона!")
                            hp -= monsters[mob].mobDamage
                            print("------------------------------------------------")
                    elif menu3 == 3:
                        while True:
                            try:
                                print(f"Имя:{name} Ур.:{lvl}Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                      f"Защита: {playerArmor} Золотые: {money}")
                                i = 1
                                for x in potionlist:
                                    print(f"{i}. {x.GetInfoInv()}")
                                    i = i + 1
                                choiseX = int(input("0. Назад.\n\t Выбор:"))
                                break
                            except ValueError:
                                print("------------------------------------------------")
                                print("Повторите попытку!")
                                print("------------------------------------------------")
                        if choiseX == 0:
                            continue
                        hp = hp + potionlist[choiseX - 1].regen
                        if hp > 100:
                            hp = 100
                    elif menu3 == 4:
                        if int(random.uniform(0, 100))>50:
                            print("Вы удачно сбежали!")
                            print("------------------------------------------------")
                            break
                        else:
                            print(f"Вам не удалось бежать!\nВы получили {mobDamage[mob]+playerArmor} урона!")
                            print("------------------------------------------------")
                    else:
                        print("???")
                        print("------------------------------------------------")
            elif menu2 == 2:
                while True:
                    print(f'ваши деньги', money)
                    while True:
                        try:
                            choice1 = int(input('1. оружие \n2. броня \n3. зелья \n4. выйти из магазина \nчто вы хотите?: '))
                            break
                        except ValueError:
                            print("------------------------------------------------")
                            print("Повторите попытку!")
                            print("------------------------------------------------")
                    if choice1 == 1:
                        while True:
                            i = 1
                            for x in weapons:
                                print(f"{i} {x.GetInfo()}")
                                i+=1
                            while True:
                                try:
                                    choice2 = int(input('7. назад\nкакое оружие пожелаете?: ')) - 1
                                    break
                                except ValueError:
                                    print("------------------------------------------------")
                                    print("Повторите попытку!")
                                    print("-------------------------------  -----------------")
                            if choice2 == 6:
                                break
                            elif choice2 < 0 or choice2 > 5:
                                print('нет у нас такого товара')
                            elif weapons[choice2].price <= money:
                                while True:
                                    try:
                                        confirm = int(input(f"вы уверенны,что хотите купить {weapons[choice2].title}"
                                                            f"\n 1. да 2. нет\n"f"Ввод: "))
                                        break
                                    except ValueError:
                                        print("------------------------------------------------")
                                        print("Повторите попытку!")
                                        print("------------------------------------------------")

                                if confirm == 2:
                                    print(f'а жаль, {weapons[choice2].title} неплохое оружие')
                                elif confirm == 1:
                                    money = money - weapons[choice2].price
                                    print(f'вы купили {weapons[choice2].title}')
                                    weaponlist.append(weapons[choice2])
                                    break
                            else:
                                print(f'подкопите ещё {weapons[choice2].price - money} монет на {weapons[choice2].title}')
                    elif choice1 == 2:
                        while True:
                            i = 1
                            for x in armors:
                                print(f"{i} {x.GetInfo()}")
                                i += 1
                            while True:
                                try:
                                    choice2 = int(input(f'\n7. назад\nкакой доспех пожелаете?: ')) - 1
                                    break
                                except ValueError:
                                    print("------------------------------------------------")
                                    print("Повторите попытку!")
                                    print("------------------------------------------------")
                            if choice2 == 6:
                                break
                            elif choice2 < 0 or choice2 > 5:
                                print('нет у нас такого товара')
                            elif armors[choice2].price <= money:
                                while True:
                                    try:
                                        confirm = int(
                                        input(f"1. да  \n2. нет\nвы уверенны, что хотите купить {armors[choice2].title}?: "))
                                        break
                                    except ValueError:
                                        print("------------------------------------------------")
                                        print("Повторите попытку!")
                                        print("------------------------------------------------")
                                if confirm == 2:
                                    print(f'а жаль, {armors[choice2].title} неплохой')
                                elif confirm == 1:
                                    money = money - armors[choice2].price
                                    print(f'вы купили {armors[choice2].title}')
                                    armorlist.append(armors[choice2])
                                    break
                            else:
                                print(
                                    f'{armors[choice2].title} не бесплатный, найди ещё {armors[choice2].price - money} монет или уходи')
                    elif choice1 == 3:
                        while True:
                            i = 1
                            for x in potions:
                                print(f"{i} {x.GetInfo()}")
                                i += 1
                            while True:
                                try:
                                    choice2 = int(input(f'4. назад \n какое зелье вы хотите купить?: ')) - 1
                                    break
                                except ValueError:
                                    print("------------------------------------------------")
                                    print("Повторите попытку!")
                                    print("------------------------------------------------")
                            if choice2 == 3:
                                break
                            elif choice2 < 0 or choice2 > 2:
                                print('нет у нас такого зелья')
                            elif potions[choice2].price <= money:
                                while True:
                                    try:
                                        confirm = int(
                                    input(f"1. да  \n2. нет\nвы уверенны, что хотите купить {potions[choice2].title}?: "))
                                        break
                                    except ValueError:
                                        print("------------------------------------------------")
                                        print("Повторите попытку!")
                                        print("------------------------------------------------")
                                if confirm == 2:
                                    print(f'а жаль, {potions[choice2].title} быстро ставит на ноги')
                                elif confirm == 1:
                                    money = money - potions[choice2].price
                                    print(f'вы купили {potions[choice2].title}')
                                    potionlist.append(potions[choice2])
                                    break
                            else:
                                print(f'вам не хватает ровно {potions[choice2].price - money} монет на {potions[choice2].title}')
                    elif choice1 == 4:
                        break
            elif menu2 == 3:
                print("Идёт востановление...")
                time.sleep(100-hp)
                print("Вы поправились!")
                print("------------------------------------------------")
            elif menu2 == 4:
                while True:
                    try:
                        menu4 = int(input("Добро пожаловать!\n Не желаете укрепить своё здоровье за счёт огненной воды?\n"
                                  "Цена: 5\n 1. Да "
                                  "2. Нет\n\tВвод: "))
                        break
                    except ValueError:
                        print("------------------------------------------------")
                        print("Повторите попытку!")
                        print("------------------------------------------------")

                print("------------------------------------------------")
                if menu4 == 1:
                    if money >= 5:
                        money = money - 5
                        hp = 100
                        print("Ваше здоровье востановленно!")
                    else:
                        print("Возвращайся, когда деньги будут!")
                    print("------------------------------------------------")
                elif menu4 == 2:
                    print("Очень жаль, прощайте")
                    print("------------------------------------------------")
                    break
            elif menu2 == 5:
                while True:
                    print(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} Защита: {playerArmor} "
                          f"Золотые: {money}")
                    while True:
                        try:
                            menu5 = int(input("\t1.Оружие.\n\t2.Броня.\n\t3.Предметы\n\t0.Назад\n\tВвод: "))
                            break
                        except ValueError:
                            print("------------------------------------------------")
                            print("Повторите попытку!")
                            print("------------------------------------------------")
                    if menu5 == 1:
                        while True:
                            try:
                                print(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                      f"Защита: {playerArmor} Золотые: {money}")
                                i = 1
                                for x in weaponlist:
                                    print(f"{i}. {x.GetInfoInv()}")
                                    i = i + 1
                                choiseX = int(input("0. Назад.\n\t Выбор:"))
                                if choiseX == 0:
                                    break
                                playerWeapon = weaponlist[choiseX - 1].damage
                                damage = 5 + (5 / 10 * lvl) + playerWeapon
                                break
                            except ValueError:
                                print("------------------------------------------------")
                                print("Повторите попытку!")
                                print("------------------------------------------------")
                    elif menu5 == 2:
                        while True:
                            try:
                                print(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                      f"Защита: {playerArmor} Золотые: {money}")
                                i = 1
                                for x in armorlist:
                                    print(f"{i}. {x.GetInfoInv()}")
                                    i = i + 1
                                choiseX = int(input("0. Назад.\n\t Выбор:"))
                                if choiseX == 0:
                                    break
                                playerArmor = armorlist[choiseX - 1].armorstats
                                break
                            except ValueError:
                                print("------------------------------------------------")
                                print("Повторите попытку!")
                                print("------------------------------------------------")
                    elif menu5 == 3:
                        while True:
                            try:
                                print(f"Имя:{name} Ур.:{lvl} Опыт:{exp}/{needExp} ХП:{hp} Урон: {damage} "
                                      f"Защита: {playerArmor} Золотые: {money}")
                                i = 1
                                for x in potionlist:
                                    print(f"{i}. {x.GetInfoInv()}")
                                    i = i + 1
                                choiseX = int(input("0. Назад.\n\t Выбор:"))
                                if choiseX == 0:
                                    break
                                hp = hp + potionlist[choiseX - 1].regen
                                if hp > 100:
                                    hp = 100
                                break
                            except ValueError:
                                print("------------------------------------------------")
                                print("Повторите попытку!")
                                print("------------------------------------------------")
                    elif menu5 == 0:
                        print("------------------------------------------------")
                        break
            elif menu2 == 6:
                break
            else:
                print("???")
                print("------------------------------------------------")
    elif menu == 2:
        break
    else:
        print("Нет такого варианта")
        print("------------------------------------------------")