import uniform 
import binomial
from tkinter import *
from tkinter import messagebox
from prettytable import PrettyTable

lst=[]
def clear():
    if len(lst) != 0:
      for i in lst:
          i.destroy()
    lst.clear()

def gui_manage():
    info = {}
    clear()

    if not lb.get(): min=0
    else: min =lb.get()

    if not amount.get() or not rb.get():
          messagebox.showerror(title="Помилка вводу", message="Введіть дані для генерації вибірки")
          return
    Label(text="Початкова таблиця", fg='blue', font='Courier 11 bold').grid(row=0, column=2, sticky=W+E)
    if v.get() == 1:
       info = binomial.info_func(int(amount.get()),int(min),int(rb.get()),float(s.get()))

       init_table = PrettyTable()
       init_table.add_column('xi', info['xi_copy'])
       init_table.add_column('mi', info['mi_copy'])
       init_table.add_column('pi', info['pi_copy'])
       init_table.add_column('n*pi', info['n*pi_copy'])
      
       str_table = init_table.get_string()
       table_text = Text(width=str_table.index('\n'), height=str_table.count('\n')+1, fg='maroon')
       lst.append(table_text)
       table_text.insert(END, init_table)
       last_row=str_table.count('\n')-3
       table_text.grid(row=1, column=2,rowspan=last_row,padx=(0,10), sticky=W+E)
       table_text.config(state=DISABLED)
      
       last_row+=1
       lst.append(Label(text='x^2 емпіричне = {}'.format(info['x^2emp']), font='Courier 11 bold'))
       lst[1].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       lst.append(Label(text='x^2 критичне = {}'.format(info['x^2kr']), font='Courier 11 bold'))
       lst[2].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       label_text=StringVar()
       if info['x^2emp']<info['x^2kr']: label_text.set('Так як x^2 емпіричне < x^2 критичного, гіпотезу приймаємо')
       else: label_text.set('Так як x^2 емпіричне > x^2 критичного, гіпотезу відхиляємло')
       lst.append(Label(textvariable=label_text, font='Courier 11 bold', fg='blue'))
       lst[3].grid(row=last_row, column=2, columnspan=2, sticky=W)
 

       Label(text='Кінцева таблиця', font='Courier 11 bold',fg='blue').grid(row=0, column=3, sticky=W+E)
       final_table = PrettyTable()
       final_table.add_column('xi', info['xi'])
       final_table.add_column('mi', info['mi'])
       final_table.add_column('pi', info['pi'])
       final_table.add_column('n*pi', info['n*pi'])
     
       str_table = final_table.get_string()
       table_text = Text(width=str_table.index('\n'), height=str_table.count('\n')+1, fg='maroon')
       lst.append(table_text)
       table_text.insert(END, final_table)
       table_text.grid(row=1, column=3,rowspan=str_table.count('\n')-2,padx=(0,10), sticky=W+E)
       table_text.config(state=DISABLED)

    elif v.get()==2: 
       info = uniform.info_func(int(amount.get()),int(min),int(rb.get()),float(s.get()))

       init_table = PrettyTable()
       init_table.add_column('(zi-1 ; zi]', info['i-vals_old'])
       init_table.add_column('zi''', info['zi_copy'])
       init_table.add_column('mi', info['mi_copy'])
       init_table.add_column('pi', info['pi_copy'])
       init_table.add_column('n*pi', info['n*pi_copy'])
      
       str_table = init_table.get_string()
       table_text = Text(width=str_table.index('\n'), height=str_table.count('\n')+1, fg='maroon')
       lst.append(table_text)
       table_text.insert(END, init_table)
       last_row=str_table.count('\n')-3
       table_text.grid(row=1, column=2,rowspan=last_row,padx=(0,10), sticky=W+E)
       table_text.config(state=DISABLED)
      
       last_row+=1
       lst.append(Label(text='x^2 емпіричне = {}'.format(info['x^2emp']), font='Courier 11 bold'))
       lst[1].grid(row=last_row, column=2, sticky=W)

       lst.append(Label(text='a = {}'.format(info['a']), font='Courier 11 bold'))
       lst[2].grid(row=last_row, column=3, sticky=W+E)
       last_row+=1

       lst.append(Label(text='x^2 критичне = {}'.format(info['x^2kr']), font='Courier 11 bold'))
       lst[3].grid(row=last_row, column=2, sticky=W)
       
       lst.append(Label(text='b = {}'.format(info['b']), font='Courier 11 bold'))
       lst[4].grid(row=last_row, column=3, sticky=W+E)
       last_row+=1

       label_text=StringVar()
       if info['x^2emp']<info['x^2kr']: label_text.set('Так як x^2 емпіричне < x^2 критичного, гіпотезу приймаємо')
       else: label_text.set('Так як x^2 емпіричне > x^2 критичного, гіпотезу відхиляємло')
       lst.append(Label(textvariable=label_text, font='Courier 11 bold', fg='blue'))
       lst[5].grid(row=last_row, column=2, columnspan=2, sticky=W)
 
       Label(text='Кінцева таблиця', font='Courier 11 bold',fg='blue').grid(row=0, column=3, sticky=W+E)
       final_table = PrettyTable()
       final_table.add_column('(zi-1 ; zi]', info['i-vals_new'])
       final_table.add_column('zi''', info['table']['zi'])
       final_table.add_column('mi', info['table']['mi'])
       final_table.add_column('pi', info['table']['pi'])
       final_table.add_column('n*pi', info['table']['n*pi'])
     
       str_table = final_table.get_string()
       table_text = Text(width=str_table.index('\n'), height=str_table.count('\n')+1, fg='maroon')
       lst.append(table_text)
       table_text.insert(END, final_table)
       table_text.grid(row=1, column=3,rowspan=str_table.count('\n')-3,padx=(0,10), sticky=W+E)
       table_text.config(state=DISABLED)
       
    else: 
        messagebox.showerror(title="Помилка розподілу", message="Оберіть тип розподілу")
        return


