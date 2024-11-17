#1 задание
class Car:
    def init(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = False
        self.speed = 0

        def start_engine(self):
            if not self.engine_started:
                print("Запускаю двигатель...")
                self.engine_started = True
            else:
                print("Двигатель уже запущен.")

        def stop_engine(self):
            if self.engine_started:
                print("Заглушаю двигатель...")
                self.engine_started = False
                self.speed = 0
            else:
                print("Двигатель уже остановлен.")

        def accelerate(self, speed):
            if self.engine_started:
                self.speed += speed
                print(f"Ускоряюсь до {self.speed} km/h")
            else:
                print("Двигатель не работает, я не могу разогнаться.")

        def brake(self):
            if self.speed > 0:
                print("Тормозит")
                self.speed = 0
            else:
                print("Машина уже остановилась ")

my_car = Car("Toyota", "Collora", 2016)

my_car.start_engine()
my_car.accelerate(50)
my_car.brake()
my_car.stop_engine()

#2 задание

class BankAccount:
    def init(self, owner, balance=0):
        self._balance = balance
        self.owner = owner

        @property
        def balance(self):
            return self._balance

        def deposit(self, amount):
            self._balance += amount

        def withdraw(self, amount):
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Not enough funds")

        def get_balance(self):
            return self.balance

account = BankAccount("Alice")
account.deposit(100)
account.withdraw(50)
print(account.get_balance()) # Выведет 50