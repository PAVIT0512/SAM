import tensorflow as tf
model = tf.keras.models.load_model('./ModelLabelDetector/model.keras')
import cv2
import numpy as np

def labelcamera(camera_no):
    vs = cv2.VideoCapture(camera_no)
    vs.set(3, 640)  # Set width
    vs.set(4, 680)  # Set height

    while True:
        ret, frame = vs.read()
        frame = cv2.resize(frame, (100, 100))  # Resize to match model input size
        img_pred = frame
        img_pred = np.expand_dims(img_pred, axis=0)
        result = model.predict(img_pred)

        if result[0][0] > result[0][1]:
            prediction = "label"
            return 1
        else:
            prediction = "no label"
            return 0

        cv2.putText(frame, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Prediction", frame)
        return prediction

    vs.release()
    cv2.destroyAllWindows()