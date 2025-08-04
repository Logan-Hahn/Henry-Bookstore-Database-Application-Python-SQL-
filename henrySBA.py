import tkinter as tk
from tkinter import ttk
from henryDAO import HenryDAO
from HenryInterfaceClasses import Author

class HenrySBA:
    def __init__(self, window_frame): 
        self.window_frame = window_frame
        self.dao = HenryDAO()
        self.author_label = ttk.Label(self.window_frame, text="Author Selection:")
        self.author_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.author_combobox = ttk.Combobox(self.window_frame, state="readonly")
        self.author_combobox.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.author_combobox.bind("<<ComboboxSelected>>", self.on_author_selected)
        self.book_label = ttk.Label(self.window_frame, text="Book Selection:")
        self.book_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.book_combobox = ttk.Combobox(self.window_frame, state="readonly")
        self.book_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="e")
        self.book_combobox.bind("<<ComboboxSelected>>", self.on_book_selected)
        self.price_label = ttk.Label(self.window_frame, text="Price: ")
        self.price_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')
        self.price_value_label = ttk.Label(self.window_frame, text="")
        self.price_value_label.grid(row=0, column=2, padx=10, pady=10, sticky='w')
        self.tree = ttk.Treeview(self.window_frame, columns=("Branch", "Copies"), show="headings")
        self.tree.heading("Branch", text="Branch Name")
        self.tree.heading("Copies", text="Copies Available")
        self.tree.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.load_authors()
    
    def load_authors(self):
        self.authors_list = self.dao.get_author_data()
        author_names = [str(author) for author in self.authors_list]
        self.author_combobox['values'] = author_names
        if author_names:
            self.author_combobox.current(0)
            self.on_author_selected(None)

    def on_author_selected(self, event):
        chosen_index = self.author_combobox.current()
        chosen_author = self.authors_list[chosen_index]
        self.book_list = self.dao.get_books_by_author(chosen_author.author_num)
        book_titles = [book.title for book in self.book_list]
        self.book_combobox['values'] = book_titles
        if book_titles:
            self.book_combobox.current(0)
            self.on_book_selected(None)

    def on_book_selected(self, event):
        chosen_book_index = self.book_combobox.current()
        selected_book = self.book_list[chosen_book_index]
        self.price_value_label.config(text=f"${selected_book.price:.2f}")
        branches = self.dao.get_branch_inventory(selected_book.book_code)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for branch in branches:
            self.tree.insert("", "end", values=(branch.branch_name, branch.num_copies))

