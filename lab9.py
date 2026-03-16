# Задача 1
# Создаем класс Node

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
# Задача 2
# Создаем класс LinkedList

class LinkedList:
    def _init_(self):
        self.head = None
# Задача 3: Добавление в начало (prepend)
def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
# Задача 4. Добавление элемента в конец списка
def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
# Задача 5: Вывод всех элементов списка
def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
# Задача 6: Поиск элемента
def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False
# Задача 7: Удаление первого элемента
def delete_first(self):
        if self.head is not None:
            self.head = self.head.next
# Задача 8: Подсчет количества элементов
def count(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count
# Задача 9: Программа с вводом пользователя
my_list = LinkedList()

print("Введите 5 чисел:")

for i in range(5):
    num = int(input())
    my_list.add_last(num)

print("Список:")
my_list.print_list()

print("Количество элементов:", my_list.count())

print("Разворачиваем список...")
my_list.reverse()

print("После разворота:")
my_list.print_list()

# Задача 10: Разворот списка
def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
