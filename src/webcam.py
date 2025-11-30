import cv2 as cv
from phone_detection import detect_phone


def use_webcam():
    # Captures video from the default webcam (index 0)
    video_capture = cv.VideoCapture(0)

    # keeps a constant loop to read frames from the webcam
    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        # flips the frame horizontally for a mirror-like effect
        flipped_frame = cv.flip(frame, 1)

        detect_phone(flipped_frame)

        # waits for the 'q' key to be pressed to exit the loop
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()  # Releases the camera hardware so other apps can use your webcam afterward
    cv.destroyAllWindows()  # Closes every OpenCV window


def main():
    use_webcam()
