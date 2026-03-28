import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("360x600")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.colors = {
            "bg": "#1E1E2E",
            "display_bg": "#2A2A3E",
            "display_fg": "#FFFFFF",
            "btn_bg": "#3A3A4E",
            "btn_fg": "#FFFFFF",
            "btn_hover": "#4A4A5E",
            "operator_bg": "#FF6B6B",
            "operator_fg": "#FFFFFF",
            "equals_bg": "#4ECDC4",
            "equals_fg": "#1E1E2E",
            "clear_bg": "#FF8C42",
            "clear_fg": "#FFFFFF"
        }
        
        self.root.configure(bg=self.colors["bg"])
        
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        display_frame = tk.Frame(self.root, bg=self.colors["display_bg"], bd=0)
        display_frame.pack(pady=20, padx=20, fill="both")
        
        input_display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 32, "bold"),
            bg=self.colors["display_bg"],
            fg=self.colors["display_fg"],
            bd=0,
            justify="right",
            insertbackground=self.colors["display_fg"]
        )
        input_display.pack(pady=15, padx=20, fill="both")
        
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        buttons = [
            ("C", 1, 0, "clear"),
            ("(", 1, 1, "operator"),
            (")", 1, 2, "operator"),
            ("/", 1, 3, "operator"),
            ("7", 2, 0, "number"),
            ("8", 2, 1, "number"),
            ("9", 2, 2, "number"),
            ("*", 2, 3, "operator"),
            ("4", 3, 0, "number"),
            ("5", 3, 1, "number"),
            ("6", 3, 2, "number"),
            ("-", 3, 3, "operator"),
            ("1", 4, 0, "number"),
            ("2", 4, 1, "number"),
            ("3", 4, 2, "number"),
            ("+", 4, 3, "operator"),
            ("0", 5, 0, "number"),
            (".", 5, 1, "number"),
            ("^", 5, 2, "operator"),
            ("=", 5, 3, "equals"),
        ]
        
        for (text, row, col, btn_type) in buttons:
            self.create_button(button_frame, text, row, col, btn_type)
            
    def create_button(self, frame, text, row, col, btn_type):
        if btn_type == "clear":
            bg_color = self.colors["clear_bg"]
            fg_color = self.colors["clear_fg"]
        elif btn_type == "operator":
            bg_color = self.colors["operator_bg"]
            fg_color = self.colors["operator_fg"]
        elif btn_type == "equals":
            bg_color = self.colors["equals_bg"]
            fg_color = self.colors["equals_fg"]
        else:
            bg_color = self.colors["btn_bg"]
            fg_color = self.colors["btn_fg"]
            
        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 20, "bold"),
            bg=bg_color,
            fg=fg_color,
            bd=0,
            relief="flat",
            command=lambda: self.on_button_click(text, btn_type)
        )
        btn.grid(row=row, column=col, padx=8, pady=8, sticky="nsew", ipady=15)
        
        btn.bind("<Enter>", lambda e: self.on_hover(e, btn_type, True))
        btn.bind("<Leave>", lambda e: self.on_hover(e, btn_type, False))
        
        frame.rowconfigure(row, weight=1)
        frame.columnconfigure(col, weight=1)
        
    def on_hover(self, event, btn_type, is_hover):
        if btn_type == "clear":
            bg = self.colors["clear_bg"]
        elif btn_type == "operator":
            bg = self.colors["operator_bg"]
        elif btn_type == "equals":
            bg = self.colors["equals_bg"]
        else:
            bg = self.colors["btn_hover"] if is_hover else self.colors["btn_bg"]
        event.widget.config(bg=bg)
        
    def on_button_click(self, value, btn_type):
        if btn_type == "clear":
            self.expression = ""
            self.input_text.set("")
        elif btn_type == "equals":
            self.calculate()
        elif value == "^":
            self.expression += "**"
            self.input_text.set(self.expression)
        else:
            self.expression += str(value)
            self.input_text.set(self.expression)
            
    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Ошибка")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
