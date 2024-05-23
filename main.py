import tkinter as tk
 
 
class CalculatorApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Simple Calculator - The Pycodes")
       self.root.geometry("350x430")
       self.root.resizable(False, False)
       self.root.configure(bg="#1e1e1e")
 
 
       self.equation = ""
 
 
       self.create_widgets()
 
 
   def create_widgets(self):
       self.result_var = tk.StringVar()
 
 
       entry_frame = tk.Frame(self.root, bg="#1e1e1e")
       entry_frame.grid(row=0, column=0, columnspan=4, pady=20)
 
 
       entry = tk.Entry(entry_frame, font=("Arial", 24), textvariable=self.result_var, bd=0, insertwidth=4, width=14,
                        justify="right", bg="#1e1e1e", fg="white")
       entry.grid(row=0, column=0, ipady=8)
 
 
       buttons = [
           ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
           ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
           ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
           ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
       ]
 
 
       for (text, row, column) in buttons:
           btn = tk.Button(self.root, text=text, font=("Arial", 18), width=5, height=2, bd=1, fg="#fff", bg="#2a2d36",
                           command=lambda t=text: self.button_click(t))
           btn.grid(row=row, column=column, padx=5, pady=5)
 
 
       self.root.bind('<Return>', lambda event: self.button_click('='))
 
 
   def button_click(self, value):
       if value == 'C':
           self.equation = ""
       elif value == '=':
           try:
               result = str(eval(self.equation))
               self.equation = result
           except Exception as e:
               result = "Error"
       else:
           self.equation += value
 
 
       self.result_var.set(self.equation)
 
 
if __name__ == "__main__":
   root = tk.Tk()
   app = CalculatorApp(root)
   root.mainloop()
