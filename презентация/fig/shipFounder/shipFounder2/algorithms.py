import cv2
import image
import numpy as np
import socket
import time

##TCP_IP = "192.168.1.101"
##TCP_PORT = 5005
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind((TCP_IP, TCP_PORT))


def threshold(img,threshold):
    _,thresh = cv2.threshold(img[:,:,2],threshold,255,cv2.THRESH_BINARY)
    return thresh


def shipFounder(img,threshold):
    
    
    radius = max(img.shape[0]/256+1,3)
    img = cv2.blur(img,(radius,radius))
    _,thresh = cv2.threshold(img[:,:,1],threshold,255,cv2.THRESH_BINARY)
    _,contours, hierarchy = cv2.findContours(
        thresh,
        cv2.RETR_CCOMP,
        cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        contours = sorted(contours, key=len,reverse=True)
        
        rect = cv2.minAreaRect(contours[0])
        box = np.int0(cv2.boxPoints(rect))
        
        cv2.drawContours(img,[box],0,(0,255,0),1)

        middle = (box[0]+box[2])/2
        cv2.circle(img, (middle[0],middle[1]), 2, (255,0,0),-1)
        cv2.drawContours(img,contours,-1,(0,0,255),1)

       
        mes=middle
##        s.listen(1)
##        conn, addr = s.accept()
        print(mes, rect[2])
##        data=np.array(mes[0],dtype=np.int32)
##        print('1')
##        x = data.tostring()
##        try:
##            conn.send(x)
##        except socket.error:
##            conn.close()
        
        
    return img


##obj = image.Image('test.jpg',True)
##obj.setAlgorithm(shipFounder,200)
##obj.run()
