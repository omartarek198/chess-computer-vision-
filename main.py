import os

import cv2

index = 1
for filename in os.listdir("images"):
    img = cv2.imread("images/"+filename )
    # cv2.rectangle(img, (270, 244), (276+630, 244+630), (0, 255, 0), 3)

    cv2.imshow("boards",img)
    print (img.shape)
    # 285-244
    cropped_image = img[244 :244+630, 270:276+630]
    cv2.imwrite(str (index)+".jpg", cropped_image)

    cv2.waitKey(0)

    index+=1
    print(filename)
