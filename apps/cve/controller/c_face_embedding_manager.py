# 
import face_recognition
from apps.cve.model.m_face_embedding_manager import MFaceEmbeddingManager

class CFaceEmbeddingManager(object):
    def __init__(self):
        self.name = ''
        self.model = MFaceEmbeddingManager()

    def save_face_embedding(self, face_name, face_embedding):
        faces_file = './data/faces.txt'
        face_embedding_num = self.model.get_face_embedding_num()
