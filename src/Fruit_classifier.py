import cv2
import numpy as np
from tensorflow.keras.models import load_model #type: ignore

def classify_image():
    model = load_model("Trained_model/model.h5")
    categories = ['Manzana', 'Platano']
    
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.resize(frame, (100, 100))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)[0]
        label = categories[np.argmax(prediction)]
        confidence = np.max(prediction)

        cv2.putText(frame, f"{label} ({confidence:.2f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.imshow("Clasificador de Frutas", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

