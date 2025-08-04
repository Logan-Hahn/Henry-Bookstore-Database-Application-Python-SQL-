import tkinter as tk
from tkinter import ttk
from henrySBA import HenrySBA
from henrySBC import HenrySBC
from henrySBP import HenrySBP
 
class Henry:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Henry's Bookstore Search")
        self.main_window.geometry("800x400")
        self.navigation_tabs = ttk.Notebook(self.main_window)
        self.author_tab = ttk.Frame(self.navigation_tabs)
        self.category_tab = ttk.Frame(self.navigation_tabs)
        self.publisher_tab = ttk.Frame(self.navigation_tabs)
        self.navigation_tabs.add(self.author_tab, text='Search by Author')
        self.navigation_tabs.add(self.category_tab, text='Search by Category')
        self.navigation_tabs.add(self.publisher_tab, text='Search by Publisher')
        self.navigation_tabs.pack(expand=True, fill='both')
        HenrySBA(self.author_tab)
        HenrySBC(self.category_tab)
        HenrySBP(self.publisher_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = Henry(root) 
    root.mainloop()
