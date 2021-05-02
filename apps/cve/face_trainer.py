#
import cv2
import face_recognition

class FaceTrainer(object):
    def __init__(self):
        self.name = 'apps.cve.FaceTrainer'

    def train(self):
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
                #printing the location of current face
                print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
                current_face_image = frame[top_pos:bottom_pos,left_pos:right_pos]
                #draw rectangle around the face detected
                cv2.rectangle(frame,(left_pos,top_pos),(right_pos,bottom_pos),(0,0,255),2)





            cv2.imshow("Webcam Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()