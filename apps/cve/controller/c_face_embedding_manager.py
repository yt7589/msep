# 

class CFaceEmbeddingManager(object):
    def __init__(self):
        self.name = ''

    def save_face_embedding(self, face_name, face_embedding):
        faces_file = './data/faces.txt'
        embedding_num_file = './data/embeddings/embedding_num.txt'
        with open(embedding_num_file, 'r', encoding='utf-8') as fd:
            for row in fd:
                embedding_num = int(row) + 1
        print('embedding_num={0};'.format(embedding_num))
        #embedding_file = './data/embeddings/'