"""Streaming video with face recognition."""
# ----------------------------------------------
# --- Author         : Hani YOUSFI
# --- Mail           : haniyousfi@gmail.com
# --- Date           : 10th May 2018
# ----------------------------------------------

import cv2


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
# Iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None']


class VideoCamera(object):
    def __init__(self):
        # Capturing video from camera 0, if you face troubles, change the
        # camera index or use a saved video.
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 640)  # Set video widht
        self.video.set(4, 480)  # Set video height
        # If you're using a video.mp4, you must have this file in the folder
        # as the main.py and uncomment the following line
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # I'm using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        # Define min window size to be recognized as a face
        minW = 0.1*self.video.get(3)
        minH = 0.1*self.video.get(4)
        while True:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = \
                faceCascade.detectMultiScale(gray, scaleFactor=1.2,
                                             minNeighbors=5,
                                             minSize=(int(minW), int(minH)),)
            for(x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(image, str(id), (x+5, y-5),
                            font, 1, (255, 255, 255), 2)
                cv2.putText(image, str(confidence), (x+5, y+h-5),
                            font, 1, (255, 255, 0), 1)
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()
