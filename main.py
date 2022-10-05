import tkinter as tk

wnd = tk.Tk()

wnd.title("Давай потеревенимо")
wnd.geometry("600x300")
wnd.resizable(False, False)

greeting_txt = "Привіт! Я няшний Бот-говорун. А як тебе звуть?"

main_txt = tk.Label(wnd, text=greeting_txt, font=("Courier", 14), justify="left")
main_txt.place(x=10, y=20)

user_input = tk.Entry(wnd, width=80)
user_input.place(x=10, y=150)


def name_handler():
    user_name = user_input.get()
    user_input.delete(0, "end")
    main_txt.configure(text=f"{user_name.strip().lower().capitalize()}, радий знайомству!\n"
                            f"Давай потеревенимо про все на світі.\nІ про це ніхто не дізнається. Почнемо?")
    btn_1.destroy()
    user_input.destroy()

    choices = ["так", "ні"]
    selected = tk.StringVar()
    for choice in choices:
        btn_2 = tk.Radiobutton(text=choice, value=choice, variable=selected)
        btn_2.pack()   # ????????????????????????????????????????????????????????????


btn_1 = tk.Button(wnd, text="send name", command=name_handler, relief=tk.RAISED)
btn_1.place(x=10, y=180)


def start_talk():
    btn = tk.Button(wnd, text="send", command=start_talk, relief=tk.RAISED)
    if str(user_input).strip().lower() == "почнемо":
        user_input.delete(0, "end")
        main_txt.configure(text="Як думаєш, що тобі варто зараз зробити в першу чергу?")
    elif str(user_input).strip().lower() == "не будемо починати":
        user_input.delete(0, "end")
        main_txt.configure(text="Хмм, у когось настрій не до бесід.\n"
                                "Я знаю що тобі зараз дуже потрібне. Цікаво?"
                                "(підказка: введи 'так' або 'ні')")
    else:
        user_input.delete(0, "end")
        main_txt.configure(text="Ой лишенько. Не таку відповідь я очікував. Спробуй ще раз.\n"
                                "(підказка: введи 'так' або 'ні')")


if __name__ == "__main__":
    wnd.mainloop()
