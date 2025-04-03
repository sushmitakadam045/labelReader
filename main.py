from CodeScanner.capture import captureImage
from CodeScanner.decode import decodeBarOrQRCode
def main():
    captureImage()
    dataRead = decodeBarOrQRCode("capture1.jpg")
    if not len(dataRead):
        print("Empty image captured")
    else:
        print(dataRead)

if __name__ == "__main__":
    main()