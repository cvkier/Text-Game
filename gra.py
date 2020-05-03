# klasa nadrzędna bohatera
class Character(object):
    def __init__(self, name, health, strength, wisdom, cash):
        self.name = name
        self.health = health
        self.strength = strength
        self.wisdom = wisdom
        self.cash = cash

    def __str__(self):
        rep = "Zdrowie: " + str(self.health) + "\n"
        rep += "Siła: " + str(self.strength) + "\n"
        rep += "Wiedza: " + str(self.wisdom) + "\n"
        rep += "Złoto: " + str(self.cash) + "\n"
        rep += "Imię: " + str(self.name)
        return rep

    def attack(self, enemy_name):
        if enemy.health > 0:
            enemy_name.health -= self.strength
            print("\nAtakujesz! Zadajesz cios za", self.strength, "!",
                  enemy_name.name, "ma już tylko", enemy_name.health, "punktów życia!")
            input("--->")


# przeciwnik i jego umiejętność atakowania
class Enemy(object):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def __str__(self):
        rep = "Zdrowie: " + str(self.health) + "\n"
        rep += "Siła: " + str(self.strength) + "\n"
        rep += "Nazwa: " + str(self.name)
        return rep

    def attack(self, player_name):
        if player_name.health > 0:
            player_name.health -= self.strength
            print("\nPrzeciwnik atakuje!", self.name, "uderza Cię z siłą", self.strength,
                  "! Zostaje Ci", player_name.health, "punkt/ów życia.")
            input("--->")


# klasa dziedziczna maga
class Mag(Character):
    def __init__(self, name="", health=5, strength=9, wisdom=9, cash=7):  # nowy konstruktor klasy Knight
        super().__init__(name, health, strength, wisdom, cash)  # super() pozwala odnieść się do metod, które są przysłonięte i coś dodać


# klasa dziedziczna rycerza
class Knight(Character):
    def __init__(self, name="", health=12, strength=5, wisdom=4, cash=9):
        super().__init__(name, health, strength, wisdom, cash)


# klasa dziedziczna, określenie parametrów klasy bezimiennego
# !! usunąć błąd przypisywania minusowych wartości !!
class Unnamed(Character):
    max = 30

    def __init__(self, name, health=0, strength=0, wisdom=0, cash=0):
        super().__init__(name, health, strength, wisdom, cash)

    def __str__(self):
        rep = "Zdrowie: " + str(self.health) + "\n"
        rep += "Siła: " + str(self.strength) + "\n"
        rep += "Wiedza: " + str(self.wisdom) + "\n"
        rep += "Złoto: " + str(self.cash) + "\n"
        rep += "Imię: " + str(self.name) + "\n"
        rep += "Max: " + str(self.max)
        return rep

    @staticmethod
    def menu():
        print("""
          0 - Zakończ
          1 - Przypisz punkty SIŁY
          2 - Przypisz punkty ZDROWIA
          3 - Przypisz punkty WIEDZY
          4 - Przypisz punkty ZŁOTA
          5 - Pokaż przypisane wartości""")

    def attribute_health(self, value):
        if self.max + self.health - value >= 0:
            self.max += self.health
            self.max -= value
            self.health = value
        else:
            open_file("przydzielanie_punktów.txt")

    def attribute_strength(self, value):
        if self.max + self.strength - value >= 0:
            self.max += self.strength
            self.max -= value
            self.strength = value
        else:
            open_file("przydzielanie_punktów.txt")

    def attribute_wisdom(self, value):
        if self.max + self.wisdom - value >= 0:
            self.max += self.wisdom
            self.max -= value
            self.wisdom = value
        else:
            open_file("przydzielanie_punktów.txt")

    def attribute_cash(self, value):
        if self.max + self.cash - value >= 0:
            self.max += self.cash
            self.max -= value
            self.cash = value
        else:
            open_file("przydzielanie_punktów.txt")

    def ascribe_unnamed(self):
        choice_number = None
        while choice_number != "0":
            print("\nPozostało punktów do wykorzystania: ", player.max)
            choice_number = input("Wybierz opcję z menu: ")
            if choice_number == "0":
                print("\nDokonałeś wyboru! Od tej pory będziesz znany jako Bezimienny!")
            elif choice_number == "1":
                attr_value = int(input("Wprowadź wartość SIŁY: "))
                player.attribute_strength(attr_value)
            elif choice_number == "2":
                attr_value = int(input("Wprowadź wartość ZDROWIA: "))
                player.attribute_health(attr_value)
            elif choice_number == "3":
                attr_value = int(input("Wprowadź wartość WIEDZY: "))
                player.attribute_wisdom(attr_value)
            elif choice_number == "4":
                attr_value = int(input("Wprowadź wartość ZŁOTA: "))
                player.attribute_cash(attr_value)
            elif choice_number == "5":
                width = 31
                print("\n\t\t", "_" * width)
                print("\t\t", "| {:26s}  |".format("BEZIMIENNY"))
                print("\t\t", "*" * width)
                print("\t\t", "| {:13s}| {:13s}|".format("SIŁA: ", str(player.strength)))
                print("\t\t", "-" * width)
                print("\t\t", "| {:13s}| {:13s}|".format("ŻYCIE: ", str(player.health)))
                print("\t\t", "-" * width)
                print("\t\t", "| {:13s}| {:13s}|".format("WIEDZA: ", str(player.wisdom)))
                print("\t\t", "-" * width)
                print("\t\t", "| {:13s}| {:13s}|".format("ZŁOTO: ", str(player.cash)))
                print("\t\t", "-" * width)
            else:
                print("Wybierz cyfrę z MENU")


