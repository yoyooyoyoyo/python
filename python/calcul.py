import tkinter as tk
# from PIL import ImageTk, Image
import tkmacosx as Button

root = tk.Tk()
root.title("CHOI")
root.minsize(600, 400)

# # Label
# widget1 = tk.Label(
#     root,
#     text="이것은 Label입니다."
# )
# widget1.pack()
# #Button

# widget2 = tk.Label(root,
#                    )

# #Text
# widget3 = tk.Text(root)

# # Listbox
# widget4 = tk.Listbox(root)


# root.mainloop()

# 변수 선언
upper_frame = tk.Frame(root, width=400, height=70)
upper_frame.pack(pady=40)

down_frame = tk.Frame(root, width=400, height=100)
down_frame.pack(padx=10, pady=10)

entry = tk.Entry(upper_frame, width=20, font=(
    "Courier", 18), borderwidth=5, bg='pink')
entry.pack()
entry.insert(0, "")


def button_clicked(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry.delete(0, tk.END)


def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, tk.END)


def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0, tk.END)


def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0, tk.END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math == 'addition':
        entry.insert(0, f_num + int(second_number))

    if math == 'subtraction':
        entry.insert(0, f_num - int(second_number))

    if math == 'multiplication':
        entry.insert(0, f_num * int(second_number))

    if math == 'division':
        entry.insert(0, f_num / int(second_number))


btn1 = tk.Button(down_frame, text='1', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(1))
btn1.grid(column=0, row=2, padx=5, pady=5)
btn2 = tk.Button(down_frame, text='2', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(2))
btn2.grid(column=1, row=2, padx=5, pady=5)
btn3 = tk.Button(down_frame, text='3', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(3))
btn3.grid(column=2, row=2, padx=5, pady=5)
btn4 = tk.Button(down_frame, text='4', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(4))
btn4.grid(column=0, row=1, padx=5, pady=5)
btn5 = tk.Button(down_frame, text='5', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(5))
btn5.grid(column=1, row=1, padx=5, pady=5)
btn6 = tk.Button(down_frame, text='6', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(6))
btn6.grid(column=2, row=1, padx=5, pady=5)

btn7 = tk.Button(down_frame, text='7', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(7))
btn7.grid(column=0, row=0, padx=5, pady=5)
btn8 = tk.Button(down_frame, text='8', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(8))
btn8.grid(column=1, row=0, padx=5, pady=5)
btn9 = tk.Button(down_frame, text='9', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(9))
btn9.grid(column=2, row=0, padx=5, pady=5)


btn_pm = tk.Button(down_frame, text='+/-', padx=5, pady=10,
                   font=("Courier", 15), command=lambda: button_clicked('-'))
btn_pm.grid(column=0, row=3, padx=5, pady=5)
btn0 = tk.Button(down_frame, text='0', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked(0))
btn0.grid(column=1, row=3, padx=5, pady=5)
btn_p = tk.Button(down_frame, text='.', padx=15, pady=10, font=(
    "Courier", 15), command=lambda: button_clicked('.'))
btn_p.grid(column=2, row=3, padx=5, pady=5)
btn_mul = tk.Button(down_frame, text='X', padx=15, pady=10, font=(
    "Courier", 15), command=button_mul, bg="yellow")
btn_mul.grid(column=3, row=0, padx=5, pady=5)
btn_sub = tk.Button(down_frame, text='-', padx=15, pady=10,
                    font=("Courier", 15), command=button_sub)
btn_sub.grid(column=3, row=1, padx=5, pady=5)
btn_add = tk.Button(down_frame, text='+', padx=15, pady=10,
                    font=("Courier", 15), command=button_add)
btn_add.grid(column=3, row=2, padx=5, pady=5)
btn_div = tk.Button(down_frame, text='/', padx=15, pady=10,
                    font=("Courier", 15), command=button_div)
btn_div.grid(column=3, row=3, padx=5, pady=5)
btn_c = tk.Button(down_frame, text='C', padx=15, pady=10,
                  font=("Courier", 15), command=button_clear)
btn_c.grid(column=2, row=4, padx=5, pady=5)

btn_res = tk.Button(down_frame, text='=', padx=15, pady=10,
                    font=("Courier", 15), command=button_equal)
btn_res.grid(column=3, row=4, padx=5, pady=5)

btn3 = tk.Button(root, text='9')

root.mainloop()
