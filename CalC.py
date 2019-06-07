from tkinter import *

class calculator:
    def __init__(self):
        self.root=Tk()
        self.result = Label(self.root, text="", width="6", height="3", bg="white")
        self.result.grid(row=0,column=0)
        self.btn1 = Button(self.root, text="1", width="6", height="3", bg="pink", command=lambda: self.print_num("1")).grid(
            row=1, column=0)
        self.btn2 = Button(self.root, text="2", width="6", height="3", bg="pink", command=lambda: self.print_num("2")).grid(row=1,
                                                                                                             column=1)
        self.btn3 = Button(self.root, text="3", width="6", height="3", bg="pink", command=lambda: self.print_num("3")).grid(row=1,
                                                                                                             column=2)
        self.btnPlus = Button(self.root, text="+", width="6", height="3", bg="pink", command=lambda: self.operator("+")).grid(row=1, column=3)

        self.btn4 = Button(self.root, text="4", width="6", height="3", bg="pink", command=lambda: self.print_num("4")).grid(row=2,
                                                                                                             column=0)
        self.btn5 = Button(self.root, text="5", width="6", height="3", bg="pink", command=lambda: self.print_num("5")).grid(row=2,
                                                                                                             column=1)
        self.btn6 = Button(self.root, text="6", width="6", height="3", bg="pink", command=lambda: self.print_num("6")).grid(row=2,
                                                                                                             column=2)
        self.btnSub = Button(self.root, text="-", width="6", height="3", bg="pink", command=lambda: self.operator("-")).grid(row=2, column=3)

        self.btn7 = Button(self.root, text="7", width="6", height="3", bg="pink", command=lambda: self.print_num("7")).grid(row=3,
                                                                                                             column=0)
        self.btn8 = Button(self.root, text="8", width="6", height="3", bg="pink", command=lambda: self.print_num("8")).grid(row=3,
                                                                                                             column=1)
        self.btn9 = Button(self.root, text="9", width="6", height="3", bg="pink", command=lambda: self.print_num("9")).grid(row=3,
                                                                                                             column=2)
        self.btnMul = Button(self.root, text="*", width="6", height="3", bg="pink", command=lambda: self.operator("*")).grid(row=3, column=3)

        self.btn0 = Button(self.root, text="0", width="6", height="3", bg="pink", command=lambda: self.print_num("0")).grid(row=4,
                                                                                                             column=0)
        self.btnDiv = Button(self.root, text="/", width="6", height="3", bg="pink", command=lambda: self.operator("/")).grid(row=4, column=1)
        self.btnClr = Button(self.root, text="C", width="6", height="3", bg="pink", command=lambda: self.clear()).grid(row=4, column=2)
        self.btnEquals = Button(self.root, text="=", width="6", height="3", bg="pink", command=lambda: self.publish()).grid(row=4, column=3)

        self.root.mainloop()

    def print_num(self,num):
        new_text=self.result['text'] + num
        self.result.configure(text=new_text)

    def clear(self):
        self.result.configure(text="")

    def operator(self,sign):
        self.operator_name=sign
        self.first_num=int(self.result['text'])
        self.result.configure(text="")

    def publish(self):
        self.second_num=int(self.result['text'])
        if self.operator_name=="+":
            self.result.configure(text=str(self.first_num+self.second_num))
        elif self.operator_name=="-":
            self.result.configure(text=str(self.first_num-self.second_num))
        elif self.operator_name=="*":
            self.result.configure(text=str(self.first_num*self.second_num))
        else:
            self.result.configure(text=str(self.first_num/self.second_num))

obj1=calculator()