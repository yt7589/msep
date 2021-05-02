# 
import tkinter as tk
from tkinter import ttk


class VFaceEmbeddingManager(object):
    def __init__(self, controller, face_embedding):
        self.name = 'apps.cve.VFaceEmbeddingManager'
        self.controller = controller
        self.face_embedding = face_embedding

    def save_face(self, *args):
        face_name = self.face_name.get()
        print('保存姓名：{0};'.format(face_name))

    def show_add_face(self):
        root = tk.Tk()
        root.title('添加人脸')
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        # 人脸姓名
        self.face_name = tk.StringVar()
        self.face_name_entry = ttk.Entry(mainframe, width=7, textvariable=self.face_name)
        self.face_name_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        ttk.Label(mainframe, text='姓名').grid(column=1, row=1, sticky=tk.W)
        #
        ttk.Button(mainframe, text="保存", command=self.save_face).grid(column=3, row=3, sticky=tk.W)
        root.mainloop()