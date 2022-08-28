# encoding:utf-8
import cv2
import numpy as np



def cut_face(filename):
    face_cascade = cv2.CascadeClassifier("/app/bustag/app/haarcascade_frontalface_alt2.xml")
    eye_cascade = cv2.CascadeClassifier('/app/bustag/app/haarcascade_eye.xml')
    # 读取图像
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 检测脸部
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    print('Detected ', len(faces), " face")
    if len(faces) == 0:
        retval = cv2.imwrite("222.png", img)

        return
    else:
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y: y + h, x: x + w]
            roi_color = img[y: y + h, x: x + w]
            cut_img = img[y: y + h, x: x + w]
            retval = cv2.imwrite("222.png", cut_img)
        # 运行之前，检查cascade文件路径是否在相应的目录下

        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return


