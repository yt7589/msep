#
import cv2

class CveApp(object):
    def __init__(self):
        self.name = 'apps.cve.CveApp'

    def startup(self, args={}):
        print('startup...')
        cap = cv2.VideoCapture('rtsp://192.168.2.68:8554/v7.mkv')
        while cap.isOpened():
            rst, frame = cap.read()
            cv2.imshow('msep', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()