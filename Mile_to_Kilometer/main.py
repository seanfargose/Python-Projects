from tkinter import *

def miles_to_Kilometers():
    miles = float(miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilometer converter!!")
window.config(padx=20,pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="Is Equal To")
is_equal_to.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command=miles_to_Kilometers)
calculate_button.grid(column=1, row=2)




window.mainloop()