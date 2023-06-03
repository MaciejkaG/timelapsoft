import cv2
from time import sleep, time
from tlsoft import base as tlb

cam = cv2.VideoCapture(tlb.getConfig()['preparation']['openCVCameraIndex'])

print("Running!")

while True:
    result, image = cam.read()
    if result:
        conf = tlb.getConfig()
        cv2.imwrite(tlb.joinWithScriptPath(f'frames/{round(time())}.png'), image)
        sleep(conf['preparation']["frameSavingDelay"])
    else:
        sleep(10)

        
    
