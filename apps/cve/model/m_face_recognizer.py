#
import numpy as np

class MFaceRecognizer(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceRecognizer'

    def load_dataset(self):
        known_face_names = []
        known_face_encodings = []
        ds_file = './data/embeddings/face_embedding.txt'
        with open(ds_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                arrs = row.split(',')
                face_name = arrs[0]
                face_embedding_npy = arrs[1]
                face_jpg = arrs[2]
                known_face_names.append(face_name)
                known_face_encodings.append(np.load(face_embedding_npy))
        return known_face_names, known_face_encodings