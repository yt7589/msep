#
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