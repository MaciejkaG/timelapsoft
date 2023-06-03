import cv2
from time import sleep, time
from tlsoft import base as tlb

cam = cv2.VideoCapture(tlb.getConfig()['preparation']['openCVCameraIndex'])

while True:
    result, image = cam.read()
    if result:
        conf = tlb.getConfig()
        print(f"{tlb.joinWithScriptPath(f'frames/{round(time())}.png')}")
        cv2.imwrite(tlb.joinWithScriptPath(f'frames/{round(time())}.png'), image)
        print("image written!")
        sleep(conf['preparation']["frameSavingDelay"])
    else:
        sleep(10)

        
    
