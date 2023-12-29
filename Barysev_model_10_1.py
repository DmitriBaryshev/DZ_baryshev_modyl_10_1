# Задание 1
class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_volume = 0.0
        self.color = ""
        self.price = 0.0

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.manufacturer)
        print("Объем двигателя:", self.engine_volume)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price


car1 = Car()
car1.input_data()
print("\nДанные об автомобиле:")
car1.display_data()
print("\nНазвание модели:", car1.get_model())
print("Год выпуска:", car1.get_year())
print("Производитель:", car1.get_manufacturer())
print("Объем двигателя:", car1.get_engine_volume())
print("Цвет машины:", car1.get_color())
print("Цена:", car1.get_price())


# Задвние 2
class Book:
    def __init__(self):
        self.title = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0.0

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        print("Название книги:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


book1 = Book()
book1.input_data()
print("\nДанные о книге:")
book1.display_data()
print("\nНазвание книги:", book1.get_title())
print("Год выпуска:", book1.get_year())
print("Издатель:", book1.get_publisher())
print("Жанр:", book1.get_genre())
print("Автор:", book1.get_author())
print("Цена:", book1.get_price())


# Задание 3
class Stadium:
    def __init__(self):
        self.name = ""
        self.opening_date = ""
        self.country = ""
        self.city = ""
        self.capacity = 0

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def display_data(self):
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity


stadium1 = Stadium()
stadium1.input_data()
print("\nДанные о стадионе:")
stadium1.display_data()
print("\nНазвание стадиона:", stadium1.get_name())
print("Дата открытия:", stadium1.get_opening_date())
print("Страна:", stadium1.get_country())
print("Город:", stadium1.get_city())
print("Вместимость:", stadium1.get_capacity())
