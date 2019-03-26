"""
1.获取路径目录信息
2.写判定条件，条件符合，创建目录，移动符合条件的文件进目录，并以后缀名分类 # 完成
3.写UI界面
4.实现，word，excel，ppt，图片等，视频，txt，画图软件，python文件，psd模板（PS）

"""

##os.rmdir(splitext[1:])#删除空目录
import sys
import os
import shutil
#b  = os.self.Path.absself.Path(os.curdir)  #获取现在的绝对路径
class Neaten:
    def __init__(self,list,Path,storePath,Namee,IF = True,IIF = True):
        self.suffix =  list
        self.IF = IF
        self.NAME = Namee
        self.IIF = IIF
        self.Path = Path + '\\'
        self.StorePath = storePath + '\\' #  在哪里保存的路径
        self.main()

    #创建文件夹
    def found(self,Name):
        os.chdir(self.StorePath)
        SCROE = 0
        isExists = os.path.exists(Name)
        while self.IF:

            if not isExists:
                os.makedirs(Name)
                self.IF = False

            else:
                SCROE += 1
                Name += '_' + str(SCROE)
                isExists = os.path.exists(Name)
                if not isExists:
                    os.makedirs(Name)
                    self.NAME = Name
                    self.IF = False
        return  self.NAME
        #更新路径




    def main(self):
        for i,j,k in os.walk(self.Path): #i = 当前路径 j = 获取目录  k = 获取目录和文件
            for K in k: #读取文件
                print(K)
                if i in self.Path: # 不获取目录文件
                    # 现在的K 等于文件名字
                    # i = 路径
                    splitext0 = os.path.splitext(K)[0]  #获取路径名字是以元组方式，0是名，1是后缀
                    splitext = os.path.splitext(K)[1]

                    if splitext == '':
                        return '请确保文件有不是空名字'


                    if splitext in self.suffix and self.IIF == True:
                        RETURN = self.found(self.NAME)
                        os.chdir(self.StorePath + RETURN)  # 去到新的路径
                        isExists = os.path.exists(splitext[1:])  # 判断该字符名，当前是否创建了目录
                        if not isExists:  # 如果不存在，则创建目录   创建目录操作函数
                            os.makedirs(splitext[1:])
                        print(self.suffix,splitext0)
                        # 判断 获取的文件名后缀，是否是在列表内的
                        try:
                            FileName = ''.join(os.path.splitext(K))#完整的文件名

                            shutil.move(i + FileName,self.StorePath + RETURN  + str('\\') + splitext[1:])
                        except shutil.Error:
                            #出现重名后的处理， 后期添加 用户决定是否移动，否，就跳过这个（加个pass就好）
                            Love = False
                            score = 0
                            while not Love:
                                score += 1
                                NewName = splitext0 + '_' + str(score) + splitext
                                os.chdir(self.Path)
                                try:
                                    B = os.rename(FileName, NewName)
                                    shutil.move(i + NewName,self.StorePath + RETURN  + str('\\') + splitext[1:])
                                    Love = True
                                # 这里的异常是，在重复后改名，之后在本地路径又重名后的处理
                                except FileExistsError:
                                    pass
                                except shutil.Error:
                                    FileName = NewName

                    if splitext in self.suffix and self.IIF == False:
                        # 判断 获取的文件名后缀，是否是在列表内的
                        if not self.IIF:
                            os.chdir(self.StorePath)
                            isExists = os.path.exists(splitext[1:])  # 判断该字符名，当前是否创建了目录
                            if not isExists:  # 如果不存在，则创建目录   创建目录操作函数
                                os.makedirs(splitext[1:])
                        try:
                            FileName = ''.join(os.path.splitext(K))  # 完整的文件名

                            shutil.move(i + FileName, self.StorePath + splitext[1:])
                        except shutil.Error:
                            # 出现重名后的处理， 后期添加 用户决定是否移动，否，就跳过这个（加个pass就好）
                            Love = False
                            score = 0
                            while not Love:
                                score += 1
                                NewName = splitext0 + '_' + str(score) + splitext
                                os.chdir(self.Path)
                                try:
                                    B = os.rename(FileName, NewName)

                                    shutil.move(i + NewName, self.StorePath + splitext[1:])
                                    Love = True
                                # 这里的异常是，在重复后改名，之后在本地路径又重名后的处理
                                except FileExistsError:
                                    pass
                                except shutil.Error:
                                    FileName = NewName

