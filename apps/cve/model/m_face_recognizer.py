#
import numpy as np
import face_recognition

class MFaceRecognizer(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceRecognizer'

    def load_dataset(self):
        known_face_names = []
        known_face_name_jpgs = []
        known_face_encodings = []
        ds_file = './data/embeddings/face_embedding.txt'
        with open(ds_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                row = row.strip()
                arrs = row.split(',')
                face_name = arrs[0]
                face_embedding_npy = arrs[1]
                face_jpg = arrs[2]
                face_name_jpg_file = arrs[3]
                face_name_jpg = face_recognition.load_image_file(face_name_jpg_file)
                print('face_name_jpg: {0};'.format(face_name_jpg.shape))
                known_face_names.append(face_name)
                known_face_name_jpgs.append(face_name_jpg)
                known_face_encodings.append(np.load(face_embedding_npy))
        return known_face_names, known_face_name_jpgs, known_face_encodings