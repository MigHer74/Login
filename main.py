from ttkbootstrap import Window, Frame, Label
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


if __name__ == ("__main__"):
    app = Login()
    app.mainloop()
