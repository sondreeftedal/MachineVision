import cv2
import pyzbar.pyzbar
import numpy as np
import qrcode
import tkinter

def decoder(code):
    bng_img = cv2.cvtColor(code,0)
    scannedCode = pyzbar.pyzbar.decode(bng_img)

    for i in scannedCode:
        points = i.polygon

        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(code, [pts], True, (0, 255, 0), 3)

        barcodeData = i.data.decode("utf-8")
        barcodeType = i.type
        print("Barcode: " + barcodeData + " | Type: " + barcodeType)

def encoder():
    selection = int(input("Select wanted action:" + "\n" + "1.Create barcode\n"+"2:Create QR-code\n"))
    if selection == 1:
        print("1")
    elif selection == 2:
        imagename = "test.png"
        data = input("Enter wanted data:" + "\n")
        img = qrcode.make(data)
        img.save(imagename)


    else:
        print("You have to select a valid option")





def main():
    encoder()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('Video', frame)

        code = cv2.waitKey(10)
        if code == ord('q'):
            break


if __name__ == '__main__':
    main()