import tkinter as tk
black = "#000"
white = "#fff"
green = "#2f0"
red = "#f00"
orange = "#f80"
digit_font=("Arial", 24, "bold")
large_font=("Arial", 40, "bold")
small_font=("Arial", 16)
defolt_font=("Arial", 20)
class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("calculator")
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        self.total_exp=""
        self.carrent_exp=""
        self.digits={7:(1,1), 8:(1,2), 9:(1,3),
                     4:(2,1), 5:(2,2), 6:(2,3),
                     1:(3,1), 2:(3,2), 3:(3,3),
                     0:(4,1), ".":(4,2)}
        self.operations={"/":"\u00f7", "*":"\u00d7", "+":"+", "-":"-"}
        self.create_operations_buttons()
        self.create_digits_button()
        self.sqrt_button()
        self.square_button()
        self.clear_button()
        self.equal_button()
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        self.total_label, self.label=self.create_display_label()
    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221)
        frame.pack(expand=True,fill="both")
        return frame
    # def create_label(self):
    #     total_label=tk.Label(self.display_frame,text=self.total_exp,bg=white,fg=green,anchor=tk.E,padx=24,font=small_font)
    #     total_label.pack(expand=True,fill="both")
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def create_digits_button(self):
        for digit,grid_value in self.digits.items():
            btn=tk.Button(self.buttons_frame,text=str(digit),bg=black,fg=white,font=digit_font,command=lambda x=digit:self.add_exp(x))
            btn.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)
    def create_operations_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            btn=tk.Button(self.buttons_frame,text=symbol,bg=black,fg=white,font=digit_font,command=lambda x=operator:self.add_operator(x))
            btn.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def sqrt(self):
        self.carrent_exp=str(eval(f"{self.carrent_exp}**0.5"))
        self.update_label()
    def sqrt_button(self):
        btn=tk.Button(self.buttons_frame,text="\u221ax",bg=black,fg=white,font=digit_font,command=self.sqrt)
        btn.grid(row=0,column=3,sticky=tk.NSEW)
    def square(self):
        self.carrent_exp=str(eval(f"{self.carrent_exp}**2"))
        self.update_label()
    def square_button(self):
        btn=tk.Button(self.buttons_frame, text="x\u00b2", bg=black, fg=white, font=digit_font,command=self.square)
        btn.grid(row=0, column=2,sticky=tk.NSEW)
    def clear(self):
        self.carrent_exp=""
        self.total_exp=""
        self.update_label()
        self.update_total_label()
    def clear_button(self):
        btn=tk.Button(self.buttons_frame, text="C", bg=black, fg=white, font=digit_font,command=self.clear)
        btn.grid(row=0, column=1,sticky=tk.NSEW)
    def equal(self):
        self.total_exp+=self.carrent_exp
        self.update_total_label()
        try:
            self.carrent_exp=str(eval(self.total_exp))
            self.total_exp=""
        except Exception:
            self.carrent_exp="Error"
        finally:
            self.update_label()
    def equal_button(self):
        btn = tk.Button(self.buttons_frame, text="=", bg=black, fg=white, font=digit_font,command=self.equal)
        btn.grid(row=4, column=3,columnspan=2,sticky=tk.NSEW)
    def add_operator(self,operator):
        self.carrent_exp+=operator
        self.total_exp+=self.carrent_exp
        self.carrent_exp=""
        self.update_label()
        self.update_total_label()
    def add_exp(self,value):
        self.carrent_exp+=str(value)
        self.update_label()
    def create_display_label(self):
        total_label=tk.Label(self.display_frame,text=self.total_exp,bg=white,font=small_font)
        total_label.pack(expand=True,fill="both")
        label=tk.Label(self.display_frame,text=self.carrent_exp,bg=white,font=large_font)
        label.pack(expand=True,fill="both")
        return total_label, label
    def update_total_label(self):
        exp=self.total_exp
        for operator, symbol in self.operations.items():
            exp=exp.replace(operator,f"{symbol}")
        self.total_label.config(text=exp)
    def update_label(self):
        self.label.config(text=self.carrent_exp[:11])
    def run(self):
        self.window.mainloop()
calc=Calculator()
calc.run()
