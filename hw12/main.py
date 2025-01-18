# Task 12.1
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          for line in file:
              current_line = re.findall(r">(.+)</", line)
              if len(current_line):
                  with open(result_file, "a", encoding='utf-8') as result:
                      result.write(f"{current_line[0]}\n")

delete_html_tags("draft.html")

# Task 12.2
class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
            return f"User: {self.user}\nItems:{all_products}"

    def get_total(self):
        total = 0
        for product, count in self.products.items():
            total += (product.price * count)
        return total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 40


