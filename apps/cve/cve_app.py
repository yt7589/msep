#
import cv2
from apps.cve.face_detector import FaceDetector
from apps.cve.face_trainer import FaceTrainer

class CveApp(object):
    def __init__(self):
        self.name = 'apps.cve.CveApp'

    def startup(self, args={}):
        print('startup...')
        trainer = FaceTrainer()
        trainer.train()
        #self.tkinter1()

    def tkinter1(self):
        pass

    def t1(self):
        cap = cv2.VideoCapture('rtsp://192.168.2.68:8554/v7.mkv')
        while cap.isOpened():
            rst, frame = cap.read()
            cv2.imshow('msep', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()