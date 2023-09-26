from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ""
price_product = [1.66, 10.34, 65, 43.67, 7.56, 80.34, 25, 3.67]
price_service = [6.66, 1.4, 6, 3.67, 14.66, 430.34, 6.5, 13.67]
price_extra = [4.46, 70.3, 5, 4.67, 3.65, 40.34, 35, 13.27]


def click_operation(number):
    global operator
    operator = operator + str(number)
    visor_calc.delete(0, END)
    visor_calc.insert(END, operator)
    
def del_calc():
    global operator
    operator = ""
    visor_calc.delete(0, END)
    
def result_calc():
    global operator
    result = str(eval(operator))
    visor_calc.delete(0, END)
    visor_calc.insert(0, result)
    operator = ""

def check_able():
    x = 0
    for c in square_product:
        if var_product[x].get() == 1:
            square_product[x].config(state = NORMAL)
            if square_product[x].get() == '0':
                square_product[x].delete(0, END)
            square_product[x].focus()
        else:
            c.config(state = DISABLED)
            text_product[x].set('0')
        x += 1
    x = 0
    for c in square_service:
        if var_service[x].get() == 1:
            square_service[x].config(state = NORMAL)
            if square_service[x].get() == '0':
                square_service[x].delete(0, END)
            square_service[x].focus()
        else:
            c.config(state = DISABLED)
            text_service[x].set('0')
        x += 1
    x = 0
    for c in square_extra:
        if var_extra[x].get() == 1:
            square_extra[x].config(state = NORMAL)
            if square_extra[x].get() == '0':
                square_extra[x].delete(0, END)
            square_extra[x].focus()
        else:
            c.config(state = DISABLED)
            text_extra[x].set('0')
        x += 1

def total():
    sub_total_product = 0
    p = 0
    for amount in text_product:
        sub_total_product = sub_total_product + (float(amount.get()) * price_product[p])
        p += 1

    sub_total_service = 0
    p = 0
    for amount in text_service:
        sub_total_service = sub_total_service + (float(amount.get()) * price_service[p])
        p += 1

    sub_total_extra = 0
    p = 0
    for amount in text_extra:
        sub_total_extra = sub_total_extra + (float(amount.get()) * price_extra[p])
        p += 1

    sub_total = sub_total_product + sub_total_service + sub_total_extra
    tax = sub_total * 0.21
    total = sub_total + tax
    
    var_cost_product.set(f'{round(sub_total_product, 2)} €')
    var_cost_service.set(f'{round(sub_total_service, 2)} €')
    var_cost_extra.set(f'{round(sub_total_extra, 2)} €')
    var_subtotal.set(f'{round(sub_total, 2)} €')
    var_tax.set(f'{round(tax, 2)} €')
    var_total.set(f'{round(total, 2)} €')
    
def print_ticket():
    text_rec.delete(1.0, END)
    num_ticket = f'N#{random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    date_ticket = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    text_rec.insert(END, f'Datos: \t{num_ticket}\t\t{date_ticket}\n')
    text_rec.insert(END, f'*' * 47 + '\n')
    text_rec.insert(END, f'Item\t\tCant. \tCosto Items\n')
    text_rec.insert(END, f'-' * 54 + '\n')
    
    x = 0
    for prod in text_product:
        if prod.get() != "0":
            text_rec.insert(END, f'{l_product[x]}\t\t{prod.get()}\t'
                            f'€ {int(prod.get()) * price_product[x]}\n')
        x += 1
        
    x = 0
    for service in text_service:
        if service.get() != "0":
            text_rec.insert(END, f'{l_service[x]}\t\t{service.get()}\t'
                            f'€ {int(service.get()) * price_service[x]}\n')
        x += 1
        
    x = 0
    for extra in text_extra:
        if extra.get() != "0":
            text_rec.insert(END, f'{l_extra[x]}\t\t{extra.get()}\t'
                            f'€ {int(extra.get()) * price_service[x]}\n')
        x += 1
        
    text_rec.insert(END, f'-' * 54 + '\n')
    text_rec.insert(END, f'Total Comida:\t\t\t{var_cost_product.get()}\n')
    text_rec.insert(END, f'Total Bebida:\t\t\t{var_cost_service.get()}\n')
    text_rec.insert(END, f'Total Postre:\t\t\t{var_cost_extra.get()}\n')
    text_rec.insert(END, f'-' * 54 + '\n')
    text_rec.insert(END, f'Total impuestos:\t\t\t{var_tax.get()}\n')
    text_rec.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    text_rec.insert(END, f'-' * 54 + '\n')
    text_rec.insert(END, f'Total:\t\t\t{var_total.get()}\n')
    text_rec.insert(END, f'*' * 47 + '\n')
    text_rec.insert(END, f'Gracias por su visita')
    
def save_ticket():
    info_ticket = text_rec.get(1.0, END)
    file = filedialog.asksaveasfile(mode = 'w', defaultextension = ".txt")
    file.write(info_ticket)
    file.close()
    messagebox.showinfo("INFORMACIÓN", "El recibo ha sido guardado")
    
