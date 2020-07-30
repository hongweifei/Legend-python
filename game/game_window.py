



from tkinter import *
from widget.menubar import *


class GameWindow(Tk):


    def __init__(self, screenName = None, baseName = None, className = 'Tk', useTk = 1, sync = 0, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use);

        self.menubar:FlyMenubar = FlyMenubar(self);
        self.menubar.add_menu("游戏");

        menu_index = [];
        for i in range(25):
            menu_index.append(0);
            self.menubar.add_submenu(str(i + 1),tuple(menu_index));
        

        self.mainloop();
        


    	













