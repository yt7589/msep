#
import numpy as np
import unittest
from apps.cve.controller.c_face_embedding_manager import CFaceEmbeddingManager

# python -m unittest -v tests.apps.cve.controller.t_c_face_embedding_manager.TCFaceEmbeddingManager.test_save_face_embedding
class TCFaceEmbeddingManager(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_face_embedding(self):
        face_name = '闫涛100'
        face_embedding = np.array([[1.0, 2, 3, 4, 5, 6, 7, 8]])
        controller = CFaceEmbeddingManager()
        controller.save_face_embedding(face_name)