# klasa nadrzędna przygody
class Adventure(object):
    def __init__(self, location1, location2):
        self.location1 = location1
        self.location2 = location2
        print("\nRzucasz kością : wynik od 1 do 3 - idziesz przez", self.location1)
        print("\t\t\t\t wynik od 4 do 6 - idziesz przez", self.location2)
        input("--->")
        self.score = roll_dice()

    def __str__(self):
        rep = "Wynik: " + str(self.score)
        return rep

    def choose_location(self):
        if self.score <= 3:
            print("\nLos zadecydował! Wyrzuciłeś", str(self.score), "! Padło na", self.location1)
            print("Zbierasz swoje rzeczy z ziemi i wyruszasz w nieznane.")
            input("--->")
        else:
            print("\nLos zadecydował! Wyrzuciłeś", str(self.score), "! Padło na", self.location2)
            print("Zbierasz swoje rzeczy z ziemi i wyruszasz w nieznane.")
            input("--->")


# klasa nadrzędna handlu
class Shop(object):
    def __init__(self, potion_1_name, potion_2_name, potion_1_cost, potion_1_effect, potion_2_cost, potion_2_effect):
        self.potion_1_name = potion_1_name
        self.potion_2_name = potion_2_name
        self.potion_1_cost = potion_1_cost
        self.potion_1_effect = potion_1_effect
        self.potion_2_cost = potion_2_cost
        self.potion_2_effect = potion_2_effect
        self.print_menu()
        self.menu()
        self.buying()

    def print_menu(self):
        width = 29
        print("\n\t\t", "_" * width)
        print("\t\t", "| {:26s}|".format("OFERTA SPRZEDAWCY"))
        print("\t\t", "*" * width)
        print("\t\t", "| {:15s} {:1s} {:1s} {:5s} |".format(self.potion_1_name, "-", str(self.potion_1_cost), "złota"))
        print("\t\t", "-" * width)
        print("\t\t", "| {:15s} {:1s} {:1s} {:5s} |".format(self.potion_2_name, "-", str(self.potion_2_cost), "złota"))
        print("\t\t", "-" * width)

    def menu(self):
        print("""
            0 - Idziesz dalej
            1 - Kupujesz""", self.potion_1_name,
              """\n\t\t\t2 - Kupujesz""", self.potion_2_name,
              """\n\t\t\t3 - Sprawdź stan złota""")

    def buying(self):
        buy = None
        while buy != "0":
            buy = input("\nCo chcesz zrobić?: ")
            print()
            if buy == "1":
                if player.cash <= 1:
                    open_file("brak_złota.txt")
                else:
                    player.health += self.potion_1_effect
                    player.cash -= self.potion_1_cost
                    print(self.potion_1_name, "zwiększył Twój atrybut o", self.potion_1_effect, "punkt. Wynosi on ", player.health, end="")
                    print(".", "\nTwój stan złota zmniejszył się o", end=" ")
                    print(self.potion_1_cost, end="")
                    print(". W sakiewce zostało Ci", player.cash, "złota.")
            elif buy == "2":
                if player.cash <= 1:
                    open_file("brak_złota.txt")
                else:
                    player.strength += self.potion_2_effect
                    player.cash -= self.potion_2_cost
                    print(self.potion_2_name, "zwiększył Twój atrybut o", self.potion_2_effect, "punkt. Wynosi on ", player.strength, end="")
                    print(".", "\nTwój stan złota zmniejszył się o", end=" ")
                    print(self.potion_2_cost, end="")
                    print(". W sakiewce zostało Ci", player.cash, "złota.")
            elif buy == "3":
                print("Masz", player.cash, "złota.")
            elif buy == "0":
                open_file("dalsza_podróż_wieża.txt")
            else:
                print("\nKupiec czeka na Twoją odpowiedź!")


