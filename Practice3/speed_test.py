from Practice2.Online_shop_practice import Generator
from LinkList import LinkList
from datetime import datetime

gen = Generator()

# генерация новых объектов
timer_start = datetime.utcnow()
gen_10_000 = gen.generate_10_000()
timer_stop = datetime.utcnow() - timer_start
print("Генерация 10 000 элементов:\n" + str(timer_stop))

# Таймер для добавления элементов в конец массива
timer_start = datetime.utcnow()

# slist = LinkedList()
slist = LinkList()
for shop in gen_10_000:
    slist.add(shop)

timer_stop = datetime.utcnow() - timer_start
print("Добавление 10 000 элементов в конец массива:\n" + str(timer_stop) +"\tРазмер массива: " + str(slist.size))

# Таймер для добавления элементов в начало массива
timer_start = datetime.utcnow()

slist = LinkList()
# slist = LinkedList()
for shop in gen_10_000:
    slist.add(shop,0)

timer_stop = datetime.utcnow() - timer_start
print("Добавление 10 000 новых элементов в начало:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))

# Таймер для замены элемента
timer_start = datetime.utcnow()

for shop in gen_10_000:
    slist.insert(shop, len(gen_10_000) - 1)

timer_stop = datetime.utcnow() - timer_start
print("Последовательная замена последнего элемента 10 000 значений:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))

# Таймер для поиска элемента
timer_start = datetime.utcnow()

res = slist.find(gen_10_000[0])

timer_stop = datetime.utcnow() - timer_start
print("Поиск первого элемента:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))


# Таймер для поиска элемента
timer_start = datetime.utcnow()

# res = slist.find(gen_10_000[9999])

timer_stop = datetime.utcnow() - timer_start
print("Поиск последнего элемента:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))

# Таймер для поиска элемента по индексу
timer_start = datetime.utcnow()

# res = slist.get(9999)

timer_stop = datetime.utcnow() - timer_start
print("Поиск последнего элемента из 10 000 по индексу:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))

# Таймер для удаления первых элементов
timer_start = datetime.utcnow()

for Shop in gen_10_000:
    slist.remove(Shop)

timer_stop = datetime.utcnow() - timer_start
print("Удаление 1-го элемента 10 000 раз:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))

# Таймер для удаления последних элементов
timer_start = datetime.utcnow()

for shop in reversed(gen_10_000):
    slist.remove(shop)

timer_stop = datetime.utcnow() - timer_start
print("Удаление последнего элемента 10 000 раз:\n" + str(timer_stop) + "\tРазмер массива: " + str(slist.size))