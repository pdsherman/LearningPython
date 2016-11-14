"""
Example 9-11 from "Programming Python"
Add common edit tools to ScrolledText by inheritance
"""
#Required to import quitter module correctly
import sys
sys.path.append("/home/psherman/GitRepos/LearningPython/GUI/part1/")

from Tkinter        import *
from tkFileDialog   import asksaveasfilename
from tkSimpleDialog import askstring
from quitter        import Quitter
from scrolledText   import ScrolledText

class SimpleEditor(ScrolledText):
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)

        Button(frm, text='Save',  command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut',   command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find',  command=self.onFind).pack(side=LEFT)
        
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 9, 'normal'))

    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()
            open(filename, 'w').write(alltext)

    def onCut(self):
        try:
            text = self.text.get(SEL_FIRST, SEL_LAST)
            self.text.delete(SEL_FIRST, SEL_LAST)
            self.clipboard_clear()
            self.clipboard_append(text)
        except:
            print("Error with cut")

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END)
            if where:
                print(where)
                pastit = where + ('+%dc'% len(target))
                #self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()
    else:
        SimpleEditor().mainloop()
