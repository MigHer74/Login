from ttkbootstrap import Window, Frame, Label, Entry, Button
import tools as tls


class Login(Window):
    def __init__(self):
        super().__init__(title="Login", resizable=(False, False))

        # Label Frame
        self.lblFrame = Frame(self)
        self.lblFrame.pack()

        self.prueba1 = Label(self.lblFrame, text="Login",
                             font=("Arial", "20", "bold"))
        self.prueba1.pack()

        # Label Image
        self.imgFront = tls.imageItem("login.png", 250, 250)

        self.imgFrame = Frame(self)
        self.imgFrame.pack()

        self.prueba = Label(self.imgFrame, image=self.imgFront)
        self.prueba.pack()

        # Entry Frames
        self.entFrame = Frame(self)
        self.entFrame.pack()

        self.lblUser = Label(self.entFrame, text="User :")
        self.lblUser.grid(row=0, column=0)

        self.lblPass = Label(self.entFrame, text="Password :")
        self.lblPass.grid(row=1, column=0)

        self.entUser = Entry(self.entFrame, width=20)
        self.entUser.grid(row=0, column=1)

        self.entPass = Entry(self.entFrame, width=20, show="*")
        self.entPass.grid(row=1, column=1)

        # Button Frames
        self.btnFrame = Frame(self)
        self.btnFrame.pack()

        self.btnEnter = Button(self.btnFrame, width=15, text="Enter")
        self.btnEnter.grid(row=0, column=0)

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               command=self.destroy)
        self.btnClose.grid(row=1, column=0)


if __name__ == "__main__":
    app = Login()
    app.mainloop()
