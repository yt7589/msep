#
import numpy as np
import unittest
from apps.cve.controller.c_face_embedding_manager import CFaceEmbeddingManager

# python -m unittest tests.apps.cve.controller.t_c_face_embedding_manager.TCFaceEmbeddingManager.test_save_face_embedding -v
class TCFaceEmbeddingManager(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_face_embedding(self):
        face_name = 'yt'
        face_embedding = np.array([[1, 2, 3, 4, 5, 6]])
        print('face_embedding: {0};'.format(face_embedding.shape))
        controller = CFaceEmbeddingManager()
        controller.save_face_embedding(face_name, face_embedding)
        self.assertEqual(1, 2)