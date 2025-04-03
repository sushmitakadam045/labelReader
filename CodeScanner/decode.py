from pyzbar.pyzbar import decode
from PIL import Image

def decodeBarOrQRCode(imgPath):
    try:
        img = Image.open(imgPath)
        decodedObjects = decode(img)
        return decodedObjects
    except FileNotFoundError:
        print("File {} not found".format(imgPath))
        return []
    except Exception as e:
        print("Error opening or processing the file {}. Error {} ".format(imgPath, e))
        return []
#print(decodeBarOrQRCode("C:\\Users\\sk6813\\Downloads\\QRCode.png"))