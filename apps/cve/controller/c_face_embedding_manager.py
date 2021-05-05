# 
import numpy as np
import cv2
import face_recognition
from PIL import Image,ImageFont,ImageDraw
import face_recognition
from apps.cve.model.m_face_embedding_manager import MFaceEmbeddingManager
from apps.cve.view.v_face_embedding_manager import VFaceEmbeddingManager

class CFaceEmbeddingManager(object):
    def __init__(self):
        self.name = ''
        self.model = MFaceEmbeddingManager()

    def prepare_data(self):
        yt_image = face_recognition.load_image_file('images/samples/yt1.jpg')
        yt_face_encodings = face_recognition.face_encodings(yt_image)[0]        

    def startup(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame_small = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            #detect all faces in the image
            #arguments are image,no_of_times_to_upsample, model
            all_face_locations = face_recognition.face_locations(frame_small,number_of_times_to_upsample=2,model='hog')
            for index,current_face_location in enumerate(all_face_locations):
                #splitting the tuple to get the four position values of current face
                top_pos,right_pos,bottom_pos,left_pos = current_face_location
                #change the position maginitude to fit the actual size video frame
                top_pos = top_pos*4
                right_pos = right_pos*4
                bottom_pos = bottom_pos*4
                left_pos = left_pos*4
                # enlarge the cripping box
                left_pos -= int((right_pos - left_pos)*0.25)
                if left_pos<0:
                    left_pos = 0
                top_pos -= int((bottom_pos - top_pos) * 0.6)
                if top_pos < 0:
                    top_pos = 0
                right_pos += int((right_pos - left_pos) * 0.3)
                if right_pos > frame.shape[1]:
                    right_pos = frame.shape[1]
                bottom_pos += int((bottom_pos - top_pos) * 0.2)
                if bottom_pos > frame.shape[0]:
                    bottom_pos = frame.shape[0]
                #printing the location of current face
                #print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
                current_face_image = frame[top_pos:bottom_pos,left_pos:right_pos]
                if cv2.waitKey(1) & 0xFF == ord('a'):
                    face_embedding = np.array(face_recognition.face_encodings(current_face_image))
                    self.model.face_embedding = np.reshape(face_embedding, (face_embedding.shape[1],))
                    self.model.face_data = current_face_image
                    view = VFaceEmbeddingManager(self)
                    view.show_add_face()
                    #im = Image.fromarray(current_face_image)
                    #im.save("yt2.jpg")
                #draw rectangle around the face detected
                cv2.rectangle(frame,(left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),2)
            cv2.imshow("Webcam Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def save_face_embedding(self, face_name):
        '''
        由界面的保存按钮触发，保存当前人脸图片
        '''
        face_embedding = self.model.face_embedding
        fe_file = self.model.save_face_embedding_npy(face_embedding)
        face_jpg = self.model.save_face_jpg(self.model.face_data)
        face_embedding_num = self.model.face_embedding_num
        face_name_jpg = self.model.text_to_jpg(face_name, face_embedding_num)
        self.model.save_face_embedding(face_name, fe_file, face_jpg, face_name_jpg)