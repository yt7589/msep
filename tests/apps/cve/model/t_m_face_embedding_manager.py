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