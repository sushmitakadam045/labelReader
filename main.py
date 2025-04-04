from CodeScanner.capture import captureImage
from CodeScanner.decode import decodeBarOrQRCode
from CodeScanner.getCodeCount import Codes
def main():
    captureImage()
    dataRead = decodeBarOrQRCode("capture1.jpg")
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


if __name__ == "__main__":
    main()