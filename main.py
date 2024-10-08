from ttkbootstrap import Window, Frame, Label, Entry, Button, Combobox
from users import UsersWindow
import tools as tls
import dba as db


class LoginApp(Window):
    def __init__(self):
        super().__init__(title="Login", resizable=(False, False),
                         themename="darkly")

        # Load User ID and Name
        self.load_users()

        # Build Main Window
        self.build_login()

        if self.user_list_final != "":
            self.entUser.config(state="readonly")

    def build_login(self):
        # Label Frame
        self.lblFrame = Frame(self)
        self.lblFrame.grid(row=0, column=0, columnspan=2,
                           padx=(15, 15), pady=(15, 0))

        self.lblTitle = Label(self.lblFrame, text="Login",
                              font=("Arial", "20", "bold"),
                              bootstyle="info")
        self.lblTitle.pack()

        # Label Image
        self.imgFront = tls.imageItem("login.png", 250, 250)

        self.imgFrame = Frame(self)
        self.imgFrame.grid(row=1, column=0, rowspan=2,
                           padx=(15, 15), pady=(15, 15))

        self.lblimg = Label(self.imgFrame, image=self.imgFront)
        self.lblimg.pack()

        # Entry Frames
        self.entFrame = Frame(self, relief="raised")
        self.entFrame.grid(row=1, column=1, padx=(15, 20), pady=(15, 0))

        self.lblUser = Label(self.entFrame, text="User :")
        self.lblUser.grid(row=0, column=0, padx=(15, 15), pady=(15, 0),
                          sticky="w")

        self.lblPass = Label(self.entFrame, text="Password :")
        self.lblPass.grid(row=1, column=0, padx=(15, 15), pady=(15, 15))

        # self.entUser = Entry(self.entFrame, width=20)
        # self.entUser.grid(row=0, column=1, padx=(15, 15), pady=(15, 0))

        self.entUser = Combobox(self.entFrame, width=18,
                                values=self.user_list_final, state="disable")
        self.entUser.grid(row=0, column=1, padx=(15, 15), pady=(15, 0))

        self.entPass = Entry(self.entFrame, width=20, show="*")
        self.entPass.grid(row=1, column=1, padx=(15, 15), pady=(15, 15))

        # Button Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=2, column=1, padx=(15, 20), pady=(15, 0))

        self.btnEnter = Button(self.btnFrame, width=15, text="Enter",
                               bootstyle="success")
        self.btnEnter.grid(row=0, column=0, padx=(15, 15))

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               command=self.destroy,
                               bootstyle="danger-outline")
        self.btnClose.grid(row=0, column=1, padx=(15, 15))

        # Add User Frame
        self.userFrame = Frame(self)
        self.userFrame.grid(row=3, column=1, padx=(0, 20), pady=(15, 15),
                            sticky="e")

        self.imgAdd = tls.imageItem("add_user.png", 15, 15)

        self.btnAdd = Button(self.userFrame, image=self.imgAdd,
                             command=lambda: UsersWindow())
        self.btnAdd.pack(padx=(0, 15))

    def load_users(self):
        user_list = []
        self.user_list_final = []

        user_list = db.retrieve_info()

        for user in user_list:
            user_temp = f"{user[0]} | {user[1]}"
            self.user_list_final.append(user_temp)


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
