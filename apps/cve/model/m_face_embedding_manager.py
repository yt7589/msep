# 
import numpy as np

class MFaceEmbeddingManager(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceEmbeddingManager'

    def get_face_embedding_num(self):
        embedding_num_file = './data/embeddings/embedding_num.txt'
        with open(embedding_num_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                embedding_num = int(row) + 1
        with open(embedding_num_file, 'w', encoding='utf-8') as fd:
            fd.write('{0}'.format(embedding_num))
        return embedding_num

    def save_face_embedding_npy(self, face_embedding):
        face_embedding_num = self.get_face_embedding_num()
        fe_file = './data/embeddings/fe_{0:06d}.npy'.format(face_embedding_num)
        np.save(fe_file, face_embedding_num)
        return fe_file

    def save_face_embedding(self, face_name, face_embedding_num):
        face_embedding_file = './data/embeddings/face_embedding.txt'
        fe_file = 'fe_{0:6d}.npy'.format(face_embedding_num)
        with oepn(face_embedding_file, 'w', encoding='utf-8') as fd:
            fd.write('{0},{1}'.format(face_name, fe_file))