import tkinter
from tkinter import *
from Writer import writer

class StartUp(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.windowO()
        self.epubCounter = 1

    def windowO(self):

        self.master.title("Scraper General")
        self.pack(fill=BOTH, expand=1)

        webSerialButton = Button(self, text="Convert Web Serial to EPUB", command=self.OpenEPUBConverter, width= 30)
        webSerialButton.place(x=90, y=50)

    def OpenEPUBConverter(self):
        if (self.epubCounter % 2 == 1):
            self.converterTxt = Label(self, text="Type in the necessary details to convert this Site to an EPUB!")
            self.converterTxt.place(x=0,y=75)


            self.link = Label(self, text="Link to table of Contents:")
            self.link.place(x=0,y=100)

            self.linkI = Entry(self)
            self.linkI.place(x=140,y=100)

            self.author = Label(self, text="Author:")
            self.author.place(x=0,y=125)

            self.authorI = Entry(self)
            self.authorI.place(x=140,y=125)

            self.pgCnt = Label(self, text="Page Count:")
            self.pgCnt.place(x=0, y=150)

            self.pgCntI = Entry(self)
            self.pgCntI.place(x=140, y=150)

            self.locationF = Label(self, text="File Location:")
            self.locationF.place(x=0, y=175)

            self.locationFI = Entry(self)
            self.locationFI.place(x=140, y=175)

            self.title = Label(self, text="Title:")
            self.title.place(x=0, y=200)

            self.titleI = Entry(self)
            self.titleI.place(x=140, y=200)

            self.formSubmit = Button(self, text="Submit form", command=self.FormSubmit)
            self.formSubmit.place(x=0, y=225)

            self.epubCounter += 1
        else:
            self.converterTxt.destroy()
            self.link.destroy()
            self.linkI.destroy()
            self.author.destroy()
            self.authorI.destroy()
            self.pgCnt.destroy()
            self.pgCntI.destroy()
            self.locationF.destroy()
            self.locationFI.destroy()
            self.title.destroy()
            self.titleI.destroy()
            self.formSubmit.destroy()
            self.epubCounter += 1

    def FormSubmit(self):

        link = self.linkI.get()
        author = self.authorI.get()
        pgCnt = self.pgCntI.get()
        locationF = self.locationFI.get()
        title = self.titleI.get()

        self.linkI.delete(0,END)
        self.authorI.delete(0,END)
        self.pgCntI.delete(0,END)
        self.locationFI.delete(0,END)
        self.titleI.delete(0,END)

        writer(link, author, int(pgCnt), locationF, title)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")
    app = StartUp(root)

    root.mainloop()

