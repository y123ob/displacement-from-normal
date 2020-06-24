import cv2
import numpy as np

#load image
image_name = 'displacemap'
#image_name = 'depthmappppppppppppp'
img = cv2.imread(image_name + '.exr' ,cv2.IMREAD_UNCHANGED)

maxi = np.amax(img)
mini = np.amin(img)
print(maxi, mini)
maxi = 0.01
mini = -0.01

def f2uc(x):
    return int(255 * x)

print(img[1400][1600])


img2 = 255 * (img - mini) / (maxi - mini)
img2 = img2.astype(int)


print(img2[1400][1600])

#cv2.imshow('img',img2)
cv2.imwrite(image_name + '_normalize.bmp',img2)
#cv2.waitKey(0)

del img