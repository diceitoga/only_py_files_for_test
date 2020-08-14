'''
 Now we need to take the static image and do the following: 
 step 1: connect call back functions step 
 2: adding functionality through 'event choices' 
 step 3: dragging the mouse for functionality ''
'''
import numpy as np
import cv2

#################################
######### Function ##############
#################################
# we will link the function to the image via 'MyFirstDynamic' as sort of the pointer #

def draw_circle(event, x, y, flags, param):     # by default all event based drawing takes these paramenters as default
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)  #cv2.circle(img,(x,y),circle = 100,color=(0,255,0),fill=-1)
#URL: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

######################################################################
#### below will connect the function to the image/'MyFirstDynamic' ###
######################################################################

cv2.namedWindow(winname = 'MyFirstDynamic') 
# namedWindow creates a function with specific parameters (this happens before imshow() typically)
cv2.setMouseCallback('MyFirstDynamic',draw_circle)
# setMouseCallback calls draw_circle() inside the setMouseCallBack function that is passed in, and transform to the image
# that is also passed in
# setMouseCallBack() function will pass a lot of things like 1. event, 2. (x,y), 3. flags, 4. param so that draw_circle()
# has all of the info it needs. 


################################################
######### showing the image with openCV ########
################################################
img = np.zeros((512,512,3), dtype = np.int8)
while True: 
    cv2.imshow('MyFirstDynamic', img)
    
    if cv2.waitKey(20)& 0xFF==27:
        break

cv2.destroyAllWindows()
    
