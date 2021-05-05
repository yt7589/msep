#

class MFaceRecognizer(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceRecognizer'

    def load_dataset(self):
        ds_file = './data/embeddings/face_embedding.txt'
        with open(ds_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                arrs = row.split(',')
                face_name = arrs[0]
                face_embedding_npy = arrs[1]
                face_jpg = arrs[2]
                print('姓名：{0}; 文件：{1}; 图像：{2};'.format(face_name, face_embedding_npy, face_jpg))