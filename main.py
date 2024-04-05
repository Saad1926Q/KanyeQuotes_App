from tkinter import *
import requests

#------------------------------FUNCTIONALITY----------------------------------#



def quote_refresh():
    new_response=requests.get("https://api.kanye.rest")
    while len(new_response.json()["quote"])>100:
        new_response = requests.get("https://api.kanye.rest")
    canvas.itemconfig(quote_text,text=f"{new_response.json()['quote']}")

#----------------------------------UI FOR THE APP------------------------------#
window=Tk()
window.title("Kanye Quotes App")
window.config(padx=100,pady=50)

canvas=Canvas(width=300,height=414)
background_img=PhotoImage(file="background.png")
canvas.create_image(150,207,image=background_img)
quote_text=canvas.create_text(150,207,text="",fill="black",width=250,font=("Arial", 30, "bold"))
canvas.grid(column=0,row=0,columnspan=3,pady=10)
kanye_img=PhotoImage(file="kanye.png")
kanye_button=Button(image=kanye_img,relief=GROOVE,command=quote_refresh)
kanye_button.grid(row=1,column=1)

response=requests.get("https://api.kanye.rest")
canvas.itemconfig(quote_text,text=f"{response.json()['quote']}")


window.mainloop()