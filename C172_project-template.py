from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")
root.config(background="#004777")

label_name = Label(root, foreground="#FF7700", bg="#004777", font=("Comic Sans MS", "15", "bold"), text="User Name : ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root, bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"),)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, foreground="#FF7700", bg="#004777", font=("Comic Sans MS", "15", "bold"), text="Email id : ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root,  bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"),)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root, foreground="#FF7700", bg="#004777", font=("Comic Sans MS", "15", "bold"), wraplength=400)

dictionary = {}
class Users: 
        
    def addUser(key, value): 
        global dictionary
        dictionary[key] = value
        label['text'] = dictionary
         #access the dictionary variable inside the class
         #pass parameter key as the index to the dictionary and inside it assign the parameter as value.
         #update the text parameter of the label with variable dictionary.
        

class GetUsers(Users): 
        
    def getUser(self):
        username = entry_name.get()
        email = entry_email.get()
        Users.addUser(username, email)
        #using get() function get the entry_name from the user and store it in variable username
        #using the get() function get the email_id from the user and store it in variable email_id
        #access the addUser function of the users class and inside it pass the parameters as username, email_id

#Create a object of GetUsers class        
user = GetUsers()
btn = Button(root, text="Add user details", bg="#CC0000", foreground="#FF7700", font=("Comic Sans MS", "12", "normal"), command=user.getUser)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()