root = Tk()
root.title("Математична статистика")
v = IntVar() 
Radiobutton(root, text='Біномний розподіл', variable=v, value=1,font='Courier 11 bold').grid(row=0,column=0)
Radiobutton(root, text='Рівномірний розподіл', variable=v, value=2,font='Courier 11 bold').grid(row=0,column=1) 

amount_label = Label(root, text = "Величина вибірки",font='Courier 12').grid(row = 1, column = 0, pady=5, padx=10)  
amount = Entry(root,font='Courier 12')
amount.grid(row = 1, column = 1, pady=5, padx=10)  

lb_label = Label(root, text = "Ліва межа",font='Courier 12').grid(row = 2, column = 0, pady=5, padx=10) 
lb = Entry(root,font='Courier 12')
lb.grid(row = 2, column = 1, pady=5, padx=10)  


rb_label = Label(root, text = "Права межа",font='Courier 12').grid(row = 3, column = 0, pady=5, padx=10)  
rb = Entry(root,font='Courier 12')
rb.grid(row = 3, column = 1, pady=5, padx=10)  

sig_label = Label(root, text = "Рівень значущості",font='Courier 12').grid(row = 4, column = 0, pady=5, padx=10)  
s = DoubleVar(value=0.05) 
Radiobutton(root, text='0.001', variable=s, value=0.001,font='Courier 11 bold').grid(row=5,column=0)
Radiobutton(root, text='0.01', variable=s, value=0.01,font='Courier 11 bold').grid(row=6,column=0)
Radiobutton(root, text='0.05', variable=s, value=0.05,font='Courier 11 bold').grid(row=7,column=0)

submit = Button(root,text='Підтвердити', command=gui_manage, bg='#7fdb92')
submit.grid(row=8,column=0,pady=5, padx=5, sticky=E + W)

clr = Button(root,text='Очистити', command=clear, bg='#8fbaff')
clr.grid(row=8,column=1,pady=5, padx=5, sticky=E + W)
root.mainloop()
