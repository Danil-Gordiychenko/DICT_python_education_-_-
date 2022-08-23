from AbstractStructure import AbstractStructure
from Practice2.Online_shop_practice import Shop
from Practice2.Online_shop_practice import Generator
from Node1 import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: Shop, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False

        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
        elif index is None:
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node

            # current = self.__head
            # while current.next:
            #     current = current.next
            # node = Node(value)
            self.size += 1

        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        self.size += 1
        return True

    def insert(self, value, index) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        return True

    def find(self, value) -> [int, None]:
        i = 0
        current = self.__head
        try:
            while current.data != value:
                current = current.next
                i += 1
            return i
        except AttributeError:
            return None

    def get(self, index) -> object:
        if self.size <= index or index < 0:
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except AttributeError:
                pass
            if current.data == value:
                self.__head = current.next
                break
            current = current.next
        self.size -= 1
        return True

    def get_all(self) -> list:
        output = []
        current = self.__head
        while current is not None:
            output.append(current.data)
            current = current.next
        return output


if __name__ == "__main__":

    s = Generator()

    p1 = s.generate_single()
    p2 = s.generate_single()
    p3 = s.generate_single()
    p4 = s.generate_single()
    p5 = s.generate_single()
    print([p1, p2, p3, p4, p5])

    s_list = LinkList()
    s_list.add(p1)
    s_list.add(p2)
    s_list.add(p3)
    s_list.add(p4)
    print(s_list.add(p5, 1))
    print("insert1: " + str(s_list.insert(p4, 1)))
    print("insert2: " + str(s_list.insert(p4, 10)))

    print(s_list.get_all())
    print(s_list.size)
    # print(len(s_list))