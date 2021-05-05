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
        known_face_names, known_face_encodings = model.load_dataset()
        for name, code in zip(known_face_names, known_face_encodings):
            print('name: {0}, code: {1};'.format(name, type(code)))
        self.assertEqual(1, 1)