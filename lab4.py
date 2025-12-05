class Pool:
    pool_id = 0
    type = "Загальний"  

    def __init__(self, address="Невідома", volume=0, max_visitors=0):

        self.__address = address
        self.__volume = volume
        self.__max_visitors = max_visitors
        print(f"[INFO] Створено басейн за адресою: {self.__address}")

    def get_address(self):
        return self.__address

    def get_volume(self):
        return self.__volume

    def get_max_visitors(self):
        return self.__max_visitors

    def set_address(self, address):
        self.__address = address

    def set_volume(self, volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("[ПОМИЛКА] Об’єм має бути більше 0!")

    def set_max_visitors(self, max_visitors):
        if max_visitors > 0:
            self.__max_visitors = max_visitors
        else:
            print("[ПОМИЛКА] Кількість відвідувачів має бути більше 0!")

    def __str__(self):
        return (f"Басейн за адресою: {self.__address}, "
                f"об’єм: {self.__volume} л, "
                f"макс. відвідувачів: {self.__max_visitors}")

    def __repr__(self):
        return (f"Pool(address='{self.__address}', "
                f"volume={self.__volume}, "
                f"max_visitors={self.__max_visitors})")

    def __del__(self):
        print(f"Об’єкт басейну за адресою '{self.__address}' видалено.")


    def find_max_pools(self, pools):
        max_volume_pool = max(pools, key=lambda p: p.get_volume())
        max_visitors_pool = max(pools, key=lambda p: p.get_max_visitors())

        print("=== РЕЗУЛЬТАТИ ПОШУКУ ===")
        print(f"Найбільший басейн: {max_volume_pool.get_address()} ({max_volume_pool.get_volume()} л)")
        print(f"Найбільше відвідувачів: {max_visitors_pool.get_address()} ({max_visitors_pool.get_max_visitors()} осіб)")
        if max_volume_pool == max_visitors_pool:
            print("Тут багато народу!")


# --- Основна функція ---
def main():
    print("=== ІНІЦІАЛІЗАЦІЯ ОБ’ЄКТІВ КЛАСУ POOL ===")

    pool1 = Pool("м. Київ, вул. Хрещатик, 10", 50000, 30)
    pool2 = Pool("м. Львів, вул. Зелена, 45", 40000, 25)
    pool3 = Pool("м. Одеса, вул. Морська, 7", 60000, 40)

    print("=== ІНФОРМАЦІЯ ПРО БАСЕЙНИ ===")
    print(pool1)
    print(pool2)
    print(pool3)

    print("=== ПЕРЕВІРКА МЕТОДІВ ДОСТУПУ ===")
    print("Адреса першого басейну:", pool1.get_address())
    pool1.set_volume(55000)
    print("Новий об’єм першого басейну:", pool1.get_volume())

    print("=== ПУБЛІЧНІ ПОЛЯ КЛАСУ ===")
    print(f"ID = {Pool.pool_id}")
    print(f"Тип = {Pool.type}")
    pool1.find_max_pools([pool1, pool2, pool3])


# --- Запуск ---
if __name__ == "__main__":
    main()
#додати метод в якому будем шукати макс відвідувачів і де найбльший обєм + екстра умова якшо найб обєм і макс людей один і той самий то прінт тут багато народу