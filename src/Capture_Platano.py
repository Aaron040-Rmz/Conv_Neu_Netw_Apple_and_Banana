import cv2
import os

def capture_images(folder="dataset/Platano", prefix="P"):
    os.makedirs(folder, exist_ok=True)
    cap = cv2.VideoCapture(0)
    count = 1

    while count <= 100:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Captura - Plátano (presiona "s" para guardar)', frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            filename = os.path.join(folder, f"{prefix}_{count:02d}.jpg")
            cv2.imwrite(filename, frame)
            print(f"[✔] Imagen guardada: {filename}")
            count += 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

