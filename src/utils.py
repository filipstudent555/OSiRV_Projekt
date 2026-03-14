import cv2 as cv
import numpy as np


def load_image(path):
    image = cv.imread(path)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image


def save_image(image_np, output_path):
    image_bgr = cv.cvtColor(image_np, cv.COLOR_RGB2BGR)
    cv.imwrite(output_path, image_bgr)