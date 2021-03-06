# 
import numpy as np
import cv2
import face_recognition
from PIL import Image,ImageFont,ImageDraw

class MFaceEmbeddingManager(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceEmbeddingManager'
        self.face_embedding = None
        self.face_data = None # 图像数据的数组形式
        self.face_embedding_num = -1

    def get_face_embedding_num(self):
        '''
        获取自增的人脸特征向量文件编号
        '''
        embedding_num_file = './data/embeddings/embedding_num.txt'
        with open(embedding_num_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                embedding_num = int(row) + 1
        with open(embedding_num_file, 'w', encoding='utf-8') as fd:
            fd.write('{0}'.format(embedding_num))
        self.face_embedding_num = embedding_num
        return embedding_num

    def save_face_jpg(self, face_data):
        face_jpg = './data/images/img_{0:06d}.jpg'.format(self.face_embedding_num)
        cv2.imwrite(face_jpg, face_data)
        return face_jpg

    def save_face_embedding_npy(self, face_embedding):
        '''
        将人脸特征向量保存到npy文件中
        '''
        face_embedding_num = self.get_face_embedding_num()
        fe_file = './data/embeddings/fe_{0:06d}.npy'.format(face_embedding_num)
        np.save(fe_file, face_embedding)
        return fe_file

    def save_face_embedding(self, face_name, fe_file, face_jpg, face_name_jpg):
        '''
        将人脸姓名和对应的特征向量文件对应关系保存到文件中
        '''
        face_embedding_file = './data/embeddings/face_embedding.txt'
        with open(face_embedding_file, 'a', encoding='utf-8') as fd:
            fd.write('{0},{1},{2},{3}\n'.format(face_name, fe_file, face_jpg, face_name_jpg))

    def save_face_image_data(self, face_name, face_image_file):
        '''
        保存人脸照片数据
        '''
        #face_embedding_num = self.get_face_embedding_num()
        face_image = face_recognition.load_image_file(face_image_file)
        face_embedding = face_recognition.face_encodings(face_image)[0]
        print('face_embedding: {0};'.format(face_embedding.shape))
        fe_file = self.save_face_embedding_npy(face_embedding)
        face_name_jpg = self.text_to_jpg(face_name, self.face_embedding_num)
        self.save_face_embedding(face_name, fe_file, face_image_file, face_name_jpg)

    
    def text_to_jpg(self, text, face_embedding_num):
        '''
        将中文变为白色背景黑色的JPG图片，用于解决OpenCV不支持中文叠加的缺陷
        '''
        pil_image = im = Image.new("RGB", (100, 25), (255, 255, 255))
        pil_draw = ImageDraw.Draw(pil_image)
        font = ImageFont.truetype('./data/fonts/simsun.ttc', 16)
        pil_draw.text((10, 5), text, font=font, fill="#000000")
        #pil_image.show()
        face_name_jpg = './data/images/u_{0:06d}.jpg'.format(face_embedding_num)
        pil_image.save(face_name_jpg)
        return face_name_jpg