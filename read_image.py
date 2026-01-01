import cv2

img = cv2.imread("test.jpg")

if img is None:
    print("Image not loaded.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