# wstęp i wybór imienia
class Name(object):
    def __init__(self, name=None):
        print("""INSTRUKCJA GRY:
Kiedy pojawi się taki symbol '--->' musisz nacisnąć Enter, aby przejść dalej.""")
        self.name = name

    def choose(self):
        while not self.name:
            self.name = input("\nWitaj! Jak mam się do Ciebie zwracać graczu?: ")
        print(self.name, "zatem...")


# funkcja pokazująca statystyki dla maga i rycerza
def show_stat():
    width_line = 31
    print("\n\t\t", "_" * width_line)
    print("\t\t", "| {:13s}| {:13s}|".format("MAG", "RYCERZ"))
    print("\t\t", "*" * width_line)
    print("\t\t", "| {:13s}| {:13s}|".format("SIŁA: 7", "SIŁA: 5"))
    print("\t\t", "-" * width_line)
    print("\t\t", "| {:13s}| {:13s}|".format("ŻYCIE: 7", "ŻYCIE: 12"))
    print("\t\t", "-" * width_line)
    print("\t\t", "| {:13s}| {:13s}|".format("WIEDZA: 8", "WIEDZA: 4"))
    print("\t\t", "-" * width_line)
    print("\t\t", "| {:13s}| {:13s}|".format("ZŁOTO: 8", "ZŁOTO: 9"))
    print("\t\t", "-" * width_line)


# funkcja otwierania plików tekstowych
def open_file(file_name):
    text_file = open(file_name, "r", encoding="utf-8")
    print()
    print(text_file.read())
    text_file.close()


# otrzymuje parametr question np. yes_no("Tak czy nie?")
def yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()  # zamienia na małe litery
    return response  # zwraca odpowiedź t lub n


# symuluje rzut kostką
def roll_dice():
    import random
    score_adventure = random.randint(1, 6)
    return score_adventure


