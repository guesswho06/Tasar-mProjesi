import os

import cv2
import camera

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
i = 0
directory_name = "images/ramazan"
image_dir = os.path.join(BASE_DIR,directory_name)
os.mkdir(image_dir)
while (True):
    camera, gri_form = Camera.camera()
    faces = face_cascade.detectMultiScale(gri_form, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        secilen_gri_bolge = gri_form[y:y + h, x:x + w]

        img_item = image_dir + "/my_image"+str(i)+".png"
        print(img_item)
        i+=1
        cv2.imwrite(img_item, secilen_gri_bolge)
        renk = (0, 0, 255)
        cizgi_kalinligi = 2
        x_bitis_kordinati = x + w
        y_bitis_kordinati = y + h
        cv2.rectangle(camera, (x, y), (x_bitis_kordinati, y_bitis_kordinati), renk, cizgi_kalinligi)

    cv2.imshow('Camera', camera)

    if (cv2.waitKey(20) == ord('q')) | (i == 10):
        break

Camera.cameraClose()