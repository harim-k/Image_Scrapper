import pytesseract
import cv2





for i in range(1,11):
	img = cv2.imread(f'{i}.jpg')

	print(pytesseract.image_to_string(img))

	with open(f'{i}.txt', 'wb') as fw:
		fw.write(pytesseract.image_to_string(img).encode())
