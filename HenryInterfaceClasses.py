class Author:
    def __init__(self, author_num, first_name, last_name):
        self.author_num = author_num
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book:
    def __init__(self, book_code, title, price):
        self.book_code = book_code
        self.title = title
        self.price = price

class Branch:
    def __init__(self, branch_name, num_copies):
        self.branch_name = branch_name
        self.num_copies = num_copies
