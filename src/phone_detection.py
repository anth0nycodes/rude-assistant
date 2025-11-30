import os
import pyttsx3
import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from dotenv import load_dotenv
from insults import get_insult

load_dotenv()

# Create an ObjectDetector object.
OBJECT_MODEL_PATH = os.getenv("OBJECT_MODEL_PATH")

if OBJECT_MODEL_PATH is None:
    raise ValueError("MODEL_PATH environment variable is not set.")

base_options = python.BaseOptions(model_asset_path=OBJECT_MODEL_PATH)
options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.35)
detector = vision.ObjectDetector.create_from_options(options)

# Initialize TTS engine with custom settings
engine = pyttsx3.init()
engine.setProperty("rate", 175)  # Speed of speech (default is ~200)


def detect_phone(frame):
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    detection_result = detector.detect(image)

    annotated_image = visualize_phone(rgb_frame, detection_result)

    bgr_annotated_image = cv.cvtColor(annotated_image, cv.COLOR_RGB2BGR)
    cv.imshow("Cellphone Detection", bgr_annotated_image)


def visualize_phone(image_copy, detection_result):
    """
    Detection result sample data

    DetectionResult(
        detections=[
            Detection(
                bounding_box=BoundingBox(origin_x=260, origin_y=65, width=1399, height=1028),
                categories=[
                    Category(index=None, score=0.91796875, display_name=None, category_name='person')
                ],
                keypoints=[]
            )
        ]
    )
    """

    for detection in detection_result.detections:
        bbox = detection.bounding_box
        x = bbox.origin_x  # left edge of the bounding box
        y = bbox.origin_y  # top edge of the bounding box
        w = bbox.width  # width of the bounding box / how far right it travels
        h = bbox.height  # height of the bounding box / how far down it travels
        x2 = x + w  # how far right it travels from the left edge
        y2 = y + h  # how far down it travels from the top edge
        green = (0, 255, 0)
        border_thickness = 2
        text_thickness = 2

        category = detection.categories[0].category_name
        score = round(detection.categories[0].score * 100, 2)

        if category == "cell phone":
            label = f"{category}: {score}%"

            cv.rectangle(image_copy, (x, y), (x2, y2), green, border_thickness)
            cv.putText(
                image_copy,
                label,
                (x, y - 10),  # Position: above the box (10 pixels up from top edge)
                cv.FONT_HERSHEY_SIMPLEX,
                1,  # Font scale (size)
                green,
                text_thickness,
            )

            insult = get_insult()
            print(
                f"Generated insult: {insult}"
            )  # debug print to see what was generated
            engine.say(insult)
            engine.runAndWait()

    return image_copy
