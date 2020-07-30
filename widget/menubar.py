



from tkinter import *






class Menubar():


    def __init__(self,window:Tk):
        super().__init__()

        self.menubar = Menu(window)
        self.menu:list = []

        window.config(menu=self.menubar)


    def __getitem__(self, index) -> Menu:
        return self.menu[index]

    def get_menu(self,index) -> Menu:
        return self[index]



    def add_menu(self,text:str) -> int:
        "返回菜单索引"

        new_menu = Menu(self.menubar)
        self.menu.append(new_menu)
        self.menubar.add_cascade(Label = text,menu = new_menu); # 给菜单加菜单
        return len(self.menu) - 1
        

    @staticmethod
    def menu_add_submenu(root_menu:Menu,text:str) -> Menu:
        "返回添加的菜单"

        submenu = Menu(root_menu)
        root_menu.add_cascade(Label = text,menu = submenu)
        return submenu



    def menu_add_menu(self,menu_index:int,text:str) -> Menu:
        "返回添加的菜单"

        root:Menu = self[menu_index]
        submenu = Menu(root)
        root.add_cascade(Label = text,menu = submenu)
        return submenu


    def menu_add_item(self,menu_index:int,text:str,func:function):
        self.get_menu(menu_index).add_command(Label=text,command=func) # 给菜单加项


    def menu_add_separator(self,menu_index:int):
        self.get_menu(menu_index).add_separator()
    




class FlyMenubar():

    def __init__(self,window:Tk):
        super().__init__()

        self.menubar = Menu(window)
        self.menu = {}

        window.config(menu=self.menubar)

    
    def __getitem__(self, index) -> Menu:
        "返回一级菜单"
        return self.menu.keys()[index]

    def get_menu(self,index) -> Menu:
        "返回一级菜单"
        return self[index]

    
    def add_menu(self,text:str) -> int:
        "添加一级菜单,返回菜单索引"

        new_menu = Menu(self.menubar)
        self.menu[new_menu] = {}
        self.menubar.add_cascade(Label = text,menu = new_menu); # 给菜单加菜单
        return len(self.menu) - 1
        

    def menu_add_submenu(self,text:str,*menu_index) -> int:
        "返回添加的菜单索引"

        if len(menu_index) > 0:
            prev_menus:dict = self.menu
            prev_menu:Menu = None

            for index in menu_index:
                prev_menu = prev_menus.keys()[index]; # 通过索引获取其key
                prev_menus = prev_menus[prev_menu]; # 通过其key获取其value
                
                if prev_menu == None or prev_menus == None:
                    return -1

            submenu = Menu(prev_menu)
            prev_menus[submenu] = {}
            prev_menu.add_cascade(Label = text,menu = submenu)

            return len(prev_menus) - 1
        else:
            return -1



    def menu_add_menu(self,menu_index:int,text:str) -> int:
        "添加二级菜单，返回添加的菜单索引"

        root:Menu = self[menu_index]
        submenu = Menu(root)
        self.menu[root][submenu] = {}
        root.add_cascade(Label = text,menu = submenu)
        return len(self.menu[root]) - 1


    def menu_add_item(self,menu_index:int,text:str,func:function):
        "给一级菜单添加项"

        self.get_menu(menu_index).add_command(Label=text,command=func) # 给菜单加项


    def menu_add_separator(self,menu_index:int):
        "给一级菜单添加分割线"

        self.get_menu(menu_index).add_separator()

    