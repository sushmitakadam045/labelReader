from sys import exception

import cv2

from CodeScanner.capture import captureImage
from CodeScanner.decode import decodeBarOrQRCode
from CodeScanner.getCodeCount import Codes
import ObjDetection.findLabel as findLabel
import time

def main():
    i = 0
    while True:
        time.sleep(0.5)
        try:
            if i % 2 == 0:
                frame = captureImage()
                x, y, w, h = findLabel.detect_sticker_label(frame)
                if None in (x, y, w, h):
                    print("No label detected")
                    cv2.imshow(
                        "No label detected", frame
                    )
                    i = i + 1
                    continue

                roi = frame[y:y + h, x:x + w]
                dataRead = decodeBarOrQRCode(roi)
                currQRCount  = currBarCount = 0

                codeCounts = Codes()
                if not len(dataRead):
                    print("Empty image captured")
                else:
                    print(dataRead)
                    for data in dataRead:
                        if data.type == "QRCODE":
                            currQRCount = currQRCount + 1
                        elif data.type in ["EAN13", "EAN8", "UPC_A", "UPC_E", "CODE128", "CODE39", "ITF", "CODABAR"]:
                            currBarCount = currBarCount + 1

                if codeCounts.QRCodeCount == currQRCount:
                    print("QR count matches")
                else:
                    print(f"Error in QR counts specified in config.json and the read image. Config.json count = {codeCounts.QRCodeCount} and current count = {currQRCount}")

                if codeCounts.barCodeCount == currBarCount:
                    print("Bar Code count matches")
                else:
                    print(f"Error in Bar code counts specified in config.json and the read image. Config.json count = {codeCounts.QRCodeCount} and current count = {currQRCount}")
        except Exception as e:
            print("Exception caught in main = ", e)
        i = i + 1
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()