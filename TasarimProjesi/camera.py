import cv2 as cv

cap = cv.VideoCapture(0)

def camera():
    if not cap.isOpened():
        print("Kamera açılamadı")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Kamera okunamadı")
        exit()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return frame, gray

def cameraClose():
    cap.release()
    cv.destroyAllWindows()
