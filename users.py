from ttkbootstrap import Toplevel, Frame, Label, Entry, Button, Treeview
from ttkbootstrap import Scrollbar
from ttkbootstrap.dialogs.dialogs import Messagebox
import bcrypt
import dba as db


class UsersWindow(Toplevel):
    def __init__(self):
        super().__init__(title="Users Information", resizable=(False, False))

        # Build User Info Window
        self.build_user()

        # Center User Window on the screen.
        self.position_center()

        # Load User Info
        self.load_info()

        self.grab_set()
        self.transient()
        self.focus()

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
        self.tblUser.column(3, width=160)

        self.tblUser.pack(side="left")

        # ScrollBar
        self.sbrUser = Scrollbar(self.tblFrame, orient="vertical",
                                 bootstyle="info-round")
        self.sbrUser.pack(side="right", fill="y")
        self.tblUser.config(yscrollcommand=self.sbrUser.set)
        self.sbrUser.config(command=self.tblUser.yview)

        self.tblUser.bind("<Double-Button-1>", self.select_modify)
        self.tblUser.bind("<<TreeviewSelect>>", self.select_delete)

        # Buttons Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=1, column=1, padx=(15, 15), pady=(20, 20))

        self.btnNew = Button(self.btnFrame, width=15, text="New",
                             command=self.new_user, bootstyle="success")
        self.btnNew.pack(pady=(0, 20))

        self.btnSave = Button(self.btnFrame, width=15, text="Save",
                              command=self.save_user, state="disabled",
                              bootstyle="success")
        self.btnSave.pack(pady=(0, 20))

        self.btnCancel = Button(self.btnFrame, width=15, text="Cancel",
                                command=self.cancel_user, state="disabled",
                                bootstyle="warning")
        self.btnCancel.pack(pady=(0, 20))

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete",
                                command=self.delete_user, state="disabled",
                                bootstyle="warning")
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

    def select_delete(self, event):
        self.keyUser = self.tblUser.item(self.tblUser.focus(), "text")

        if self.keyUser != "":
            self.btnDelete.config(state="normal")

    def select_modify(self, event):
        self.keyUser = self.tblUser.item(self.tblUser.focus(), "text")

        if self.keyUser != "":
            self.btnAction = 2
            self.modify_user()

    def new_user(self):
        self.enable_entries()

        self.btnAction = 1

        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")
        self.btnNew.config(state="disabled")
        self.btnDelete.config(state="disabled")

        self.entId.focus()

    def save_user(self):
        if self.btnAction == 1:
            password_hashed = bcrypt.hashpw(
                self.entPassword.get().encode('utf-8'), bcrypt.gensalt())
            password_storage = password_hashed.decode('utf-8')

            db.save_info(self.entId.get(), self.entName.get(),
                         password_storage)
        else:
            db.modify_info(self.entId.get(), self.entName.get(),
                           self.entPassword.get())

        self.tblFrame.focus()
        self.load_info()
        self.cancel_user()

        self.btnAction = 0

    def modify_user(self):
        modifyUser = db.retrieve_one_info(self.keyUser)

        self.enable_entries()

        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")

        self.entId.insert(0, modifyUser[0])
        self.entName.insert(0, modifyUser[1])
        self.entPassword.insert(0, modifyUser[2])

        self.entId.config(state="disabled")
        self.btnNew.config(state="disabled")
        self.btnDelete.config(state="disabled")

        self.entName.focus()

    def cancel_user(self):
        self.enable_entries()
        self.clear_entries()
        self.disable_entries()

        self.btnSave.config(state="disabled")
        self.btnCancel.config(state="disabled")
        self.btnNew.config(state="normal")
        self.btnDelete.config(state="disabled")

    def delete_user(self):
        deleteUser = db.retrieve_one_info(self.keyUser)

        messageUSer = f"Do you want to delete {deleteUser[1]} user info ?."

        answer_user = Messagebox.show_question(message=messageUSer,
                                               title="Delete User", alert=True,
                                               buttons=['Yes:success',
                                                        'No:outline-danger'],
                                               parent=self)

        if answer_user != "No":
            db.delete_one_info(self.keyUser)
            self.load_info()
        else:
            self.btnDelete.config(state="disabled")

    def enable_entries(self):
        self.entId.config(state="normal", bootstyle="success")
        self.entName.config(state="normal", bootstyle="success")
        self.entPassword.config(state="normal", bootstyle="success")

    def disable_entries(self):
        self.entId.config(state="disabled", bootstyle="default")
        self.entName.config(state="disabled", bootstyle="default")
        self.entPassword.config(state="disabled", bootstyle="default")

    def clear_entries(self):
        self.entId.delete(0, "end")
        self.entName.delete(0, "end")
        self.entPassword.delete(0, "end")
