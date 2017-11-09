import tkinter
import tkinter.filedialog as dialog

class OpenFile:
    def __init__(self, parent):

        self.parent = parent

        self.text = tkinter.Text(self.parent)
        self.text.pack()

        self.menubar = tkinter.Menu(self.parent)
        self.filemenu = tkinter.Menu(self.menubar)
        self.filemenu.add_command(label='Save',
                                  command=lambda: self.save(self.parent,
                                                            self.text))
        self.filemenu.add_command(label='Quit',
                                  command=lambda: self.quit(self.parent))

        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.parent.config(menu=self.menubar)

    def save(self, root, text):
        self.data = text.get('0.0', tkinter.END)
        self.filename = dialog.asksaveasfilename(
            parent=root,
            filetypes=[('Text', '*.txt')],
            title='Save as...')

        self.writer = open(self.filename, 'w')
        self.writer.write(self.data)
        self.writer.close()

    def quit(self, root):
        root.destroy()


window = tkinter.Tk()

openfile = OpenFile(window)

window.mainloop()