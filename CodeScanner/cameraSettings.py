import json
import os

class CameraSettingsCls:
    def __init__(self, configFile = ".\\CodeScanner\\config.json"):
        #TODO: make a note of all the config settings you make
        self.defaultConfig = {
            "resolution": {"width": 1280, "height": 720},
            "camera_settings": {
                "brightness": 0.7,
                "contrast": 0.7,
                "saturation": 0.6,
                "gain": 0.7,
                "exposure": 0,
                "fps": 30
            }
        }
        self.configFile = configFile
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.configFile):
            print("Config file does not exit. Using default configurations.")
            config = self.defaultConfig
        else:
            try:
                with open(self.configFile, "r") as file:
                    config = json.load(file)

                if not config:
                    print("File is empty. Using default settings")
                    config = self.defaultConfig

            except json.JSONDecodeError:
                print("Error: Invalid JSON format. Using default settings.")
                config = self.defaultConfig
            except Exception as e:
                print("Exception Caught while reading config file ", e)

            # Load settings with default fallback for each key
            resolution = config.get("resolution", self.defaultConfig["resolution"])
            camera_settings = config.get("camera_settings", self.defaultConfig["camera_settings"])

            self.width = resolution.get("width", 1280)
            self.height = resolution.get("height", 720)

            self.brightness = camera_settings.get("brightness", 0.5)
            self.contrast = camera_settings.get("contrast", 0.5)
            self.saturation = camera_settings.get("saturation", 0.5)
            self.gain = camera_settings.get("gain", 0.5)
            self.exposure = camera_settings.get("exposure", -4)
            self.fps = camera_settings.get("fps", 30)