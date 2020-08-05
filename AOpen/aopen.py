import os


class AOpen():
    path=''
    # file_name='file'
    encode_mode='utf-8'
    mode='r'
    cursor=0
    def __init__(self, path, encode_mode='utf-8', mode=511):
        self.path=path
        # self.file_name=file_name
        self.encode_mode=encode_mode
        self.mode=mode


    # def opener(path, flags):
    #     return os.open(path, flags, dir_fd=dir_fd)
    

    def close(self):
        with open(self.path) as file:
            return file.close()

    def write(self,  text):
        with open(self.path, mode='w') as file:
            return file.write(text)


    def writeline(self,  text, bytes):
        with open(self.path, mode='a') as file:
            return file.writeline(text)




    def writelines_w(self, list=[]):
        with open(self.path, mode='w') as file:
            for i in list:
                file.writelines(i)

    
    
    def writelines_a(self, list=[]):
        with open(self.path, mode='a') as file:
            for i in list:
                file.writelines(i+'\n')


    def read(self, bytes=-1):
        with open(self.path,mode='r') as file:
            return file.read(bytes)

    
    def readline(self, bytes=-1):
        with open(self.path,mode='r') as file:
            return file.readline(bytes)


    def readlines(self, bytes=-1):
        with open(self.path,mode='r') as file:
            return file.readlines(bytes)


    def seek(self,cursor):
        with open(self.path) as file:
            file.seek(cursor)
            return cursor



    def tell(self):
        return self.cursor







file = AOpen('hello.txt')
