import tensorflow as tf
model = tf.keras.models.load_model('model_cardboard.keras')
import cv2
import numpy as np

vs = cv2.VideoCapture(0)
vs.set(3, 640)  # Set width
vs.set(4, 680)  # Set height

while True:
    ret, frame = vs.read()
    frame = cv2.resize(frame, (100, 100))  # Resize to match model input size
    img_pred = frame
    img_pred = np.expand_dims(img_pred, axis=0)
    result = model.predict(img_pred)
    print(result)
    if result[0][0] > result[0][1] and result[0][0] > result[0][2]:
        prediction = "Cardboard"
    elif result[0][1] > result[0][0] and result[0][1] > result[0][2]:
        prediction = "Paperbag"
    else:
        prediction = "Empty"

    cv2.putText(frame, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()