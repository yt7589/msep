#
import cv2

class FaceTrainer(object):
    def __init__(self):
        self.name = 'apps.cve.FaceTrainer'

    def train(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("Webcam Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()