"""
GUI Calculator Application
"""

import tkinter as tk


class CalculatorGUI:
    """Calculator GUI"""

    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 20),
            justify="right",
            bd=10
        )
        display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(
                root,
                text=button,
                width=8,
                height=3,
                font=("Arial", 12),
                command=lambda value=button: self.click(value)
            ).grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear Button
        tk.Button(
            root,
            text="C",
            width=16,
            height=2,
            font=("Arial", 12),
            command=self.clear
        ).grid(row=5, column=0, columnspan=2, padx=2, pady=2)

        # Backspace Button
        tk.Button(
            root,
            text="⌫",
            width=16,
            height=2,
            font=("Arial", 12),
            command=self.backspace
        ).grid(row=5, column=2, columnspan=2, padx=2, pady=2)

    def click(self, value):
        """Handle button click"""

        if value == "=":
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except (SyntaxError, ZeroDivisionError):
                self.display_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(value)
            self.display_var.set(self.expression)

    def clear(self):
        """Clear display"""
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        """Delete last character"""
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)


def main():
    """Application entry point"""
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()