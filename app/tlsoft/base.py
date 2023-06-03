import os
import json
from PIL import Image
import cv2
import numpy as np
import math

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getConfig():
    with open(os.path.join(__location__, '../config.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def joinWithScriptPath(filename : str):
    return os.path.join(__location__, '../'+filename)


def convertResolution(img, expectedSize : tuple):
    # Convert OpenCV array to PIL image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imPil = Image.fromarray(img)
    # Check whether the image is too big in any of the dimensions and downscale it properly preserving aspect ratio
    x, y = imPil.size
    xTooBig = x > expectedSize[0]
    yTooBig = y > expectedSize[1]
    if xTooBig or yTooBig:
        xScaleFactor = expectedSize[0] / x
        yScaleFactor = expectedSize[1] / y
        scaleFactor = min(xScaleFactor, yScaleFactor)
        imPil = imPil.resize((int(x * scaleFactor), int(y * scaleFactor)))
    x, y = imPil.size
    # Check if the image is too small in any of the dimensions and upscale it properly preserving aspect ratio
    xTooSmall = x < expectedSize[0]
    yTooSmall = y < expectedSize[1]
    if xTooSmall or yTooSmall:
        xScaleFactor = expectedSize[0] / x
        yScaleFactor = expectedSize[1] / y
        scaleFactor = min(xScaleFactor, yScaleFactor)
        imPil = imPil.resize((int(x * scaleFactor), int(y * scaleFactor)))
    x, y = imPil.size
    # Convert the image back into OpenCV array, convert RGB back to BGR and return the image
    newIm = Image.new('RGBA', (expectedSize[0], expectedSize[1]), (0, 0, 0, 0))
    newIm.paste(imPil, (int((expectedSize[0] - x) / 2), int((expectedSize[1] - y) / 2)))
    rgb = newIm.split()
    img = np.array(Image.merge("RGB", (rgb[2], rgb[1], rgb[0])))
    return img
