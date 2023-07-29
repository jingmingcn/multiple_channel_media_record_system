import json
import time
import numpy as np
import pyaudio
from PyQt5.QtCore import (QTimer, pyqtSignal,QThread)
from CvPyGui import ImageCvQtContainer
import pygame
import cv2
import threading
from PyQt5.QtWidgets import QWidget
from CvPyGui.ui import child_test
Ui_ChildWindow = child_test.Ui_Form
hd_width = 1920
hd_higth= 1080
pleace_choice_camera = '请选择摄像头'
no_camera_ = '不选择摄像头'
pleace_choice_voice = '请选择麦克风'
no_voice = '不选择麦克风'
img_no_camera = cv2.imread('config/image/no_camera.jpg', cv2.IMREAD_COLOR)
img_no_voice = cv2.imread('config/image/no_voice.jpg', cv2.IMREAD_COLOR)
img_voice = cv2.imread('config/image/voice.jpg',cv2.IMREAD_COLOR)
tab1_judge = False #判断下拉列表选择的内容是否是摄像头
tab2_judge = False
tab3_judge = False
tab4_judge = False
camera_judge = {}
thread_judge = {}
frame = {}
frame2 = {}
frame3 = {}
cap = {}
cap2 = {}
cap3 = {}
tab1_text = ''
tab2_text = ''
tab3_text = ''
tab4_text = ''
class UpdateVolume(QThread):
    update_data = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.vo_judge = True
        self.voice_index_thread = 0
    def run(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        INTERVAL = 5
        pa = pyaudio.PyAudio()
        stream = pa.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         frames_per_buffer=CHUNK,
                         input_device_index=self.voice_index_thread)
        buffer = []
        while self.vo_judge:
            for i in range(int(INTERVAL * RATE / CHUNK)):  # STREAN INTERVAL
                if self.vo_judge == False:
                    break
                data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
                self.un = int(np.amax(data))
                self.un = int(pow(self.un,0.5))
                if self.un >= 100:
                    self.un = 99
                self.update_data.emit(str(self.un))
        print('子线程结束')
