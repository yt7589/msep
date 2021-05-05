# 
import numpy as np
import cv2
import face_recognition

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
        np.save(fe_file, face_embedding_num)
        return fe_file

    def save_face_embedding(self, face_name, fe_file, face_jpg):
        '''
        将人脸姓名和对应的特征向量文件对应关系保存到文件中
        '''
        face_embedding_file = './data/embeddings/face_embedding.txt'
        with open(face_embedding_file, 'a', encoding='utf-8') as fd:
            fd.write('{0},{1},{2}\n'.format(face_name, fe_file, face_jpg))

    def save_face_image_data(self, face_name, face_image_file):
        '''
        保存人脸照片数据
        '''
        #face_embedding_num = self.get_face_embedding_num()
        face_image = face_recognition.load_image_file(face_image_file)
        face_embedding = face_recognition.face_encodings(face_image)[0]
        fe_file = self.save_face_embedding_npy(face_embedding)
        self.save_face_embedding(face_name, fe_file, face_image_file)