# przedstawienie aktualnych statystyk bohatera
def show_skill():
    print("""\nW międzyczasie masz możliwość sprawdzenia swoich atrybutów!

        Sprawdź swoje atrybuty:
        0 - Zamknij i podróżój dalej
        1 - Sprawdź swoje Atrybuty""")
    check_1 = ""
    while check_1 != "0":
        check_1 = input("\nTwój wybór to: ")
        if check_1 == "1":
            width = 16
            print("\n\t\t", "_" * width)
            print("\t\t", "| {:8s}| {:3s}|" .format("SIŁA: ", str(player.strength)))
            print("\t\t", "-" * width)
            print("\t\t", "| {:8s}| {:3s}|" .format("ŻYCIE: ", str(player.health)))
            print("\t\t", "-" * width)
            print("\t\t", "| {:8s}| {:3s}|" .format("WIEDZA: ", str(player.wisdom)))
            print("\t\t", "-" * width)
            print("\t\t", "| {:8s}| {:3s}|" .format("ZŁOTO: ", str(player.cash)))
            print("\t\t", "-" * width)
            print()
        elif check_1 not in ("0", "1"):
            print("\nMusisz dokonać wyboru!")


# funkcja walki bohatera z przeciwnikiem
def fight(player_name, enemy_name, next_way):
    while enemy_name.health > 0 and player_name.health > 0:
        player_name.attack(enemy_name)
        if enemy_name.health > 0:
            enemy_name.attack(player_name)
    if player_name.health >= 1 and enemy_name.health <= 0:
        player_name.cash += 2
        open_file("normalna_walka_zwycięstwo.txt")
        open_file(next_way)
        input("--->")
    else:
        open_file("przegrana.txt")


# konkretyzacja klasy Name i wywołanie instrukcji przez __init__
start = Name()

# wywołanie metody wyboru imienia
start.choose()

# prezentacja statystyk maga i rycerza
show_stat()

# wybór postaci
choice = None
while choice not in ("1", "2", "3"):
    choice = input("""\n... jaką postacią chcesz grać? Magiem, Rycerzem czy Bezimiennym? Sam wybierz!
Mag - 1 Rycerz - 2 Bezimienny - 3: """)
    if choice == "1":
        player = Mag()  # konkretyzacja klasy Mag
        print("\nDokonałeś wyboru! Od tej pory będziesz znany jako Mag", start.name.capitalize(), "!")
    elif choice == "2":
        player = Knight(start.name)  # konkretyzacja klasy Knight
        print("\nDokonałeś wyboru! Od tej pory będziesz znany jako Rycerz", start.name.capitalize(), "!")
    elif choice == "3":
        open_file("bezimienny_wstęp.txt")
        player = Unnamed("Bezimienny")  # konkretyzacja klasy Unnamed
        player.menu()  # wywołanie metody menu
        player.ascribe_unnamed()  # wywołanie metody przypisania wartości atrybutów
    else:
        print("\nNie możesz się zdecydować? Zastanów się dobrze!")

# użycie funkcji do otwarcia napisów wstępnych gry
open_file("intro_gra.txt")

# konkretyzacja klasy Adventure i losowanie lokalizacji
first_adventure = Adventure("Zakazany las", "Trakt kupców")
first_adventure.choose_location()

# pierwsza przygoda - walka lub trakt
if first_adventure.score <= 3:
    open_file("przygoda_1.txt")
    answer = yes_no("Czy chcesz go zaatakować? <t/n>: ")
    if answer == "t":
        print("\nZatem przygotuj się ... ZACZYNAMY!!")
        input("--->")
        enemy = Enemy("Jaskiniowy Trol", 7, 2)  # konkretyzacja klasy Enemy - stworzenie 1 przeciwnika
        fight(player, enemy, "trakt_1.txt")  # wywołanie funkcji walki - fight()
    else:
        print("\nStchórzyłeś? Strach Cię obleciał? Uciekaj z podkulonym ogonem!")
        input("--->")
        open_file("trakt_1.txt")
else:
    open_file("trakt_1.txt")
    input("--->")

choice_buy = yes_no("\nChcesz sprawdzić co sprzedawca ma w ofercie? <t/n>: ")
if choice_buy == "t":
    shop1 = Shop("Eliksir życia", "Eliksir Zdrowia", 2, 1, 2, 1)
else:
    print("\nIdziesz dalej, ale póki co to koniec gry!")