def reset():
    text_rec.delete(0.1, END)
    
    for text in text_product:
        text.set("0")
    for text in text_service:
        text.set("0")
    for text in text_extra:
        text.set("0")
        
    for square in square_product:
        square.config(state = DISABLED)
    for square in square_service:
        square.config(state = DISABLED)
    for square in square_extra:
        square.config(state = DISABLED)

    for v in var_product:
        v.set(0)
    for v in var_service:
        v.set(0)    
    for v in var_extra:
        v.set(0)
        
aplication = Tk()

# tamaño ventana
aplication.geometry('1112x720+0+0')

# evitar maximizar
aplication.resizable(0, 0)

# titulo ventana
aplication.title("Sistema de facturación")

# color de fondo
aplication.config(bg="grey")

# panel superior
p_sup = Frame(aplication, bd = 1, relief = FLAT)
p_sup.pack(side = TOP)

# etiqueta título
tag_title = Label(p_sup, text = "Sistema de facturación", fg = "white", 
                  font = ("Dosis", 58), bg = "burlywood", width = 23)
tag_title.grid(row = 0, column = 0)

# panel izquierdo
p_left = Frame(aplication, bd = 1, relief = FLAT)
p_left.pack(side = LEFT)

# panel costos

p_cost = Frame(p_left, bd = 1, relief = FLAT, bg = "blue", padx = 50)
p_cost.pack(side = BOTTOM)

# panel productos
p_prod = LabelFrame(p_left, text = "Comidas", font = ("Dosis", 15, "bold"), 
                    bd = 1, relief = FLAT, fg = "azure4")
p_prod.pack(side = LEFT)

# panel servicios
p_serv = LabelFrame(p_left, text = "Bebidas", font = ("Dosis", 15, "bold"), 
                    bd = 1, relief = FLAT, fg = "azure4")
p_serv.pack(side = LEFT)

# panel extras
p_extra = LabelFrame(p_left, text = "Postres", font = ("Dosis", 15, "bold"), 
                    bd = 1, relief = FLAT, fg = "azure4")
p_extra.pack(side = LEFT)

# panel derecho
p_right = Frame(aplication, bd = 1, relief = FLAT)
p_right.pack(side = RIGHT)

# panel calculadora
p_calc = Frame(p_right,  bd = 1, relief = FLAT, bg = "burlywood")
p_calc.pack()

# panel recibo
p_rec = Frame(p_right,  bd = 1, relief = FLAT, bg = "burlywood")
p_rec.pack()

# panel botones
p_but= Frame(p_right,  bd = 1, relief = FLAT, bg = "burlywood")
p_but.pack()

# listas 
l_product = ["Pollo", "Salmón", "Bacalao", "Arroz", "Paella", "Huevos", "Tortilla", "Ensalada"]
l_service = ["Cocacola", "Fanta", "Vino", "Mahou", "Heineken", "Agua", "Zumo", "Mosto"]
l_extra = ["Tarta", "Pastel", "Bizcocho", "Fruta", "Helado", "Flan", "Gelatina", "Yougour"]

# generar item productos
var_product = []
square_product = []
text_product = []
count = 0
for product in l_product:
    var_product.append("")
    var_product[count] = IntVar()
    product = Checkbutton(p_prod, 
                          text = product.title(), 
                          font = ("Dosis", 15, "bold"),
                          onvalue = 1, 
                          offvalue = 0, 
                          variable = var_product[count],
                          command = check_able)
    # generar cuadros de entrada
    square_product.append("")
    text_product.append("")
    text_product[count] = StringVar()
    text_product[count].set("0")
    square_product[count] = Entry(p_prod,
                                  font = ("Dosis", 18, "bold"),
                                  bd = 1,
                                  width = 6,
                                  state = DISABLED,
                                  textvariable = text_product[count])
    
    product.grid(row = count, 
            column = 0, 
            sticky = W
            )
    square_product[count].grid(row = count,
                         column = 1)   
    count += 1
    
# generar item servicios
var_service = []
square_service = []
text_service = []
count = 0
for service in l_service:
    var_service.append("")
    var_service[count] = IntVar()
    service = Checkbutton(p_serv, 
                          text = service.title(), 
                          font = ("Dosis", 15, "bold"),
                          onvalue = 1, 
                          offvalue = 0, 
                          variable = var_service[count],
                          command = check_able)
    # generar cuadros de entrada
    square_service.append("")
    text_service.append("")
    text_service[count] = StringVar()
    text_service[count].set("0")
    square_service[count] = Entry(p_serv,
                                  font = ("Dosis", 18, "bold"),
                                  bd = 1,
                                  width = 6,
                                  state = DISABLED,
                                  textvariable = text_service[count])
    service.grid(row = count, 
                 column = 0, 
                 sticky = W)
    square_service[count].grid(row = count,
                         column = 1)
    
    count += 1

# generar item extra
var_extra = []
square_extra = []
text_extra = []
count = 0
for extra in l_extra:
    var_extra.append("")
    var_extra[count] = IntVar()
    extra = Checkbutton(p_extra, 
                        text = extra.title(), 
                        font = ("Dosis", 15, "bold"),
                        onvalue = 1, 
                        offvalue = 0, 
                        variable = var_extra[count],
                        command = check_able)
    extra.grid(row = count, 
            column = 0, 
            sticky = W)
