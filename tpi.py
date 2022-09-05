import cv2

def getDotCount(img):
    th, threshed = cv2.threshold(img, 255, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    return len(cnts)

def getAuthenticCount(img,t):
    i=0
    weft=img[0:i]
    weft_count = getDotCount(weft)
    while(weft_count<t):
        i=i+1
        weft=img[0:i]
        weft_count = getDotCount(weft)
    return weft_count,weft

def countDots(img,t_wrap=60,t_weft=70):

    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(gry, 255, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = cv2.dilate(img, None, iterations=1)
    wrap_count,wrap=getAuthenticCount(img,t_wrap)
    
    image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    
    weft_count,weft=getAuthenticCount(image,t_weft)

    map={'wrap':wrap_count,'weft':weft_count,'total':wrap_count+weft_count}
    return map