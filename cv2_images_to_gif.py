from pathlib import Path

import cv2
import numpy as np
from PIL import Image


def cv2_images_to_animation_gif(imgs, output_path):
    pil_imgs = [Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) for img in imgs]
    pil_imgs[0].save(output_path, save_all=True, append_images=pil_imgs[1:], duration=500, disposal=2)


def cv2_images_to_animation_gif_with_param(imgs, output_path, param_name, params):
    new_imgs = []
    for img, param in zip(imgs, params):
        h, w = img.shape[:2]
        new_h = h + 15
        new_img = np.full((new_h, w, 3), 255, dtype=np.uint8)
        new_img[:h, :] = img

        cv2.putText(new_img, f"{param_name}: {param}", (5, new_h - 5), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
        new_imgs.append(new_img)
    cv2_images_to_animation_gif(new_imgs, output_path)


def main():
    file_paths = list(Path("sample/parsed").glob("*.jpg"))
    file_paths.sort()
    imgs = [cv2.imread(str(path)) for path in file_paths]
    output_path = "sample/marged/marged.gif"
    param_name = "name"
    file_names = [p.name for p in file_paths]
    cv2_images_to_animation_gif_with_param(imgs, output_path, param_name, file_names)

    output_path = "sample/marged/reverse_marged.gif"
    imgs.reverse()
    file_names.reverse()
    cv2_images_to_animation_gif_with_param(imgs, output_path, param_name, file_names)


if __name__ == "__main__":
    main()
