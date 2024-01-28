import tkinter as tk
from tkinter import ttk
from functools import partial
from interface import PasswordGeneratorGUI

def main():
    app = PasswordGeneratorGUI()
    app.run()

if __name__ == "__main__":
    main()