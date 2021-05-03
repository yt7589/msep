# 

class MFaceEmbeddingManager(object):
    def __init__(self):
        self.name = 'apps.cve.model.MFaceEmbeddingManager'

    def get_face_embedding_num(self):
        embedding_num_file = './data/embeddings/embedding_num.txt'
        with open(embedding_num_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                embedding_num = int(row) + 1
        with open(embedding_num_file, 'w', encoding='utf-8') as fd:
            fd.write('{0}'.format(embedding_num))