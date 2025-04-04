import json
import os
class Codes:
    def __init__(self, configFile = ".\\CodeScanner\\config.json"):
        defaultCodes = {"QR": 2, "bar": 3}
        if not os.path.exists(configFile):
            print("Config file does not exist. Using default configurations.")
            self.QRCodeCount  = defaultCodes["QR"]
            self.barCodeCount = defaultCodes["bar"]
        else:
            try:
                with open(configFile, "r") as file:
                    config = json.load(file)

                if not config:
                    print("File is empty. Using default settings")
                code = config.get("codeCount", defaultCodes)
                self.QRCodeCount  = config.get(code.get("QR"), defaultCodes["QR"])
                self.barCodeCount = config.get(code.get("bar"), defaultCodes["bar"])
            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Using default settings.")
            except Exception as e:
                print("Exception Caught while reading config file ", e)
        print(self.QRCodeCount, self.barCodeCount)
