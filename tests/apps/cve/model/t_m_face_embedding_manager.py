#
import numpy as np
import unittest
from apps.cve.model.m_face_embedding_manager import MFaceEmbeddingManager

class TMFaceEmbeddingManager(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_face_embedding_num(self):
        mngr = MFaceEmbeddingManager()
        mngr.get_face_embedding_num()
        self.assertEqual(1, 1)

    def test_save_face_embedding_npy(self):
        face_embedding = np.array([[1, 2.0, 3, 4, 5, 6]])
        model = MFaceEmbeddingManager()
        fe_file = model.save_face_embedding_npy(face_embedding)
        self.assertEqual(1, 1)
        print(f'npy:{fe_file};')

    def test_save_face_embedding(self):
        model = MFaceEmbeddingManager()
        face_name = '闫涛003'
        fe_file = 'fe_000121.npy'
        model.save_face_embedding(face_name, fe_file)

    def test_save_face_image_data(self):
        model = MFaceEmbeddingManager()
        face_name = '莫迪'
        face_image = './data/images_org/modi.jpg'
        model.save_face_image_data(face_name, face_image)
        face_name = '教师'
        face_image = './data/images_org/abhi.jpg'
        model.save_face_image_data(face_name, face_image)
        face_name = '川普'
        face_image = './data/images_org/trump.jpg'
        model.save_face_image_data(face_name, face_image)

        t_file = './data/embeddings/fe_000001.npy'
        a1 = np.load(t_file)
        print('a1: {0}; {1};'.format(type(a1), a1.shape))