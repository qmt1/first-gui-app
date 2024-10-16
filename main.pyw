from config.config import *

# MY FIRST GUI APPLICATION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! .qmt <3

click = 0
pi = None  
pa45 = None  

def event():
    global click, pi, pa45
    click += 1
    txt.configure(text=f"{click}",font=("Arial", 20))
    
    if click == 5:
        xt.configure(text="GG YOU HAVE 5 CLICKS")
    elif click == 6:
        xt.configure(text="")
    elif click == 20:
        xt.configure(text="GG YOU HAVE 20 CLICKS")
    elif click == 21:
        xt.configure(text="")
    elif click == 45:
        xt.configure(text="GNGNGNGNGNGNN TRYHARD")
    elif click == 46:
        xt.configure(text="")
    elif click == 70:
        xt.configure(text="UwU itadakimas")
    elif click == 72: 
        xt.configure(text="")

# START
# variable app dans /config/config.py
app.geometry("900x720")

# TEXT DE BASE 
txt = customtkinter.CTkLabel(app, text="")  
txt.pack(expand=True)

# TEXT GG 
xt = customtkinter.CTkLabel(app, text_color="red", text="",font=("Arial", 30))  
xt.place(x=310,y=310)


# BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON BOUTON 
button = customtkinter.CTkButton(app, text="Click", command=event)
button.place(x=380,y=389)

app.mainloop()