import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator APP")
        self.root.geometry("380x550")
        self.root.configure(bg="#1e1e1e")  
        self.root.resizable(False, False)

        self.expression = ""
        self.display_text = tk.StringVar()

        # Create the display screen
        self.create_display()
        
        
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, width=380, height=100, bd=0, bg="#1e1e1e")
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        display_label = tk.Label(
            display_frame, 
            textvariable=self.display_text, 
            font=("Helvetica", 28, "bold"), 
            bg="#1e1e1e", 
            fg="#ffffff", 
            anchor="e", 
            padx=20
        )
        display_label.pack(expand=True, fill=tk.BOTH)
        self.display_text.set("0")

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    
        button_layout = [
            ['C', '^', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '\\', '=']
        ]

        # Configure grid weights to make buttons expand evenly
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.columnconfigure(j, weight=1)

        for row_idx, row in enumerate(button_layout):
            for col_idx, char in enumerate(row):
                
                if char in ['C', '^', '%', '/', '*', '-', '+', '\\', '=']:
                    bg_color = "#ff9500" if char == "=" else "#333333"
                    fg_color = "#ffffff"
                    active_bg = "#ffaa33" if char == "=" else "#555555"
                else:
                    bg_color = "#2c2c2c"
                    fg_color = "#ffffff"
                    active_bg = "#444444"

                btn = tk.Button(
                    button_frame, 
                    text=char, 
                    font=("Helvetica", 18, "bold"),
                    bg=bg_color, 
                    fg=fg_color, 
                    activebackground=active_bg,
                    activeforeground="#ffffff",
                    bd=0, 
                    relief="flat",
                    command=lambda x=char: self.on_button_click(x)
                )
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_text.set("0")
        
        elif char == '=':
            try:
                
                expr_to_eval = self.expression.replace('^', '**').replace('\\', '//')
                
                # Prevent evaluation if empty
                if not expr_to_eval:
                    return
                
                result = eval(expr_to_eval)
                
                
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                    
                self.display_text.set(result)
                self.expression = str(result)  
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.display_text.set("0")
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_text.set("0")
                
        else:
            
            if self.display_text.get() == "0" and char not in ['^', '%', '/', '*', '-', '+', '\\']:
                self.expression = char
            else:
                self.expression += char
                
            self.display_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()