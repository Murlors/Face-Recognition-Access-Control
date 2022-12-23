import logging

import cv2
import numpy as np
import torch
from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1
from torchvision import transforms

from SQL import store_face_image, store_face_recogonized_record

log = logging.getLogger('facenet')
log.setLevel(logging.ERROR)


class Facenet:
    def __init__(self):
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        print('Running on device: {}'.format(self.device))
        # 人脸检测模型
        self.mtcnn = MTCNN(
            image_size=160, margin=20, min_face_size=20,
            thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
            device=self.device
        ).eval()
        # 人脸识别模型
        self.resnet = InceptionResnetV1(pretrained='vggface2', device=self.device).eval().to(self.device)
        self.loader = transforms.Compose([transforms.ToTensor()])
        self.feature_lib = []
        self.featureLibID = []

    def get_features(self, image_data):
        # 计算人脸特征向量
        features = self.resnet(image_data).detach()
        return features

    def boxes_to_images(self, image_data, boxes, probs):
        # 人脸概率在0.5以上的保留
        return_images = [self.loader(image_data.crop(box).resize((160, 160)))
                         for box, prob in zip(boxes, probs)
                         if prob > 0.5]
        return torch.stack(return_images).to(self.device)

    def predict(self, image_data):
        # 人脸的位置坐标和概率
        boxes, probs = self.mtcnn.detect(image_data)
        if boxes is not None:  # 检测到人脸
            images = self.boxes_to_images(image_data, boxes, probs)
            # 计算人脸特征向量
            embeddings_features = self.get_features(images)
            return embeddings_features, images

    def face_recognize(self, features):
        if features:
            dists = [[(feature - feature_in_lib).norm().item()
                      for feature_in_lib in self.feature_lib]
                     for feature in features]
            # 求最小值，即为识别到的人脸
            recognized_face = np.argmin(dists, axis=1)
            IDs = []
            for i in range(len(recognized_face)):
                print(dists[i][recognized_face[i]], self.featureLibID[recognized_face[i]])
                if dists[i][recognized_face[i]] < 0.25:
                    result_id = self.featureLibID[recognized_face[i]]
                    IDs.append(result_id)
            return IDs

    def register_new_face(self, id, image_data, new_feature_vector):
        # 注册新的人脸
        self.featureLibID.append(id)
        self.feature_lib.append(new_feature_vector)
        store_face_image(id, image_data.numpy(), new_feature_vector)
        print(f"register: {id}")


if __name__ == '__main__':
    facenet = Facenet()
    frame = Image.open("3.png")
    framePil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    features, images = facenet.predict(framePil)
    IDs = facenet.face_recognize(features)
    for id, image_data in zip(IDs, images):
        store_face_recogonized_record(id, image_data.numpy(), door_id, direction)
