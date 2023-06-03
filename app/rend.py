import cv2
import os
from time import time, sleep
from tlsoft import base as tlb
from datetime import timedelta

conf = tlb.getConfig()
imgDir = tlb.joinWithScriptPath(f'frames')
fname = f"{round(time())}.mp4"
videoPath = tlb.joinWithScriptPath(f'output/{fname}')

images = [img for img in os.listdir(imgDir) if img.endswith(".png")]
width, height = conf['rendering']['resolution'][0], conf['rendering']['resolution'][1]

video = cv2.VideoWriter(videoPath, 0, conf['rendering']['framesPerSecond'], (width, height))

startTs = time()
doneImages = 0
for image in images:
    image = cv2.imread(os.path.join(imgDir, image))
    image = tlb.convertResolution(image, (width, height))
    video.write(image)
    doneImages += 1
    print(f"Rendering: {doneImages} / {len(images)} frames ({round(doneImages/len(images)*100)}%)")

frames = len(images)
fps = conf['rendering']['framesPerSecond']
videoDuration = timedelta(seconds=round(frames / fps))

print(f"Successfully rendered a {videoDuration} long video consisitng of {frames} frames in {width}x{height} {conf['rendering']['framesPerSecond']}\nRendering took {timedelta(seconds=round(time()-startTs))} and the file was saved under the name '{fname}'")

cv2.destroyAllWindows()
video.release()
