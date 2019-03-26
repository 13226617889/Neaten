from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import os
from Desktop_finishing import Neaten

#添加文件名
"""

  # 增加背景图片
        photo = PhotoImage(file="timg.png")
        theLabel = Label(self.windows,justify=LEFT, image=photo, compound=CENTER, font=("华文行楷", 20),
                         fg="white")
        self.Path()
        theLabel.grid()
"""
special = ['\\','/','*','?','<',">",'|']# 进制修改的名字，有包含该列表内的字符
# 勾选中的参数，生成新的列表，传入函数执行
# 测试异常，并写异常处理
class Gui:
    def __init__(self,Name = '整理文件夹'):
        self.NAME = Name
        self.List = []
        self.windows = Tk()
        self.windows.title('桌面整理小程序')
        self.Frame = Frame(self.windows)
        self.Frame.grid()
        self.Frame3 = Frame(self.windows)
        self.Frame3.grid()
        self.Frame4 = Frame(self.windows)
        self.Frame4.grid()
        self.Frame5 = Frame(self.windows)
        self.Frame5.grid()
        self.Frame2 = Frame(self.windows)
        self.Frame2.grid()

        self.windows.resizable(width=False, height=False)
        self.ft1 = tkFont.Font(size=14, slant=tkFont.ITALIC)
        self.gui()
        self.Button()

        self.windows.mainloop()

    def gui(self):
        self.PATHNAME = StringVar()
        self.PATHNAME2 = StringVar()
        self.FILENAM = StringVar()
        self.FILE = IntVar()
        Wecome = Label(self.Frame, text="桌面整理小程序",font=("华文行楷",25),width = 15)
        PATHtxt = Label(self.Frame3, text="整理路径",width = 12)

        Black = Label(self.Frame3)

        comment = Label(self.Frame5, text="输入路径，勾选，需要整理的后缀类型文件，点击整理",font = (20),height = 2)


        PATHEnter = Entry(self.Frame3,text="例如:C:\\Users\\Administrator\\Desktop",textvariable = self.PATHNAME,\
                          width = 28)

        PATHtxt2 = Label(self.Frame4, text="存储路径", width=12)
        PathName= Label(self.Frame4, text="存储文件夹名", width=12)
        FILENAME = Entry(self.Frame4, text="存储文件输入框", width=15,textvariable = self.FILENAM)
        black = Label(self.Frame4)
        RepositoryPath = Entry(self.Frame4, textvariable=self.PATHNAME2, width=28)
        Buttonn = Button(self.Frame4, text='整理', command=self.function,width = 6)
        FiLe = Checkbutton(self.Frame4, text="不创建包容的文件夹", variable=self.FILE)
        self.Vi = Label(self.Frame4, text="欢迎您的到来，干巴爹")

        FiLe.grid(row = 3,column = 1,sticky=W)
        PATHtxt.grid(row = 1,column = 0,sticky = E)
        comment.grid(row = 0,column = 1)
        Black.grid(row = 1,column = 2)
        PATHEnter.grid(row = 1,column = 1)
        Buttonn.grid(row = 2,column =1,sticky = E)
        Wecome.grid(row = 0,column = 0)
        PATHtxt2.grid(row = 1,column = 0,sticky = E)
        PathName.grid(row=2, column=0, sticky=E)
        black.grid(row=1, column=2)
        RepositoryPath.grid(row = 1,column = 1)
        self.Vi.grid(row = 4,column = 1,sticky= W)
        FILENAME.grid(row=2, column=1,sticky= W)




    def JPG(self):
        if self.jpg.get() == 1:
            self.List.append('.jpg')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.jpg':
                    self.List.pop(i)
                    print(self.List)
                    return


        print(self.List)
    def PNG(self):
        if self.png.get() == 1:
            self.List.append('.png')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.png':
                    self.List.pop(i)
                    print(self.List)
                    return

        print(self.List)
    def PSD(self):
        if self.psd.get() == 1:
            self.List.append('.psd')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.psd':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def XLS(self):
        if self.xls.get() == 1:
            self.List.append('.xls')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.xls':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def XLSX(self):
        if self.xlsx.get() == 1:
            self.List.append('.xlsx')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.xlsx':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def LNK(self):
        if self.lnk.get() == 1:
            self.List.append('.lnk')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.lnk':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def TXT(self):
        if self.txt.get() == 1:
            self.List.append('.txt')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.txt':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def LNK(self):
        if self.lnk.get() == 1:
            self.List.append('.lnk')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.lnk':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def PY(self):
        if self.py.get() == 1:
            self.List.append('.py')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.py':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def GIF(self):
        if self.gif.get() == 1:
            self.List.append('.gif')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.gif':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def VSDX(self):
        if self.vsdx.get() == 1:
            self.List.append('.vsdx')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.vsdx':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def PPTX(self):
        if self.pptx.get() == 1:
            self.List.append('.pptx')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.pptx':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def RAR(self):
        if self.rar.get() == 1:
            self.List.append('.rar')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.rar':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def DOCX(self):
        if self.docx.get() == 1:
            self.List.append('.docx')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.docx':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def DOC(self):
        if self.doc.get() == 1:
            self.List.append('.doc')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.doc':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def BMP(self):
        if self.bmp.get() == 1:
            self.List.append('.bmp')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.bmp':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def BAT(self):
        if self.bat.get() == 1:
            self.List.append('.bat')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.bat':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def JPEG(self):
        if self.jpeg.get() == 1:
            self.List.append('.jpeg')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.jpeg':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def AVI(self):
        if self.avi.get() == 1:
            self.List.append('.avi')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.avi':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def MP4(self):
        if self.mp4.get() == 1:
            self.List.append('.mp4')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.mp4':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def MOV(self):
        if self.mov.get() == 1:
            self.List.append('.mov')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.mov':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def MP3(self):
        if self.mp3.get() == 1:
            self.List.append('.mp3')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.mp3':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)
    def ASF(self):
        if self.asf.get() == 1:
            self.List.append('.asf')
        else:
            for i in range(len(self.List)):
                if self.List[i] == '.asf':
                    self.List.pop(i)
                    print(self.List)
                    return
        print(self.List)


    def function(self):
        #如果存储路径没写，默认在整理路径下创建目录保存
        for i in self.FILENAM.get():
            print(i)
            if i in special:
                self.Vi['text'] = '文件名字不能有\\ / * , ? <>|等字符'
                return

        if self.FILENAM.get() != '': #如果存储文件名为空，使用默认
            self.NAME = self.FILENAM.get()

        if self.FILE.get() == 0:
            if self.PATHNAME2.get() == '' and os.path.exists(self.PATHNAME.get()):
                PATHNAME2 = self.PATHNAME.get()
                b = Neaten(self.List, self.PATHNAME.get(),PATHNAME2, self.NAME)
            elif os.path.exists(self.PATHNAME.get()) and os.path.exists(self.PATHNAME2.get()):
                b = Neaten(self.List, self.PATHNAME.get(), self.PATHNAME2.get(),self.NAME)


            else:
                print('请输入正确的路径')
                return
            self.Vi['text'] = '处理完成'


        elif self.FILE.get() == 1:
            if self.PATHNAME2.get() == '' and os.path.exists(self.PATHNAME.get()):
                PATHNAME2 = self.PATHNAME.get()
                b = Neaten(self.List, self.PATHNAME.get(),PATHNAME2,self.NAME,IF = False,IIF = False)
            elif os.path.exists(self.PATHNAME.get()) and os.path.exists(self.PATHNAME2.get()):
                b = Neaten(self.List, self.PATHNAME.get(), self.PATHNAME2.get(),self.NAME,IF =False,IIF =False)
            else:
                print('请输入正确的路径')
                return
                #b = Neaten(self.List,self.PATHNAME.get(),self.PATHNAME2.get())

            self.Vi['text'] = '处理完成'



    def Button(self):
        self.avi = IntVar()
        self.mov = IntVar()
        self.asf = IntVar()
        self.mp4 = IntVar()
        self.mp3 = IntVar()

        self.jpg = IntVar()
        self.png = IntVar()
        self.psd = IntVar()
        self.xls = IntVar()
        self.xlsx = IntVar()
        self.lnk = IntVar()
        self.txt = IntVar()
        self.py = IntVar()
        self.vsdx = IntVar()
        self.pptx = IntVar()
        self.rar = IntVar()
        self.docx = IntVar()
        self.doc = IntVar()
        self.bmp = IntVar()
        self.bat = IntVar()
        self.jpeg = IntVar()

        Avi  = Checkbutton(self.Frame2, text="AVI", variable=self.avi, command=self.AVI,width = 7)
        Mov  = Checkbutton(self.Frame2, text="MOV", variable=self.mov, command=self.MOV,width = 7)
        Asf  = Checkbutton(self.Frame2, text="asf", variable=self.asf, command=self.ASF,width = 7)
        Mp4  = Checkbutton(self.Frame2, text="mp4", variable=self.mp4, command=self.MP4,width = 7)
        Mp3  = Checkbutton(self.Frame2, text="mp3", variable=self.mp3, command=self.MP3,width = 7)
        Jpg  = Checkbutton(self.Frame2, text="Jpg", variable=self.jpg, command=self.JPG,width = 7)
        Png  = Checkbutton(self.Frame2, text="Png", variable=self.png, command=self.PNG,width = 7)
        Psd  = Checkbutton(self.Frame2, text="Psd", variable=self.psd, command=self.PSD,width = 7)
        Xls  = Checkbutton(self.Frame2, text="Xls", variable=self.xls, command=self.XLS,width = 7)
        Xlsx = Checkbutton(self.Frame2, text="Xlsx", variable=self.xlsx, command=self.XLSX,width = 7)
        Lnk  = Checkbutton(self.Frame2, text="Lnk", variable=self.lnk, command=self.LNK,width = 7)
        Txt  = Checkbutton(self.Frame2, text="Txt", variable=self.txt, command=self.TXT,width = 7)
        Py   = Checkbutton(self.Frame2, text="Py", variable=self.py, command=self.PY,width = 7)
        Vsdx = Checkbutton(self.Frame2, text="Vsdx", variable=self.vsdx, command=self.VSDX,width = 7)
        Pptx = Checkbutton(self.Frame2, text="Pptx", variable=self.pptx, command=self.PPTX,width = 7)
        Rar  = Checkbutton(self.Frame2, text="Rar", variable=self.rar, command=self.RAR,width = 7)
        Doc  = Checkbutton(self.Frame2, text="Doc", variable=self.doc, command=self.DOC,width = 7)
        Docx = Checkbutton(self.Frame2, text="Docx", variable=self.docx, command=self.DOCX,width = 7)
        Bmp  = Checkbutton(self.Frame2, text="Bmp", variable=self.bmp, command=self.BMP,width = 7)
        Bat  = Checkbutton(self.Frame2, text="Bat", variable=self.bat, command=self.BAT,width = 7)
        Jpeg  = Checkbutton(self.Frame2, text="Jpeg", variable=self.jpeg, command=self.JPEG,width = 7)


        Jpg.grid(row = 2,column = 0,sticky = W)
        Png.grid(row = 2,column = 1,sticky = W)
        Psd.grid(row = 2,column =2,sticky = W)
        Xls.grid(row = 2,column = 3,sticky = W)
        Xlsx.grid(row = 2,column = 4,sticky = W)
        Lnk.grid(row = 3,column = 0,sticky = W)
        Txt.grid(row = 3,column = 1,sticky = W)
        Py.grid(row = 3,column = 2,sticky = W)
        Vsdx.grid(row = 3,column = 3,sticky = W)
        Pptx.grid(row = 3,column = 4,sticky = W)
        Rar.grid(row = 4,column = 0,sticky = W)
        Doc.grid(row = 4,column = 1,sticky = W)
        Docx.grid(row = 4,column = 2,sticky = W)
        Bmp.grid(row = 4,column = 3,sticky = W)
        Bat.grid(row = 4,column = 4,sticky = W)
        Jpeg.grid(row = 5,column = 0,sticky = W)
        Avi.grid(row = 5,column = 1,sticky = W)
        Mov.grid(row = 5,column = 2,sticky = W)
        Mp3.grid(row = 5,column = 3,sticky = W)
        Mp4.grid(row = 5,column = 4,sticky = W)
        Asf.grid(row = 6,column = 0,sticky = W)
if __name__ == '__main__':
    Gui()