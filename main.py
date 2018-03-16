import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("0.png", 0)
img2 = cv2.imread("0.png")
template = cv2.imread('person_0.png', 0)
w, h = template.shape[::-1]

method_str = 'cv2.TM_SQDIFF'
method = eval(method_str)


res = cv2.matchTemplate(img, template ,method)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
print "If there was a birth every 7 seconds, ther"

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.circle(img2, top_left, 6, 255, -1)
cv2.rectangle(img2, top_left, bottom_right, 255, 2)

plt.subplot(121), plt.imshow(res, cmap='gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])


plt.subplot(122), plt.imshow(img2, cmap='gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()