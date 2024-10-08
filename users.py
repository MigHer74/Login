from ttkbootstrap import Toplevel


class UsersWindow(Toplevel):
    def __init__(self):
        super().__init__(title="Users Information", resizable=(False, False))
