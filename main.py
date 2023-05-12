import tkinter as tk

bg_color = "#404258"
# #474E68
# #50577A
# #6B728E

app = tk.Tk()
app.title("Macro Panda")
app.geometry("1024x576")
app.config(background=bg_color)

header = tk.Label(text="Macro Panda",
                  font=("Times", 30),
                  background=bg_color,
                  foreground="white").pack(pady=(10, 0))

app.mainloop()
