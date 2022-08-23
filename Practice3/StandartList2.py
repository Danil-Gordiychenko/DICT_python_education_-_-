from AbstractStructure import AbstractStructure
from Practice2.Online_shop_practice import Shop
from Practice2.Online_shop_practice import Generator


class StandartList2(AbstractStructure):
    __list: list = []
    size: int = 0

    def add(self, value: Shop, index: [int, None] = None) -> bool:
        if index is not None and self.size <= index < -self.size:
            return False

        if index is None:
            self.__list.append(value)

        else:
            self.__list.insert(index, value)
        self.size += 1
        return True

    def insert(self, value: Shop,  index: int) -> bool:
        if index is None or index < -self.size or index >= self.size:
            return False
        self.__list[index] = value
        return True

    def find(self, value: Shop) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        return None

    def get(self, index: int) -> [Shop, None]:
        if -self.size <= index < self.size:
            return self.__list[index]
        return None

    def remove(self, value: Shop) -> bool:
        try:
            self.__list.remove(value)
            self.size -= 1
            return True
        except ValueError:
            return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self):
        return self.size


if __name__ == "__main__":

    g = Generator()

    p1 = g.generate_single()
    p2 = g.generate_single()
    p3 = g.generate_single()
    p4 = g.generate_single()
    print([p1, p2, p3])

    s_list = StandartList2()
    s_list.add(p1)
    s_list.add(p2)
    s_list.add(p3, 0)
    print("insert1: " + str(s_list.insert(p4, 1)))
    print("insert2: " + str(s_list.insert(p4, 10)))

    print(s_list.get_all())
    print(len(s_list))

    print("find1: " + str(s_list.find(p1)))
    print("find2: " + str(s_list.find(p2)))
    print("get: " + str(s_list.get(1)))
    print("remove1: " + str(s_list.remove(p2)))
    print("remove2:" + str(s_list.remove(p2)))
    print(s_list.get_all())
