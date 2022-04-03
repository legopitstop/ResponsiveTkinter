"""Make your tkinter widgets responsive"""
from tkinter import Tk, Widget

# https://www.w3schools.com/html/html_responsive.asp
class Responsive():
    class _add():
        def __init__(self,master:Tk, value:int, mode='<', orient='horizontal'):
            self.master = master

            self.value = value
            self.orient = orient
            self.mode = mode
            self.children = []

        def _resize(self):
            # get size
            if self.orient=='horizontal':
                size = self.master.winfo_width()
            elif self.orient=='vertical':
                size = self.master.winfo_height()
            else:
                print('Invalid orient')

            # TEMP
            self.master.title('Window Title %sx%s'%( str(self.master.winfo_width()), str(self.master.winfo_height()) ))

            # Update size
            if self.mode =='<':
                if self.value <= size:
                    for w in self.children:
                        self._update(w, 'update')
                else:
                    for w in self.children:
                        self._update(w, 'default')

            elif self.mode =='>':
                if self.value >= size:
                    for w in self.children:
                        self._update(w, 'update')
                else:
                    for w in self.children:
                        self._update(w, 'default')

        def _get_geo_type(self,widget:Widget):
            """internal function"""
            try:
                w = widget.grid_info()
                if w!={}: return 'grid'
            except: pass

            try:
                w = widget.pack_info()
                if w!={}: return 'pack'
            except: pass

            try:
                w = widget.place_info()
                if w!={}: return 'place'
            except: pass
        
        def _update(self, widget, options):
                """internal function"""
                w:Widget = widget['widget']
                if widget['type'] == 'grid':
                    w.grid(**widget[options])

                elif widget['type'] == 'pack':
                    w.pack(**widget[options])
                        
                elif widget['type'] == 'place':
                    w.place(**widget[options])

                elif widget['type'] == 'destroy':

                    if widget['geo'] == 'grid':
                        if options=='update': w.grid_forget()
                        else: w.grid(**widget[options])

                    elif widget['geo'] == 'pack':
                        if options=='update': w.pack_forget()
                        else: w.pack(**widget[options])

                    elif widget['geo'] == 'place':
                        if options=='update': w.place_forget()
                        else: w.place(**widget[options])

        def grid(self,widget:Widget,**kw):
            """
            Modify the grid geometry

            Attributes
            ---
            `master` - The widget to update the grid.

            `kw` - The grid properties to apply.
            """
            self.children.append({'type':'grid', 'widget': widget, 'default': widget.grid_info(), 'update':kw})

        def destroy(self,widget:Widget):
            """Remove the widget"""
            geo = self._get_geo_type(widget)
            self.children.append({'type':'destroy', 'geo': geo, 'widget': widget, 'default': widget.grid_info(), 'update': True})

        def place(self,widget:Widget,**kw):
            """
            Modify the place geometry

            Attributes
            ---
            `master` - The widget to update the grid.

            `kw` - The grid properties to apply.
            """
            self.children.append({'type':'place', 'widget': widget, 'default': widget.place_info(), 'update':kw})

        def pack(self,widget:Widget,**kw):
            """
            Modify the pack geometry

            Attributes
            ---
            `master` - The widget to update the grid.

            `kw` - The grid properties to apply.
            """
            self.children.append({'type':'pack', 'widget': widget, 'default': widget.pack_info(), 'update':kw})

    def __init__(self, master:Tk):
        """
        Modify your widget depending on the max size of the parent

        Attributes
        ---
        `master` - The root window to bind to.
        
        """
        self.master = master
        self.groups=[]
        master.bind('<Configure>', self._resize)

    def _resize(self,e):
        """Internal Function"""
        # self.groups._resize()
        for group in self.groups:
            group._resize()

    def add_group(self, value:int, mode='<', orient='horizontal'):
        """
        Create a new group of widgets
        
        Attributes
        ---
        `value` - The size value to match

        `mode` - The size mode. only `>` or `<`. default: `<`
        
        `orient` - The orentation to monitor. only `horizontal` or `vertical` default: horizontal
        
        """
        
        master = self.master
        group = self._add(master,value, mode, orient)
        self.groups.append(group)
        return group

def example():
    from tkinter import Frame, Tk
    root=Tk()
    root.title('Window Title')
    # root.minsize(356,346)
    root.geometry('902x900')

    # resize the window to see that the three Frames below will be adjusted or removed
    left = Frame(root,width=300,height=300,bg='blue')
    left.grid(row=0,column=0)
    main = Frame(root,width=300,height=300,bg='gray')
    main.grid(row=0,column=1)
    right = Frame(root,width=300,height=300,bg='green')
    right.grid(row=0,column=2)

    R = Responsive(root) # Initilize Responsive `root`
    nine = R.add_group(900,'>')
    nine.destroy(main)

    six = R.add_group(600,'>')
    six.grid(right,row=1,column=0)

    root.mainloop()

if __name__ == '__main__':
    example()