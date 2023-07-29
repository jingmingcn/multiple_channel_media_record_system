import json
import time
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from CvPyGui.ui import child_file
Ui_ChildWindow_2 = child_file.Ui_Form
class child_file_setting(QWidget,Ui_ChildWindow_2):
    #功能：选择文件路径。。显示当前的文件路径。。
    #选择音视频保存的格式  是名字的格式还是文件格式？
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitChildWindwo()
    def InitChildWindwo(self):
        #初始化，，，读取json文件，显示当前的保存路径
        with open("config/db.json","r",encoding='UTF-8') as dbfile_r:
            file_save_path = json.load(dbfile_r)
        self.file_path_label.setText(file_save_path["save_path"])
        self.CreateButtons()
        if file_save_path["video_format"] == ".avi":
            self.radioButton_avi.setChecked(True)
        else:
            self.radioButton_mp4.setChecked(True)
        if file_save_path["voice_format"] == ".wav":
            self.radioButton_wav.setChecked(True)
        else:
            self.radioButton_mp3.setChecked(True)
    def msg(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        with open("config/db.json","r",encoding='UTF-8') as file_r:
            savepath = json.load(file_r)
        #原路径保存至former_save_path
        former_save_path = savepath["save_path"]
        print(m)#打印刚刚获取的当前路径
        #如果获取的路径为空，就不改变路径，把之前的路径赋给新的路径
        if m == "":
            m = former_save_path
        print(m)
        savepath["save_path"] = m
        #将更改后（或获取空时不更改）的路径写入json文件
        with open("config/db.json","w",encoding='UTF-8') as dbfile:
            json.dump(savepath,dbfile)
        time.sleep(0.5)
        self.update_file_save_path()
    def update_file_save_path(self):
        with open("config/db.json","r",encoding='UTF-8') as dbfile_r:
            file_save_path = json.load(dbfile_r)
        self.file_path_label.setText(str(file_save_path['save_path']))
    def ok_close(self):
        self.close()
    def mp3_button(self):
        if self.radioButton_mp3.isChecked() == True:
            self.voiceformat = ".mp3"
        else:
            self.voiceformat = ".wav"
        with open("config/db.json","r",encoding='UTF-8') as dbfile:
            json_file = json.load(dbfile)
        json_file["voice_format"] = self.voiceformat
        with open("config/db.json","w",encoding='UTF-8') as dbfile:
            json.dump(json_file,dbfile)
        print(self.voiceformat)
    def video_radio_button(self):
        if self.radioButton_mp4.isChecked() == True:
            self.videoformat = ".mp4v"
        else:
            self.videoformat = ".avi"
        with open("config/db.json","r",encoding='UTF-8') as dbfile:
            json_file = json.load(dbfile)
        json_file["video_format"] = self.videoformat
        with open("config/db.json","w",encoding='UTF-8') as dbfile:
            json.dump(json_file,dbfile)
        print(self.videoformat)
    def CreateButtons(self):
        self.choice_file_path_button.clicked.connect(self.msg)
        self.file_ok.clicked.connect(self.ok_close)
        self.radioButton_mp3.clicked.connect(self.mp3_button)
        self.radioButton_wav.clicked.connect(self.mp3_button)
        self.radioButton_mp4.clicked.connect(self.video_radio_button)
        self.radioButton_avi.clicked.connect(self.video_radio_button)