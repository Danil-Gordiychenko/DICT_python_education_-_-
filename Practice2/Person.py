class Person:

    def __init__(self, name: str, surname: str, birhtdate: str, phone: str, mail: str, address: str):
        self.name = name
        self.surname = surname
        self.birhtdate = birhtdate
        self.phone = phone
        self.mail = mail
        self.address = address

    def info(self):
        self.name = input('Name: ')
        self.surname = input('Surname: ')
        self.birhtdate = input('Birhtdate: ')
        self.phone = input('Phone: ')
        self.mail = input('Mail: ')
        self.address = input('Adress: ')
        print(self.mail)

    def domain(self):
        global mail
        list_gmail = ['@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']
        list_yahoo = ['@', 'y', 'a', 'h', 'o', 'o', '.', 'c', 'o', 'm']
        list_mail = list(self.mail[3:])
        in_gmail = set(list_mail).issubset(list_gmail)
        in_yahoo = set(list_mail).issubset(list_yahoo)
        if in_gmail == True:
            mail = 'Gmail'
        elif in_yahoo == True:
            mail = 'Yahoo'
        else:
            index = list(self.mail).index('@')
            mail = self.mail[0:2] + "***" + self.mail[index:]

    def phone_number(self):
        global phone
        phone = self.phone[0:6] + "***" + self.phone[-4:]

    def program(self):
        print(f" {self.name} {self.surname}, информация о\n заказе отправлена на почту ", mail, "\n код верефикации отпрален в смс на\n номер", phone)


a = Person(name='', surname='', birhtdate='', phone='', mail='', address='')
a.info()
a.domain()
a.phone_number()
a.program()