#1:下拉列表选择后lable标签显示对应的视频。  获取下拉列表的内容  根据内容确定显示的摄像头。
class Child_Window(QWidget,Ui_ChildWindow):
    def __init__(self):
        super().__init__()
        Ui_ChildWindow.__init__(self)
        self.setupUi(self)
        self.InitChildWindow()
        self.timer = QTimer()
        self.child_wind_judge = True
    def InitChildWindow(self):#初始化子窗口
        pygame.init()
        pygame.camera.init()
        global cameralist_child
        cameralist_child = pygame.camera.list_cameras()
        self.update_tab1_image = ImageCvQtContainer.Image('tab1_label_camera', self.tab1_label)
        self.update_tab2_image = ImageCvQtContainer.Image('tab2_label_camera', self.tab1_label_3)
        self.update_tab3_image = ImageCvQtContainer.Image('tab3_label_camera', self.tab1_label_4)
        self.update_tab1_image.updateImage(img_no_camera)
        self.update_tab2_image.updateImage(img_no_camera)
        self.update_tab3_image.updateImage(img_no_camera)
        self.tab1_combobox.addItem(pleace_choice_camera)
        self.tab1_combobox_3.addItem(pleace_choice_camera)
        self.tab1_combobox_4.addItem(pleace_choice_camera)
        self.tab1_combobox_7.addItem(pleace_choice_voice)
        self.tab1_combobox.addItem(no_camera_)
        self.tab1_combobox_3.addItem(no_camera_)
        self.tab1_combobox_4.addItem(no_camera_)
        self.tab1_combobox_7.addItem(no_voice)
        self.tab1_combobox.addItems(cameralist_child)
        self.tab1_combobox_3.addItems(cameralist_child)
        self.tab1_combobox_4.addItems(cameralist_child)
        self.CreateButtons()
        with open("config/db.json","r",encoding='UTF-8') as dbfile_r:
            camera_voice_name = json.load(dbfile_r)
        self.tab1_text = camera_voice_name["hd_camera_name"]
        self.tab2_text = camera_voice_name["face_camera_name"]
        self.tab3_text = camera_voice_name["eye_camera_name"]
        self.tab4_text = camera_voice_name["hk_voice_name"]
        if len(cameralist_child) >= 1:
            for i in range(len(cameralist_child)):
                camera_judge[i] = 'close'
        else:
            print('no camera')
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        global voice_list
        voice_list = []
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                voice_list.append(p.get_device_info_by_host_api_device_index(0, i).get('name'))
        self.tab1_combobox_7.addItems(voice_list)
        self.child_wind_judge = True
        if self.tab1_text in cameralist_child:
            self.tab1_combobox.setCurrentIndex(cameralist_child.index(self.tab1_text) + 2)
        if self.tab2_text in cameralist_child:
            self.tab1_combobox_3.setCurrentIndex(cameralist_child.index(self.tab2_text) + 2)
        if self.tab3_text in cameralist_child:
            self.tab1_combobox_4.setCurrentIndex(cameralist_child.index(self.tab3_text) + 2)
        if self.tab4_text in voice_list:
            self.tab1_combobox_7.setCurrentIndex(voice_list.index(self.tab4_text) + 2)
    def tab1_combobox_setting(self):  # tab1中的下拉列表选择摄像头
        #获取当前下拉列表选中的文本
        tab1_camera_text = self.tab1_combobox.currentText()
        self.tab1_text = tab1_camera_text
        #尝试查询当前文本所在摄像头列表中第几项，查询不到则显示没有摄像头的图片。
        try:
            tab1_camera_index = cameralist_child.index(tab1_camera_text)
            tab1_judge = True
        except:
            self.update_tab1_image.updateImage(img_no_camera)
            tab1_judge = False
        #获取摄像头的名字后显示画面
        #启动一个线程，显示摄像头捕获的画面
        #如果查询到文本所在该列表中，并且该摄像头没有打开，就启动线程显示该摄像头的画面
        if tab1_judge:
            if camera_judge[tab1_camera_index] == 'close':
                camera_judge[tab1_camera_index] = 'open'
                threading._start_new_thread(self.open_camera,(tab1_camera_index,))
        else:
           self.update_tab1_image.updateImage(img_no_camera)
    def tab2_combobox_setting(self):
        tab2_camera_text = self.tab1_combobox_3.currentText()
        self.tab2_text = tab2_camera_text
        try:
            tab2_camera_index = cameralist_child.index(tab2_camera_text)
            tab2_judge = True
        except:
            self.update_tab2_image.updateImage(img_no_camera)
            tab2_judge = False
        # 获取摄像头的名字后显示画面
        # 启动一个线程，显示摄像头捕获的画面
        if tab2_judge:
            #如果选择的摄像头没有打开
            if camera_judge[tab2_camera_index] == 'close':
                camera_judge[tab2_camera_index] = 'open'
                threading._start_new_thread(self.open_camera_2, (tab2_camera_index,))
        else:
            self.update_tab2_image.updateImage(img_no_camera)
    def open_camera(self,camera_index):
        #传入摄像头的序号，判断摄像头是否开启的代码应该在调用该函数的函数中。
        #根据摄像头的序号，打开摄像头，然后把摄像头的画面传入其他函数？
        #只有三个要显示的标签，判断要在那个标签上显示，然后更新图片。
        cap[camera_index] = cv2.VideoCapture(camera_index,cv2.CAP_DSHOW)
        print(cap[camera_index].get(3))
        camera_judge[camera_index] = 'open'
        cap[camera_index].set(3,hd_width)
        cap[camera_index].set(4,hd_width)
        cap[camera_index].set(5,30)
        while self.child_wind_judge:
            self.ret, frame[camera_index] = cap[camera_index].read()
            if self.ret:
                #判断需要在哪几个标签上显示  判断方式：获取三个下拉列表当前显示的值，确定该值在摄像头列表中所占的序号，序号与camera_index相同则更新图片。
                frame[camera_index] = cv2.cvtColor(frame[camera_index], cv2.COLOR_BGR2RGB)
                if (self.tab1_combobox.currentText() != pleace_choice_camera) and (self.tab1_combobox.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox.currentText()):
                        self.update_tab1_image.updateImage(frame[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_3.currentText() != pleace_choice_camera) and (self.tab1_combobox_3.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_3.currentText()):
                        self.update_tab2_image.updateImage(frame[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_4.currentText() != pleace_choice_camera) and (self.tab1_combobox_4.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_4.currentText()):
                        self.update_tab3_image.updateImage(frame[camera_index])
                    else:
                        pass
                else:
                    pass
                if (cameralist_child[camera_index] != self.tab1_combobox.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_3.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_4.currentText()):
                    camera_judge[camera_index] = 'close'
                    break
            if self.child_wind_judge == False: #子窗口如果关闭就停止循环
                break
    def open_camera_2(self,camera_index):
        cap2[camera_index] = cv2.VideoCapture(camera_index,cv2.CAP_DSHOW)
        camera_judge[camera_index] = 'open'
        cap2[camera_index].set(3,hd_width)
        cap2[camera_index].set(4,hd_width)
        cap2[camera_index].set(5,30.0)
        while self.child_wind_judge:
            self.ret_2,frame2[camera_index] = cap2[camera_index].read()
            if self.ret_2:
                frame2[camera_index] = cv2.cvtColor(frame2[camera_index], cv2.COLOR_BGR2RGB)
                if (self.tab1_combobox.currentText() != pleace_choice_camera) and (self.tab1_combobox.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox.currentText()):
                        self.update_tab1_image.updateImage(frame2[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_3.currentText() != pleace_choice_camera) and (self.tab1_combobox_3.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_3.currentText()):
                        self.update_tab2_image.updateImage(frame2[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_4.currentText() != pleace_choice_camera) and (self.tab1_combobox_4.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_4.currentText()):
                        self.update_tab3_image.updateImage(frame2[camera_index])
                    else:
                        pass
                else:
                    pass
                if (cameralist_child[camera_index] != self.tab1_combobox.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_3.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_4.currentText()):
                    camera_judge[camera_index] = 'close'
                    break
                else:
                    pass
                if self.child_wind_judge == False: #子窗口如果关闭就停止循环
                    break
    def open_camera_3(self,camera_index):
        cap3[camera_index] = cv2.VideoCapture(camera_index,cv2.CAP_DSHOW)
        camera_judge[camera_index] = 'open'
        cap3[camera_index].set(3,hd_width)
        cap3[camera_index].set(4,hd_width)
        cap3[camera_index].set(5,30.0)
        while self.child_wind_judge:
            self.ret_3, frame3[camera_index] = cap3[camera_index].read()
            if self.ret_3:
                frame3[camera_index] = cv2.cvtColor(frame3[camera_index], cv2.COLOR_BGR2RGB)
                if (self.tab1_combobox.currentText() != pleace_choice_camera) and (self.tab1_combobox.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox.currentText()):
                        self.update_tab1_image.updateImage(frame3[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_3.currentText() != pleace_choice_camera) and (self.tab1_combobox_3.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_3.currentText()):
                        self.update_tab2_image.updateImage(frame3[camera_index])
                    else:
                        pass
                else:
                    pass
                if (self.tab1_combobox_4.currentText() != pleace_choice_camera) and (self.tab1_combobox_4.currentText() != no_camera_):
                    if camera_index == cameralist_child.index(self.tab1_combobox_4.currentText()):
                        self.update_tab3_image.updateImage(frame3[camera_index])
                    else:
                        pass
                else:
                    pass
                if (cameralist_child[camera_index] != self.tab1_combobox.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_3.currentText()) & (cameralist_child[camera_index] != self.tab1_combobox_4.currentText()):
                    camera_judge[camera_index] = 'close'
                    break
                else:
                    pass
                if self.child_wind_judge == False: #子窗口如果关闭就停止循环
                    break
    def tab3_combobox_setting(self):
        tab3_camera_text = self.tab1_combobox_4.currentText()
        self.tab3_text = tab3_camera_text
        try:
            tab3_camera_index = cameralist_child.index(tab3_camera_text)
            tab3_judge = True
        except:
            self.update_tab3_image.updateImage(img_no_camera)
            tab3_judge = False
        # 获取摄像头的名字后显示画面
        # 启动一个线程，显示摄像头捕获的画面
        if tab3_judge:
            if camera_judge[tab3_camera_index] == 'close':
                camera_judge[tab3_camera_index] = 'open'
                threading._start_new_thread(self.open_camera_3, (tab3_camera_index,))
        else:
            self.update_tab3_image.updateImage(img_no_camera)
    def tab4_voice_setting(self):
        tab4_voice_text = self.tab1_combobox_7.currentText()
        self.tab4_text = tab4_voice_text
        try:
            voice_index = voice_list.index(self.tab4_text)
            tab4_judge = True
        except:
            tab4_judge =False
        try:
            self.sub_thread.vo_judge = False
        except:
            pass
        time.sleep(0.2)
        if tab4_judge:
            self.sub_thread = UpdateVolume()
            self.sub_thread.vo_judge = True
            self.sub_thread.voice_index_thread = voice_index
            self.sub_thread.update_data.connect(self.unnn)
            self.sub_thread.start()
        else:
            print('无声音设备')
        print('voice setting')
    def unnn(self,data):
        self.progressBar.setValue(int(data))
    def save_camera_json(self):
        #用来关闭上面所有的线程，改写json配置文件。
        # tab1_text、tab2_text、tab3_text分别是行为、面部、眼部的摄像头名字，初始内容为读取json文件得到的。
        with open("config/db.json","r",encoding='UTF-8') as dbfile_r:
            camera_voice_name = json.load(dbfile_r)
        camera_voice_name["hd_camera_name"] = self.tab1_text
        camera_voice_name["face_camera_name"] = self.tab2_text
        camera_voice_name["eye_camera_name"] = self.tab3_text
        camera_voice_name["hk_voice_name"] = self.tab4_text
        with open("config/db.json","w",encoding='UTF-8') as dbfile:
            json.dump(camera_voice_name,dbfile)
        self.child_wind_judge = False
        try:
            self.sub_thread.vo_judge = False
            print('success')
        except:
            print('defalt')
        self.close()#关闭该窗口
    def closeEvent(self, event):
        print('关闭窗口')
        self.child_wind_judge = False
        try:
            self.sub_thread.vo_judge = False
            self.child_wind_judge = False
        except:
            pass
#应该是改变摄像头选项时修改配置文件还是在点确认是关闭呢？ 点确认时关闭，先把选好的信息存起来，点确认时修改。
    def CreateButtons(self):
        # print("createbuttons")
        self.tab1_combobox.currentIndexChanged.connect(self.tab1_combobox_setting)
        self.tab1_combobox_3.currentIndexChanged.connect(self.tab2_combobox_setting)
        self.tab1_combobox_4.currentIndexChanged.connect(self.tab3_combobox_setting)
        self.tab1_combobox_7.currentIndexChanged.connect(self.tab4_voice_setting)
        self.OK.clicked.connect(self.save_camera_json)
