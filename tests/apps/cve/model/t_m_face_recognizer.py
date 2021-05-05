#
import unittest
from apps.cve.model.m_face_recognizer import MFaceRecognizer

class TMFaceRecognizer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_dataset(self):
        model = MFaceRecognizer()
        model.load_dataset()
        self.assertEqual(1, 1)