import time
import cv2

from tensorflow.keras import Input, Model
from darknet import darknet_base
from predict import predict, predict_with_yolo_head


INCLUDE_YOLO_HEAD = False

stream = cv2.VideoCapture(1)

inputs = Input(shape=(None, None, 3))
outputs, config = darknet_base(inputs, include_yolo_head=INCLUDE_YOLO_HEAD)
model = Model(inputs, outputs)

while True:
    # Capture frame-by-frame
    grabbed, image = stream.read()
    height , width , layers =  image.shape
    new_h=height/2
    new_w=width/2
    frame = cv2.resize(image, (100, 100))

    if not grabbed:
        break

    # Run detection
    start = time.time()

    if INCLUDE_YOLO_HEAD:
        output_image = predict(model, frame, config)
    else:
        output_image = predict_with_yolo_head(model, frame, config, confidence=0.3, iou_threshold=0.4)

    # output_image = frame
    end = time.time()
    # print("Inference time: {:.2f}s".format(end - start))

    # Display the resulting frame
    cv2.imshow('', output_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# When everything done, release the capture
stream.release()
cv2.destroyAllWindows()
