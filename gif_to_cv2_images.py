import cv2
import numpy as np
from PIL import Image, ImageSequence


def gif_to_cv2_image(file_path):
    cap = cv2.VideoCapture(file_path)

    flames = []

    while True:
        read_success, flame = cap.read()
        if not read_success:
            break

        flames.append(flame)

    return flames


def gif_to_cv2_image_by_pillow(file_path):
    img = Image.open(file_path)
    frames = [frame.convert("RGB") for frame in ImageSequence.Iterator(img)]
    images = [cv2.cvtColor(np.asarray(f.convert("RGB")), cv2.COLOR_RGB2BGR) for f in frames]
    return images


def main():
    file_path = "sample/original/degu_gamma.gif"

    # images = gif_to_cv2_image_by_pillow(file_path)
    images = gif_to_cv2_image(file_path)  # faster

    for i, image in enumerate(images):
        cv2.imwrite(f"sample/parsed/parsed_{i:02}.jpg", image)


if __name__ == "__main__":
    main()