# cuadros entrada
    square_extra.append("")
    text_extra.append("")
    text_extra[count] = StringVar()
    text_extra[count].set("0")
    square_extra[count] = Entry(p_extra,
                                font = ("Dosis", 18, "bold"),
                                bd = 1,
                                width = 6,
                                state = DISABLED,
                                textvariable = text_extra[count])
    square_extra[count].grid(row = count,
                         column = 1)
    count += 1

#variables
var_cost_product = StringVar()
var_cost_service = StringVar()
var_cost_extra = StringVar()
var_subtotal = StringVar()
var_tax = StringVar()
var_total = StringVar()

# Etiquetas de costos primera columna (0, 1)
label_cost_product = Label(p_cost,
                           text = "Total comida: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_product.grid(row = 0, column = 0)

text_cost_product = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_cost_product)
text_cost_product.grid(row = 0, column = 1)

label_cost_service = Label(p_cost,
                           text = "Total bebida: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_service.grid(row = 1, column = 0)

text_cost_service = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_cost_service)
text_cost_service.grid(row = 1, column = 1)

label_cost_extra = Label(p_cost,
                           text = "Total postre: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_extra.grid(row = 2, column = 0)

text_cost_extra = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_cost_extra)
text_cost_extra.grid(row = 2, column = 1)

# Segunda columna (2,3) impuestos y totales
label_cost_subtotal = Label(p_cost,
                           text = "Subtotal: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_subtotal.grid(row = 0, column = 2, padx = 41)

text_cost_subtotal = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_subtotal)
text_cost_subtotal.grid(row = 0, column = 3, padx = 41)

label_cost_tax = Label(p_cost,
                           text = "Impuestos: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_tax.grid(row = 1, column = 2, padx = 41)

text_cost_tax = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_tax)
text_cost_tax.grid(row = 1, column = 3, padx = 41)

label_cost_total = Label(p_cost,
                           text = "Total: ",
                           font = ("Dosis", 12, "bold")
                           )
label_cost_total.grid(row = 2, column = 2, padx = 41)

text_cost_total = Entry(p_cost,
                          font = ("Dosis", 15, "bold"),
                          bd = 1,
                          width = 10,
                          state = "readonly",
                          textvariable = var_total)
text_cost_total.grid(row = 2, column = 3, padx = 41)

# botones
buttons = ["total", "recibo", "guardar", "resetear"]
buttons_created = []
columns = 0
for button in buttons:
    button = Button(p_but,
                    text = button.title(),
                    font = ("Dosis", 12, "bold"),
                    width = 9,
                    height = 1,
                    bd = 1,
                    bg = "azure4")
    buttons_created.append(button)
    
    button.grid(row = 0, column = columns)
    columns += 1
    
buttons_created[0].config(command = total)
buttons_created[1].config(command = print_ticket)
buttons_created[2].config(command = save_ticket)
buttons_created[3].config(command = reset)
# area recibo
text_rec = Text(p_rec,
                width = 40,
                height = 12,
                font = ("Dosis", 12, "bold"),
                bd = 1)
text_rec.grid(row = 0, column = 0)

# calculadora
visor_calc = Entry(p_calc,
                   font = ("Dosis", 12, "bold"),
                   width = 32,
                   bd = 1)
visor_calc.grid(row = 0, column = 0, columnspan = 4)

but_calc = ["7", "8", "9", "+", 
            "4", "5", "6", "-",
            "1", "2", "3", "x", 
            "=", "CE", "0", "/"]

but_save = []

row_calc = 1
col_calc = 0
for but in but_calc:
    button_calc = Button(p_calc, 
                    text = but.title(),
                    font = ("Dosis", 12, "bold"),
                    width = 7,
                    height = 2,
                    bd = 1,
                    bg = "azure4")
    
    but_save.append(button_calc)
    button_calc.grid(row = row_calc, 
                     column = col_calc)
    if col_calc == 3:
        row_calc += 1
        
    col_calc += 1
    
    if col_calc == 4:
        col_calc = 0

but_save[0].config(command = lambda : click_operation("7"))
but_save[1].config(command = lambda : click_operation("8"))
but_save[2].config(command = lambda : click_operation("9"))
but_save[3].config(command = lambda : click_operation("+"))
but_save[4].config(command = lambda : click_operation("4"))
but_save[5].config(command = lambda : click_operation("5"))
but_save[6].config(command = lambda : click_operation("6"))
but_save[7].config(command = lambda : click_operation("-"))
but_save[8].config(command = lambda : click_operation("1"))
but_save[9].config(command = lambda : click_operation("2"))
but_save[10].config(command = lambda : click_operation("3"))
but_save[11].config(command = lambda : click_operation("*"))
but_save[12].config(command = result_calc)
but_save[13].config(command = del_calc)
but_save[14].config(command = lambda : click_operation("0"))
but_save[15].config(command = lambda : click_operation("/"))


aplication.mainloop()