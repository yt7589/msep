#
import numpy as np
import cv2
import face_recognition
from apps.cve.model.m_face_recognizer import MFaceRecognizer

class CFaceRecognizer(object):
    def __init__(self):
        self.name = 'apps.cve.controller.CFaceRecognizer'
        self.model = MFaceRecognizer()
    
    def startup(self, args={}):
        print('人脸识别程序 v0.0.1')
        known_face_names, known_face_encodings = self.model.load_dataset()
        # 视频帧中所有人脸位置、编码和对应的姓名
        all_face_locations = []
        all_face_encodings = []
        all_face_names = []
        # 启动摄像头
        webcam_video_stream = cv2.VideoCapture(0)
        #loop through every frame in the video
        while True:
            #get the current frame from the video stream as an image
            ret,current_frame = webcam_video_stream.read()
            #resize the current frame to 1/4 size to proces faster
            current_frame_small = cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
            #detect all faces in the image
            #arguments are image,no_of_times_to_upsample, model
            all_face_locations = face_recognition.face_locations(current_frame_small,number_of_times_to_upsample=1,model='hog')
            
            #detect face encodings for all the faces detected
            all_face_encodings = face_recognition.face_encodings(current_frame_small,all_face_locations)


            #looping through the face locations and the face embeddings
            for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):
                #splitting the tuple to get the four position values of current face
                top_pos,right_pos,bottom_pos,left_pos = current_face_location
                
                #change the position maginitude to fit the actual size video frame
                top_pos = top_pos*4
                right_pos = right_pos*4
                bottom_pos = bottom_pos*4
                left_pos = left_pos*4
                
                #find all the matches and get the list of matches
                all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)
            
                #string to hold the label
                name_of_person = 'Unknown face'
                
                #check if the all_matches have at least one item
                #if yes, get the index number of face that is located in the first index of all_matches
                #get the name corresponding to the index number and save it in name_of_person
                if True in all_matches:
                    first_match_index = all_matches.index(True)
                    name_of_person = known_face_names[first_match_index]
                
                #draw rectangle around the face    
                cv2.rectangle(current_frame,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)
                
                #display the name as text in the image
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(current_frame, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)
            
            #display the video
            cv2.imshow("Webcam Video",current_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        #release the stream and cam
        #close all opencv windows open
        webcam_video_stream.release()
        cv2.destroyAllWindows()       