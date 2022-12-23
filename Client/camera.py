import cv2
from PIL import Image

# from Model.facenetModel import Facenet
# facenet = Facenet()
cap = cv2.VideoCapture(0)
while True:
    # 获取图像
    ret, frame = cap.read()
    if ret:
        # cv2获取的图像是BGR格式的，需要转换成RGB格式
        rgb_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # 减小图片大小加速传输
        small_frame = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)
        # TODO: 给服务器发送图片(small_frame)识别人脸，返回人脸信息(Name, Box)
        # features, boxes = facenet.predict(framePil)
        for i in range(len(boxes)):
            temp = abs(boxes[i][0] - boxes[i][2]) * abs(boxes[i][1] - boxes[i][3])
        # IDs = facenet.face_recognize(features)
        # Names = facenet.get_name(IDs)
        for i in range(len(boxes)):  # 画框
            cv2.rectangle(
                frame, (int(boxes[i][0]), int(boxes[i][1])), (int(boxes[i][2]), int(boxes[i][3])), (0, 0, 255), 2)
            cv2.putText(
                frame, Names[i], (int(boxes[i][0]), int(boxes[i][1])),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)
        # 显示图像
        cv2.imshow('frame', frame)

# 释放摄像头
cap.release()
cv2.destroyAllWindows()
