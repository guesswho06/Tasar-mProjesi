import cv2
import camera

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

while (True):
    cam, gri_form = camera.camera()
    faces = face_cascade.detectMultiScale(gri_form, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        secilen_gri_bolge = gri_form[y:y + h, x:x + w]

        img_item = "my_image.png"
        cv2.imwrite(img_item, secilen_gri_bolge)
        renk = (0, 0, 255)
        cizgi_kalinligi = 2
        x_bitis_kordinati = x + w
        y_bitis_kordinati = y + h
        cv2.rectangle(cam, (x, y), (x_bitis_kordinati, y_bitis_kordinati), renk, cizgi_kalinligi)

    cv2.imshow('Camera', cam)

    if cv2.waitKey(1) == ord('q'):
        break

camera.cameraClose()
