import csv
import datetime

# Menu.txt dosyasını okuyarak pizza tabanı ve sosları belirleyen bir fonksiyon oluştur,
def get_pizza():
    with open('Menu.txt', 'r') as menu_file:
        menu = menu_file.read()
        print(menu)
        
        pizza_base = input("Pizza tabanı seçiniz: ")
        sos = input("Sos seçiniz: ")
        
        return pizza_base, sos


# Main fonksiyonunu,
def main():
    # Kullanıcıdan pizza ve sos seçimlerini almak için,
    pizza_base, sos = get_pizza()
    
    # Kullanıcının seçimine göre uygun pizza nesnesi oluştur,
    pizza = None
    if pizza_base == "1":
        pizza = KlasikPizza()
    elif pizza_base == "2":
        pizza = MargaritaPizza()
    elif pizza_base == "3":
        pizza = TurkPizza()
    elif pizza_base == "4":
        pizza = SadePizza()
    else:
        print("Geçersiz pizza tabanı seçimi!")
        return
    
    if sos == "11":
        pizza = ZeytinSosu(pizza)
    elif sos == "12":
        pizza = MantarSosu(pizza)
    elif sos == "13":
        pizza = KeciPeyniriSosu(pizza)
    elif sos == "14":
        pizza = EtSosu(pizza)
    elif sos == "15":
        pizza = Soğan(pizza)
    elif sos == "16":
        pizza = Mısır(pizza)
    else:
        print("Geçersiz sos seçimi!")
        return
    
    # Toplam fiyatı hesapla,
    total_cost = pizza.get_cost()

# Veriler
def save_order_to_database(user_name, user_id, credit_card_number, credit_card_password, order_description, order_time):
    with open('Orders_Database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, user_id, credit_card_number, credit_card_password, order_description, order_time])

menu = '''Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza

Lütfen bir sos seçiniz:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan

Teşekkür ederiz!'''
# Müşteriden girdileri al,
def main():
    print(menu)
    pizza_choice = input("Lütfen bir pizza seçiniz: ")
    sos_choice = input("Lütfen bir sos seçiniz: ")
    user_name = input("Lütfen isminizi giriniz: ")
    user_id = input("Lütfen TC kimlik numaranızı giriniz: ")
    credit_card_number = input("Lütfen kredi kartı numaranızı giriniz: ")
    credit_card_password = input("Lütfen kredi kartı şifrenizi giriniz: ")
    order_description = f"{pizza_choice}, {sos_choice}"
    order_time = datetime.datetime.now()
    save_order_to_database(user_name, user_id, credit_card_number, credit_card_password, order_description, order_time)
    print("Siparişiniz başarıyla alındı. Bizi tercih ettiğiniz için teşekkür ederiz. Afiyet olsun. :) ")

if __name__ == "__main__":
    main()


# Üst sınıf "Pizza"


class Pizza:
    def __init__(self):
        self._description = "Bir pizza"
        self._cost = 0.0

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost

# Alt sınıf "KlasikPizza"


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Klasik pizza"
        self._cost = 35.0

# Alt sınıf "MargaritaPizza"


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Margarita pizza"
        self._cost = 50.0

# Alt sınıf "TurkPizza"


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Türk pizza"
        self._cost = 45.0

# Alt sınıf "SadePizza"


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Sade pizza"
        self._cost = 30.0

# Üst sınıf "Decorator"


class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description() + ", " + self._description

    def get_cost(self):
        return self._pizza.get_cost() + self._cost

# Alt sınıf "ZeytinSosu"


class ZeytinSosu(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "zeytin sosu"
        self._cost = 3.0

# Alt sınıf "MantarSosu"


class MantarSosu(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "mantar sosu"
        self._cost = 7.0

# Alt sınıf "KeciPeyniriSosu"


class KeciPeyniriSosu(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "keçi peyniri sosu"
        self._cost = 12.0


# Alt sınıf "EtSosu"

class EtSosu(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "Et Sosu"
        self.cost = 15.0

# Alt sınıf "Soğan"
class Soğan(Decorator):
 def __init__(self, pizza):
     super().__init__(pizza)
     self._description = "Soğan"
     self.cost = 8.0

# Alt sınıf "Mısır"
class Soğan(Decorator):
 def __init__(self, pizza):
     super().__init__(pizza)
     self._description = "Mısır "
     self.cost = 7.50

class Pizza:
    def __init__(self):
        self.description = "Bir pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

