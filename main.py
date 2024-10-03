from ttkbootstrap import Window, Frame, Label


class Login(Window):
    def __init__(self):
        super().__init__(title="Login", resizable=(False, False))

        # Label Frame
        self.lblFrame = Frame(self)
        self.lblFrame.grid(row=0, column=0)

        Label(self.lblFrame, text="Login",
              font=("Arial", "20", "bold")).pack()


if __name__ == ("__main__"):
    app = Login()
    app.mainloop()
