from ttkbootstrap import Toplevel, Frame, Label, Entry, Button, Treeview


class UsersWindow(Toplevel):
    def __init__(self):
        super().__init__(title="Users Information", resizable=(False, False))

        # Build User Info Window
        self.build_user()

    def build_user(self):
        # Entry Frame
        self.infoUser = Frame(self)
        self.infoUser.grid(row=0, column=0, columnspan=2)

        self.lblId = Label(self.infoUser, text="Id")
        self.lblId.grid(row=0, column=0, padx=(15, 0), pady=(15, 0))

        self.entId = Entry(self.infoUser, width=10, state="disabled")
        self.entId.grid(row=1, column=0, padx=(15, 0), pady=(3, 0))

        self.lblName = Label(self.infoUser, text="Name")
        self.lblName.grid(row=0, column=1, padx=(15, 0), pady=(15, 0))

        self.entName = Entry(self.infoUser, width=50, state="disabled")
        self.entName.grid(row=1, column=1, padx=(15, 0), pady=(3, 0))

        self.lblPassword = Label(self.infoUser, text="Password")
        self.lblPassword.grid(row=0, column=2, padx=(15, 15), pady=(15, 0))

        self.entPassword = Entry(self.infoUser, width=30, state="disabled")
        self.entPassword.grid(row=1, column=2, padx=(15, 15), pady=(3, 0))

        # Table Frame
        self.tblFrame = Frame(self)
        self.tblFrame.grid(row=1, column=0, padx=(15, 0), pady=(20, 20),
                           sticky="w")

        self.tblUser = Treeview(self.tblFrame, columns=(1, 2, 3),
                                show="headings", height=15,
                                selectmode="browse", bootstyle="info")

        self.tblUser.heading(1, text="Id")
        self.tblUser.heading(2, text="Name")
        self.tblUser.heading(3, text="Password")

        self.tblUser.column(1, width=50, anchor="center")
        self.tblUser.column(2, width=150)
        self.tblUser.column(3, width=150)

        self.tblUser.pack()

        # Buttons Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=1, column=1, padx=(15, 15), pady=(20, 20))

        self.btnAdd = Button(self.btnFrame, width=15, text="New User",
                             bootstyle="success")
        self.btnAdd.pack(pady=(0, 20))

        self.btnModify = Button(self.btnFrame, width=15, text="Modify User",
                                state="disabled", bootstyle="success")
        self.btnModify.pack(pady=(0, 20))

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete User",
                                state="disabled", bootstyle="warning")
        self.btnDelete.pack(pady=(0, 20))

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               bootstyle="outline-danger")
        self.btnClose.pack()
