import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())

    bmi = weight / (height ** 2)

    result_label.config(text = "Your BMI is: {:.2f}".format(bmi))

    if bmi < 18.5:
        result_label.config(fg = "blue")
        result_label.config(text = result_label.cget("text") + "\nYou are underweight.")
    elif 18.5 <= bmi < 25:
        result_label.config(fg = "green")
        result_label.config(text = result_label.cget("text") + "\nYou are at a healthy weight.")
    elif 25 <= bmi < 30:
        result_label.config(fg = "orange")
        result_label.config(text = result_label.cget("text") + "\nYou are overweight.")
    else:
        result_label.config(fg = "red")
        result_label.config(text = result_label.cget("text") + "\nYou are obese.")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text = "Enter your weight in kilograms: ")
weight_label.grid(row = 0, column = 0)

weight_entry = tk.Entry(root)
weight_entry.grid(row = 0, column = 1)

height_label = tk.Label(root, text = "Enter your height in meters: ")
height_label.grid(row = 1, column = 0)

height_entry = tk.Entry(root)
height_entry.grid(row = 1, column = 1)

calculate_button = tk.Button(root, text = "Calculate BMI", command = calculate_bmi)
calculate_button.grid(row = 2, column = 0, columnspan = 2)

result_label = tk.Label(root)
result_label.grid(row = 3, column = 0, columnspan = 2)

root.mainloop()
