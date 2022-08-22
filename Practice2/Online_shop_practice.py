import names
import random


class Shop:
    name: str
    surname: str
    phone: str
    mail: str

    def __init__(self, name: str, surname: str, phone: str, mail: str):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail

    def get_info(self) -> str:
        return f'Person({self.name} {self.surname},' \
               f' информация о заказе отправлена на почту: {self.mail}' \
               f' код верификации отправлен в смс на номер: {self.phone} )'

    def __repr__(self):
        return Shop.get_info(self)


class Generator:
    mail = ['Google', 'Yahoo', 'Microsoft', 'Ukr.net']

    def __create_a_phone(self):
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]

        suffix = random.randint(9999999, 100000000)

        return "1{}{}{}".format(second, third, suffix)

    def generate_single(self) -> Shop:
        gen = random.randint(0, 3)
        tmp_surname = names.get_last_name()
        tmp_name = names.get_first_name()
        return Shop(tmp_name, tmp_surname, self.__create_a_phone(), self.mail[gen])

    def generate_1000(self) -> list:
        message = list()
        for i in range(1000):
            message.append(self.generate_single())
        return message

    def generate_10_000(self) -> list:
        message = list()
        [message.append(self.generate_single()) for i in range(10000)]
        return message


if __name__ == "__main__":
    person = Shop(1233, 356, 446, 838)
    print(person.get_info())

    person = Shop('John', 'Black', '+380672861619', 'danilgordiychenko@gmail.com')
    print(person.get_info())

    generator = Generator()
    person = generator.generate_single()
    print(person.get_info())

    persons1000 = generator.generate_1000()
    print(persons1000)

    persons10000 = generator.generate_10_000()
    print(persons10000)
