
import cv2
import numpy as np

image = cv2.imread('Images/099982.jpg')

face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

def get_color_name(color_value):
    if color_value < 20:
        return "Nero"
    elif color_value < 60:
        return "Marrone scuro"
    elif color_value < 110:
        return "Marrone"
    elif color_value < 160:
        return "Castano"
    elif color_value < 190:
        return "Biondo scuro"
    elif color_value < 220:
        return "Biondo"
    elif color_value < 240:
        return "Biondo chiaro"
    else:
        return "Biondo platino"

for (x, y, w, h) in faces:
    face = image[y:y+h, x:x+w]
    
    # Calcola il colore dei capelli
    hair_color = np.mean(face[:, :, 2])
    
    # Calcola il colore degli occhi
    eye_roi = face[int(h/2):h, :]
    eye_color = np.mean(eye_roi)
    
    # Calcola il colore della pelle
    skin_roi = face[int(h/2):h, int(w/4):int(3*w/4)]
    skin_color = np.mean(skin_roi)
    
    # Stampa i risultati
    print("Colore dei capelli: ", get_color_name(int(hair_color)))
    print("Colore degli occhi: ", get_color_name(int(eye_color)))
