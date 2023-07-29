import wave
import cv2, os
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import (QMainWindow,QMessageBox,)
import threading
import time
from CvPyGui import ImageCvQtContainer
from CvPyGui import child_CameraVoice_setting
from CvPyGui import Child_File_Setting
from CvPyGui.ui import gui
from datetime import datetime
import pygame
import pygame.camera
import pyaudio
Ui_MainWindow = gui.Ui_MainWindow
import json
img_no_camera = cv2.imread('config/image/no_camera.jpg', cv2.IMREAD_COLOR)
img_no_voice = cv2.imread('config/image/no_voice.jpg', cv2.IMREAD_COLOR)
img_voice=cv2.imread('config/image/voice.jpg',cv2.IMREAD_COLOR)
class MyApp(QMainWindow, Ui_MainWindow, threading.Thread):
    filter_count = 0
    def __init__(self,chunk=1024, rate=16000):
        super().__init__()
        threading.Thread.__init__(self)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()
        self.hd_camera=-1
        self.voice_index=-1
        self.eye_camera=-1
        self.face_camera=-1
        self.hd_width = 1920
        self.hd_height = 1080
        self.face_width = 1280
        self.eye_width = 1280
        self.face_height = 1920
        self.eye_height = 720
        self.hd_fps = 30.0
        self.face_fps = 10.0
        self.eye_fps = 10.0
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = rate
        self._win1_running = True
        self._win2_running = True
        self._win3_running = True
        self._voice_get = True
        self._begin = False
        self._frames = []
        self._init_running = True
        self._start_running = True
        self.record_judge = False
        self.recording_time = '0'
        self.recording_location = 'c/'
        self.recording_information = self.recording_time + '  ' + self.recording_location
    def initUI(self):
        self.original1_image = ImageCvQtContainer.Image(
            'camera1', self.original_frame_lbl)
        self.original2_image = ImageCvQtContainer.Image(
            'camera2', self.processed_frame_lbl)
        self.eye_image = ImageCvQtContainer.Image('eye_camera', self.eye_lbl)
        self.voice_image = ImageCvQtContainer.Image('voice_mic', self.voice_lbl)
        self.setBackground()
        self.createButtons()
        self.Child_File_Setting()
    def r_json(self):
        #读取配置文件
        with open('config/db.json',encoding='utf-8',mode='r') as rf:
            data = rf.read().encode()
            configuration = json.loads(data)
            print('configuation')
            print(configuration)
            self.hd_cream_name=configuration['hd_camera_name']
            self.face_camera_name=configuration['face_camera_name']
            self.eye_camera_name=configuration['eye_camera_name']
            self.vocie_name=configuration['voice_name']
            self.hk_voice_name=configuration['hk_voice_name']
            self.bluetooth_voice_name=configuration['bluetooth_voice_name']
            self.save_path=configuration['save_path']
            self.hd_width=configuration['hd_width']
            self.hd_height=configuration['hd_height']
            self.hd_fps=configuration['hd_fps']
            self.face_width=configuration['face_width']
            self.face_height=configuration['face_height']
            self.face_fps=configuration['face_fps']
            self.eye_width=configuration['eye_width']
            self.eye_height=configuration['eye_height']
            self.eye_fps=configuration['eye_fps']
            self.voice_format = configuration['voice_format']
            self.video_format = configuration['video_format']
            self.recorfing_location = self.save_path
    def initfrom(self):
        if self._init_running:
            self._init_running=False
            pygame.init()
            pygame.camera.init()
            cameralist = pygame.camera.list_cameras()
            print(cameralist)
            p = pyaudio.PyAudio()
            info = p.get_host_api_info_by_index(0)
            numdevices = info.get('deviceCount')
            voice_list = []
            for i in range(0, numdevices):
                if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                    voice_list.append(p.get_device_info_by_host_api_device_index(0, i).get('name'))
            print(voice_list)
            try:
                self.r_json()
            except:
                self.statusbar.showMessage('未找到配置文件',5000)
            try:
                self.hd_camera=cameralist.index(self.hd_cream_name)
            except:
                self.hd_camera=-1
            try:
                self.face_camera=cameralist.index(self.face_camera_name)
            except:
                self.face_camera=-1
            try:
                self.eye_camera=cameralist.index(self.eye_camera_name)
            except:
                self.eye_camera=-1
            try:
                if self.hk_voice_name in voice_list:
                    self.voice_index = voice_list.index(self.hk_voice_name)
                else:
                    if self.vocie_name in voice_list and self.bluetooth_voice_name in voice_list:
                        self.voice_index=voice_list.index(self.vocie_name)
                        self.CHANNELS=2
                    elif self.vocie_name in voice_list and self.bluetooth_voice_name not in voice_list:
                        self.voice_index=voice_list.index(self.vocie_name)
                        self.CHANNELS=2
                    elif self.vocie_name not in voice_list and self.bluetooth_voice_name in voice_list:
                        self.voice_index=voice_list.index(self.bluetooth_voice_name)
                    else:
                        self.voice_index = -1
            except:
                self.voice_index=-1
            print(self.hd_camera,'行为设备index')
            print(self.face_camera,'面部设备index')
            print(self.eye_camera,'眼部设备index')
            print(self.voice_index,'音频设备index')
            if os.path.exists(self.save_path) is False:
                os.makedirs(self.save_path)
            if self.hd_camera == -1 and self.face_camera == -1 and self.eye_camera ==-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到任何可用设备', 5000)
            elif self.hd_camera != -1 and self.face_camera == -1 and self.eye_camera ==-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到面部、眼部、音频设备',5000)
            elif self.hd_camera == -1 and self.face_camera != -1 and self.eye_camera ==-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到行为、眼部、音频设备', 5000)
            elif self.hd_camera == -1 and self.face_camera == -1 and self.eye_camera !=-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到行为、面部、音频设备', 5000)
            elif self.hd_camera == -1 and self.face_camera == -1 and self.eye_camera ==-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到行为、面部、眼部设备', 5000)
            elif self.hd_camera != -1 and self.face_camera != -1 and self.eye_camera ==-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到眼部、音频设备', 5000)
            elif self.hd_camera != -1 and self.face_camera == -1 and self.eye_camera !=-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到面部、音频设备', 5000)
            elif self.hd_camera != -1 and self.face_camera == -1 and self.eye_camera ==-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到面部、眼部设备', 5000)
            elif self.hd_camera == -1 and self.face_camera != -1 and self.eye_camera !=-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到行为、音频设备', 5000)
            elif self.hd_camera == -1 and self.face_camera != -1 and self.eye_camera ==-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到行为、眼部设备', 5000)
            elif self.hd_camera == -1 and self.face_camera == -1 and self.eye_camera !=-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到行为、面部设备', 5000)
            elif self.hd_camera != -1 and self.face_camera != -1 and self.eye_camera ==-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到眼部设备', 5000)
            elif self.hd_camera != -1 and self.face_camera == -1 and self.eye_camera !=-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到面部设备', 5000)
            elif self.hd_camera == -1 and self.face_camera != -1 and self.eye_camera !=-1 and self.voice_index !=-1:
                self.statusbar.showMessage('未检测到行为设备', 5000)
            elif self.hd_camera != -1 and self.face_camera != -1 and self.eye_camera !=-1 and self.voice_index ==-1:
                self.statusbar.showMessage('未检测到音频设备', 5000)
            else:
                self.statusbar.showMessage('所有设备准备就绪', 5000)
            self.start()
            self.win_4_upimage()
        else:
            pass
    def child_CameraVoice_setting(self):#点击此选项时不能处于以下状态：  录制视频中。
        if self._init_running == False:
            QMessageBox.information(self,'警告','进程未中止，请中止进程再点击此选项！')
        else:
        #结束录制
            self.endRe()
            self.f_p()
            self.Child_window = child_CameraVoice_setting.Child_Window()
            self.Child_window.setWindowModality(Qt.ApplicationModal)
            self.Child_window.show()
    def Child_File_Setting(self):
        #因为打开软件时便会调用该函数，所以不能调用下面两个方法
        self.child_file_window = Child_File_Setting.child_file_setting()
        self.child_file_window.setWindowModality(Qt.ApplicationModal)
        self.child_file_window.show()
    def start(self):
        threading._start_new_thread(self.win_1,())
        threading._start_new_thread(self.win_2,())
        threading._start_new_thread(self.win_3,())
    def win_1(self):
        if self.hd_camera != -1:
            self._win1_running=True
            self.cap1 = 0
            self.cap1 = cv2.VideoCapture(self.hd_camera,cv2.CAP_DSHOW)
            self.cap1.set(3,2560)
            self.cap1.set(4,1440)
            self.cap1.set(5,self.hd_fps)
            print(self.cap1.get(3))
            print(self.cap1.get(4))
            self.cap1_3 = self.cap1.get(3)  # 宽
            self.cap1_4 = self.cap1.get(4)  # 高
            self.hd_width = self.cap1_3
            self.hd_height = self.cap1_4
            with open("config/db.json", "r", encoding='UTF-8') as dbfile_r_hd:
                jsonfile_hd = json.load(dbfile_r_hd)
            jsonfile_hd['hd_width'] = self.hd_width
            jsonfile_hd['hd_height'] = self.hd_height
            if self.face_camera_name == self.hd_cream_name:
                self.face_width = self.cap1_3
                self.face_height = self.cap1_4
                jsonfile_hd['face_width'] = self.face_width
                jsonfile_hd['face_height'] = self.face_height
            if self.hd_cream_name == self.eye_camera_name:
                self.eye_width = self.cap1_3
                self.eye_height = self.cap1_4
                jsonfile_hd['eye_width'] = self.eye_width
                jsonfile_hd['eye_height'] = self.eye_height
                print('toooooo')
            with open("config/db.json", "w", encoding='UTF-8') as dbfile_hd:
                json.dump(jsonfile_hd, dbfile_hd)
            self.cap1.set(3, self.hd_width)
            self.cap1.set(4,self.hd_width)
            if self.face_camera_name == self.hd_cream_name and self.hd_cream_name == self.eye_camera_name:
                while self._win1_running:
                    ret, frame = self.cap1.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        self.original1_image.updateImage(frame)
                        self.eye_image.updateImage(frame)
                        self.original2_image.updateImage(frame)
            if self.hd_cream_name == self.face_camera_name and self.hd_cream_name != self.eye_camera_name:
                while self._win1_running:
                    ret, frame = self.cap1.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        self.original1_image.updateImage(frame)
                        self.original2_image.updateImage(frame)
            if self.hd_cream_name != self.face_camera_name and self.hd_cream_name == self.eye_camera_name:
                while self._win1_running:
                    ret, frame = self.cap1.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        self.original1_image.updateImage(frame)
                        self.eye_image.updateImage(frame)
            if self.hd_cream_name != self.face_camera_name and self.hd_cream_name != self.eye_camera_name:
                while self._win1_running:
                    ret, frame = self.cap1.read()
                    if ret:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        self.original1_image.updateImage(frame)
            self.original1_image.updateImage(img_no_camera)
            if self.face_camera_name == self.hd_cream_name:
                self.original2_image.updateImage(img_no_camera)
            if self.hd_cream_name == self.eye_camera_name:
                self.eye_image.updateImage(img_no_camera)
        else:
            self.original1_image.updateImage(img_no_camera)
    def win_2(self):
        if (self.face_camera != -1) and (self.face_camera_name != self.hd_cream_name):#脸部摄像头存在并且不和行为摄像头重合
            self._win2_running=True
            self.cap2 = 0
            self.cap2 = cv2.VideoCapture(self.face_camera,cv2.CAP_DSHOW)
            self.cap2.set(3,2560)
            self.cap2.set(4,1440)
            self.cap2.set(5,self.face_fps)
            print('cap2'+'_'+str(self.cap2.get(3)))
            print('cap2'+'_'+str(self.cap2.get(4)))
            print('cap2'+'_'+str(self.cap2.get(5)))
            self.cap2_3 = self.cap2.get(3)  # 宽
            self.cap2_4 = self.cap2.get(4)  # 高
            self.face_width = self.cap2_3
            self.face_height = self.cap2_4
            with open("config/db.json", "r", encoding='UTF-8') as dbfile_r_face:
                jsonfile_face = json.load(dbfile_r_face)
            jsonfile_face['face_width'] = self.face_width
            jsonfile_face['face_height'] = self.face_height
            if self.face_camera_name == self.eye_camera_name:
                self.eye_width = self.cap2_3
                self.eye_height = self.cap2_4
                jsonfile_face['eye_width'] = self.eye_width
                jsonfile_face['eye_height'] = self.eye_height
            with open("config/db.json", "w", encoding='UTF-8') as dbfile_face:
                json.dump(jsonfile_face, dbfile_face)
            self.cap2.set(3, self.face_width)
            self.cap2.set(4,self.face_width)
            if self.face_camera_name == self.eye_camera_name:
                while self._win2_running:
                    ret2,frame2 = self.cap2.read()
                    if ret2:
                        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                        self.original2_image.updateImage(frame2)
                        self.eye_image.updateImage(frame2)
            else:
                while self._win2_running:
                    ret2, frame2 = self.cap2.read()
                    if ret2:
                        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                        self.original2_image.updateImage(frame2)
            self.original2_image.updateImage(img_no_camera)
            if self.face_camera_name == self.eye_camera_name:
                self.eye_image.updateImage(img_no_camera)
        else:
            self.original2_image.updateImage(img_no_camera)
    def win_3(self):
        if (self.eye_camera != -1) and (self.eye_camera_name != self.face_camera_name) and (self.eye_camera_name != self.hd_cream_name):#不和脸部、行为重合
            self._win3_running=True
            self.cap3 = 0
            self.cap3 = cv2.VideoCapture(self.eye_camera,cv2.CAP_DSHOW)
            self.cap3.set(3,2560)
            self.cap3.set(4,1440)
            self.cap3.set(5,self.eye_fps)
            print('cap3'+'_'+str(self.cap3.get(3)))
            print('cap3'+'_'+str(self.cap3.get(4)))
            print('cap3'+'_'+str(self.cap3.get(5)))
            self.cap3_3 = self.cap3.get(3)  # 宽
            self.cap3_4 = self.cap3.get(4)  # 高
            self.eye_width = self.cap3_3
            self.eye_height = self.cap3_4
            with open("config/db.json", "r", encoding='UTF-8') as dbfile_r_eye:
                jsonfile_eye = json.load(dbfile_r_eye)
            jsonfile_eye['face_width'] = self.eye_width
            jsonfile_eye['face_height'] = self.eye_height
            with open("config/db.json", "w", encoding='UTF-8') as dbfile_eye:
                json.dump(jsonfile_eye, dbfile_eye)
            self.cap3.set(3, self.eye_width)
            self.cap3.set(4,self.eye_width)
            while self._win3_running:
                ret3, frame3 = self.cap3.read()
                if ret3:
                    frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
                    self.eye_image.updateImage(frame3)
            self.eye_image.updateImage(img_no_camera)
        else:
            self.eye_image.updateImage(img_no_camera)
    def save_hd_video(self):
        if self.hd_camera != -1:
            fn = self.lineEdit.text()
            name=self.save_path+"/behavior_" + fn + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + self.video_format
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(name, fourcc, int(self.hd_fps), (int(self.hd_width), int(self.hd_height)))
            while self._begin:
                ret,frame=self.cap1.read()
                out.write(frame)
    def save_face_video(self):
        if self.face_camera != -1:
            fn = self.lineEdit.text()
            name=self.save_path+"/face_" + fn + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + self.video_format
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(name, fourcc, int(self.face_fps), (int(self.face_width), int(self.face_height)))
            if self.face_camera_name != self.hd_cream_name:
                while self._begin:
                    ret,frame=self.cap2.read()
                    out.write(frame)
            else:
                while self._begin:
                    ret,frame=self.cap1.read()
                    out.write(frame)
    def save_eye_video(self):
        if self.eye_camera != -1:
            fn = self.lineEdit.text()
            name=self.save_path+"/eye_" + fn + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + self.video_format
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(name, fourcc, int(self.eye_fps), (int(self.eye_width), int(self.eye_height)))
            if (self.eye_camera_name != self.hd_cream_name) & (self.eye_camera_name != self.face_camera_name):
                while self._begin:
                    ret,frame=self.cap3.read()
                    out.write(frame)
            elif (self.eye_camera_name != self.hd_cream_name) & (self.eye_camera_name == self.face_camera_name):
                while self._begin:
                    ret,frame=self.cap2.read()
                    out.write(frame)
            else:
                while self._begin:
                    ret,frame=self.cap1.read()
                    out.write(frame)
    def win_4_upimage(self):
        if self.voice_index != -1:
            self.voice_image.updateImage(img_voice)
        else:
            pass
    def win_4(self):
        self._voice_get = True
        self._frames=[]
        p=pyaudio.PyAudio()
        print(self.voice_index)
        stream=p.open(format=self.FORMAT,
                      rate=self.RATE,
                      channels=self.CHANNELS,
                      input=True,
                      frames_per_buffer=self.CHUNK,
                      input_device_index=self.voice_index)
        while self._voice_get:
            data = stream.read(self.CHUNK)
            self._frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
    def voice_save(self):
        p = pyaudio.PyAudio()
        fn = self.lineEdit.text()
        name = self.save_path+"/vioce_" + fn + "_" + datetime.now().strftime('%Y%m%d%H%M%S') + self.voice_format
        wf = wave.open(name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        print("Saved")
    def updatemessage(self):
        # 只有在点击开始录制时才会显示该消息，点击进程结束时停止显示。
        with open("config/db.json", "r", encoding='UTF-8') as dbfile_r:
            jsonfile = json.load(dbfile_r)
        self.save_path = jsonfile['save_path']
        self.time_end = time.time()
        m, s = divmod(int(self.time_end-self.time_start), 60)
        h, m = divmod(m, 60)
        self.recording_time = str(h)+'时'+str(m)+'分'+str(s)+'秒'
        self.statusbar.showMessage('当前病人id：' + self.lineEdit.text() + '   保存位置：' + self.save_path + '   录制时间：' + self.recording_time)
        if self._start_running == True:
            self.qttimer.stop()
    def startRe(self):
        print(self.voice_index)
        if self._start_running:
            self._start_running =False
            self._begin = True
            with open("config/db.json", "r", encoding='UTF-8') as dbfile_r:
                jsonfile = json.load(dbfile_r)
            self.voice_format = jsonfile["voice_format"]
            self.video_format = jsonfile["video_format"]
            #需要显示的有：病人ID，当前保存路径，已经录制多长时间，在加一个录制中。
            #已录制多长时间需要动态显示，每秒更新一次状态栏，只在录制视频的时候显示。
            #什么情况下会录制视频？_begin == True ,上面写了，不等于-1就能录制视频。
            if self.voice_index != -1 or self.eye_camera != -1 or self.hd_camera != -1 or self.face_camera != -1:#self.voice_index！=-1，则一定会录制音频。如果有其他设备不为-1则会录制视频，只要有录制情况就显示该消息
                self.time_start = time.time()
                self.record_judge = True #表示是否在录制中。该变量只与qtimer有关，该变量为True则一定有QTimer（）,当然线程终止也会赋值为False，表示结束录制了。
                self.qttimer = QTimer()
                self.qttimer.start(200)
                self.qttimer.timeout.connect(self.updatemessage)
            threading._start_new_thread(self.save_hd_video, ())
            threading._start_new_thread(self.save_face_video, ())
            threading._start_new_thread(self.save_eye_video, ())
            if self.voice_index != -1:
                threading._start_new_thread(self.win_4, ())
        else:
            pass
    def endRe(self):
        if self._start_running==False:
            if self.record_judge == True:#只有点击
                self.qttimer.stop()
                self.record_judge = False
                self.statusbar.showMessage('录制结束，文件已保存至：' + self.save_path + ' 录制时长：' + self.recording_time)
            self._start_running=True
            self._begin =False
            if self.voice_index != -1:
                self._voice_get = False
                self.voice_save()
                self.statusbar.showMessage('录制结束，文件已保存至：'+self.save_path+' 录制时长：'+self.recording_time)
        else:
            pass
    def closeEvent(self,event):
        #关闭所有线程，防止不能退出
        #如果没有运行进程终止，则不能退出
        if self._init_running == False:
            QMessageBox.information(self,'警告','进程未中止，请中止进程再关闭窗口！')
            event.ignore()
        print('closeevent')
    def stop(self):
        if self.record_judge == True:
            QMessageBox.information(self,'警告','正在录制中，请结束录制后再点击停用视频设备！')
        else:
            self._win1_running = False
            self._win2_running = False
            self._win3_running = False
            self._init_running = True
            print('stop','所有通道均已断开')
            self.voice_image.updateImage(img_no_voice)
            self.statusbar.showMessage('所有通道均已断开')
    def f_p(self):
        #点进程终止的时候录音进程可能不会终止，而视频录制会结束，必须再点结束录制才能结束---------先不管它，假设先用不到它。--------还是先解决它吧。
        #进程中止前判断是否在录制中，若在录制中，需要点击录制结束
        if self.record_judge == True:
            QMessageBox.information(self,'警告','正在录制中，请结束录制后再点击进程中止！')
        else:
            self._win1_running = False
            self._win2_running = False
            self._win3_running = False
            self._init_running = True
            if self.record_judge == True:
                self._begin = False
                self._start_running = True
                self._voice_get = False
                self.voice_save()
                self.qttimer.stop()
                self.record_judge = False
            self._voice_get = True
            self._begin = False
            print('stop', '所有进程均已中止')
            self.statusbar.showMessage('所有进程均已中止')
            self.voice_image.updateImage(img_no_voice)
    def about(self):
        QMessageBox.about(self, "多通道音视频采集软件",
                          "<p>山东大学健康医疗大数据研究院")
    def updateImages(self):
        self.calculateProcessed()
        self.calculateOriginal()
    def createButtons(self):
        self.initButton.clicked.connect(self.initfrom)
        self.pushButton.clicked.connect(self.stop)
        self.shotButton.clicked.connect(self.f_p)
        self.actionAbout.triggered.connect(self.about)
        self.startButton.clicked.connect(self.startRe)
        self.endButton.clicked.connect(self.endRe)
        self.action12.triggered.connect(self.child_CameraVoice_setting) #子窗口配置摄像头和麦克风
        self.actionse.triggered.connect(self.Child_File_Setting)#选择文件路径
    def setBackground(self):
        cv_img_rgb = img_no_camera
        self.original1_image.updateImage(cv_img_rgb)
        self.original2_image.updateImage(cv_img_rgb)
        self.eye_image.updateImage(cv_img_rgb)
        self.voice_image.updateImage(img_no_voice)
