import os
import cv2
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    rotate = cv2.warpAffine(image, M, (nW, nH))
    cv2.imwrite(image_folder + '/' + str(angle) + '_' + file_name, rotate)


def crop_image(img, rows, cols, r, c):
    r = int(rows*r)
    c = int(cols*c)
    h = rows - r
    w = cols - c
    crop = img[c:c+w,r:r+h]
    cv2.imwrite(image_folder + '/' + 'Croped_' + '_' + file_name, crop)


def funcBrightContrast(bright, contrast, typeOp):
    effect = apply_brightness_contrast(img,bright,contrast)
    cv2.imwrite(image_folder + '/' + typeOp + 'BriCon_' + file_name, effect)
 

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)
 
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
 
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
 
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
 
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
        
    return buf
 

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


def blur_image(img):
    blur = cv2.blur(img, (15, 15))
    cv2.imwrite(image_folder + '/' + 'Blured_' + file_name, blur)


def flip_image(img):
    horizontal_img = cv2.flip(img, 1)
    cv2.imwrite(image_folder + '/' + 'Flipped_' + file_name, horizontal_img)


#Main
image_folder = 'Pat_to_image_folder'  
file_names = os.listdir(image_folder)
file_name = ''
image_name = ''

for file_name in file_names:
    if file_name[0] != '.':   
        dir_file = image_folder + '/' + file_name
        img = cv2.imread(dir_file) 
        rows, cols, ch = img.shape

        rotate_image(img, 90)
        crop_image(img, rows, cols, 0.1, 0.20) 
        funcBrightContrast(300, 150, 'In')          #Increase Brigth Contrast
        funcBrightContrast(180, 150, 'De')          #Decrease Brigth Contrast
        blur_image(img)
        flip_image(img)
