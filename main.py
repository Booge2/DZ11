class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_first(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def remove_last(self):
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def remove(self, value):
        current_node = self.head
        while current_node and current_node.value != value:
            current_node = current_node.next

        if current_node:
            if current_node == self.head:
                self.remove_first()
            elif current_node == self.tail:
                self.remove_last()
            else:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev

    def print_list(self, forward=True):
        if forward:
            current_node = self.head
            while current_node:
                print(current_node.value, end=" ")
                current_node = current_node.next
        else:
            current_node = self.tail
            while current_node:
                print(current_node.value, end=" ")
                current_node = current_node.prev
        print()

    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def replace(self, old_value, new_value, all_occurrences=False):
        current_node = self.head
        while current_node:
            if current_node.value == old_value:
                current_node.value = new_value
                if not all_occurrences:
                    return
            current_node = current_node.next


def main():
    numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]

    linked_list = DoublyLinkedList()
    for number in numbers:
        linked_list.add_last(number)

    while True:
        print("1. Додати нове число")
        print("2. Видалити всі входження числа")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("0. Вихід")

        choice = int(input("Введіть номер пункту меню: "))

        if choice == 0:
            break

        elif choice == 1:
            value = int(input("Введіть число: "))
            if linked_list.contains(value):
                print("Число", value, "вже є в списку")
            else:
                linked_list.add_last(value)
        elif choice == 2:
            value = int(input("Введіть число для видалення: "))
            while linked_list.contains(value):
                linked_list.remove(value)
            print("Всі входження числа", value, "видалені")

        elif choice == 3:
            direction = input("Введіть 'з початку' або 'з кінця': ").lower()
            if direction == "з початку":
                linked_list.print_list()
            elif direction == "з кінця":
                linked_list.print_list(forward=False)
            else:
                print("Невідомий напрямок")

        elif choice == 4:
            value = int(input("Введіть значення: "))
            if linked_list.contains(value):
                print("Значення", value, "є в списку")
            else:
                print("Значення", value, "немає в списку")

        elif choice == 5:
            old_value = int(input("Введіть старе значення: "))
            new_value = int(input("Введіть нове значення: "))
            replace_all = input("Замінити всі входження (так/ні): ").lower()
            if replace_all == "так":
                linked_list.replace(old_value, new_value, all_occurrences=True)
            else:
                linked_list.replace(old_value, new_value)

        else:
            print("Неправильний номер пункту меню")


if __name__ == "__main__":
    main()
