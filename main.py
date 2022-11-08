from tkinter import *
from MorseCode import MORSE_CODE



def encrypt():
    message = text_entry.get().upper()
    msg = ""
    for letter in message:
        if letter != " ":
            msg += MORSE_CODE[letter] + " "
        else:
            msg += " "
    print(msg)
    result_text.config(text = f"{msg}")


def decrypt():
    message = text_entry2.get()
    message += ' '

    result = ''
    text = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            text += letter

        else:

            i += 1
            if i == 2:
                result += ' '
            else:

                result += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(text)]
                text = ''

    result_text2.config(text = f"{result}")

def reset():
    text_entry.delete(0, END)
    result_text.config(text = " ")

def reset2():
    text_entry2.delete(0, END)
    result_text2.config(text=" ")

window = Tk()
window.title("Morse Code Translator")
window.config(padx= 25, pady =25)


title_label=Label(text="Morse Code Translator", font = ("Ariel", 40, "bold"))
title_label.grid(column = 0, row = 0, columnspan = 2)

text_label= Label(text = "Insert your text:", font = ("Ariel", 20))
text_label.grid(column = 0, row = 1, padx=25, pady=25, columnspan = 2)

text_entry= Entry(width = 100)
text_entry.grid(column = 0, row = 2, padx=25, pady=25, columnspan = 2)

translate = Button(text = "Translate", font = 20, width=15, command = encrypt)
translate.grid(column = 0, row = 3, columnspan = 2)

result = Label(text = "Result:", font = ("Ariel", 20))
result.grid(column = 0, row = 4, padx=25, pady=25)

result_text = Label(text = "", font = ("Ariel", 20))
result_text.grid(column = 1, row = 4, padx=25, pady=25)

reset = Button(text = "Reset", font = 20, width=15, command = reset)
reset.grid(column =0,  row = 5, columnspan = 2)

text_label2= Label(text = "Insert your morse code:", font = ("Ariel", 20))
text_label2.grid(column = 0, row = 6, padx=25, pady=25, columnspan = 2)

text_entry2= Entry(width = 100)
text_entry2.grid(column = 0, row = 7, padx=25, pady=25, columnspan = 2)

translate2 = Button(text = "Translate", font = 20, width=15, command = decrypt)
translate2.grid(column = 0, row = 8, columnspan = 2)

result2 = Label(text = "Result:", font = ("Ariel", 20))
result2.grid(column = 0, row = 9, padx=25, pady=25)

result_text2 = Label(text = "", font = ("Ariel", 20))
result_text2.grid(column = 1, row = 9, padx=25, pady=25)

reset2 = Button(text = "Reset", font = 20, width=15, command = reset2)
reset2.grid(column =0,  row = 10)

exit_button = Button(text = "Close", font = 20, width=15, command = window.destroy)
exit_button.grid(column = 1, row = 10)

window.mainloop()