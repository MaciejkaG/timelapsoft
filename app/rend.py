import cv2
import os
from time import time, sleep
from tlsoft import base as tlb

conf = tlb.getConfig()
imgDir = tlb.joinWithScriptPath(f'frames')
videoPath = tlb.joinWithScriptPath(f'output/{round(time())}.mp4')

images = [img for img in os.listdir(imgDir) if img.endswith(".png")]
width, height = conf['rendering']['resolution'][0], conf['rendering']['resolution'][1]

video = cv2.VideoWriter(videoPath, 0, conf['rendering']['framesPerSecond'], (width, height))

for image in images:
    image = cv2.imread(os.path.join(imgDir, image))
    image = tlb.convertResolution(image, (width, height))
    video.write(image)


cv2.destroyAllWindows()
video.release()
