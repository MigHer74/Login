from ttkbootstrap import Window


class Login(Window):
    def __init__(self):
        super().__init__(title="Login")


if __name__ == ("__main__"):
    app = Login()
    app.mainloop()
