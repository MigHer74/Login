from ttkbootstrap import Toplevel, Frame, Label, Entry, Button, Treeview
import dba as db


class UsersWindow(Toplevel):
    def __init__(self):
        super().__init__(title="Users Information", resizable=(False, False))

        # Build User Info Window
        self.build_user()

        # Load User Info
        self.load_info()

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

        self.tblUser.column(1, width=50)
        self.tblUser.column(2, width=175)
        self.tblUser.column(3, width=175)

        self.tblUser.pack()

        # Buttons Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=1, column=1, padx=(15, 15), pady=(20, 20))

        self.btnNew = Button(self.btnFrame, width=15, text="New",
                             command=self.new_user, bootstyle="success")
        self.btnNew.pack(pady=(0, 20))

        self.btnSave = Button(self.btnFrame, width=15, text="Save",
                              state="disabled", bootstyle="success")
        self.btnSave.pack(pady=(0, 20))

        self.btnCancel = Button(self.btnFrame, width=15, text="Cancel",
                                state="disabled", bootstyle="warning")
        self.btnCancel.pack(pady=(0, 20))

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete",
                                state="disabled", bootstyle="warning")
        self.btnDelete.pack(pady=(0, 20))

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               command=self.destroy,
                               bootstyle="outline-danger")
        self.btnClose.pack()

    def load_info(self):
        data_user = db.retrieve_info("l")

        self.tblUser.delete(*self.tblUser.get_children())

        for item in data_user:
            self.tblUser.insert("", index="end", text=item[0],
                                values=[item[0], item[1], item[2]])

    def new_user(self):
        self.entId.config(state="normal", bootstyle="info")
        self.entName.config(state="normal", bootstyle="info")
        self.entPassword.config(state="normal", bootstyle="info")

        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")
        self.btnNew.config(state="disabled")

        self.entId.focus()