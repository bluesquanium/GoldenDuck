import yaml
import os

# os.getcwd()+"/deployment/conf.yaml"

class Config:
    yamlPath = ""
    dartApiKey = ""

    def __init__(self, yamlPath):
        byte = open(yamlPath, "r")
        y = yaml.load(byte, Loader=yaml.FullLoader)
        self.yamlPath = yamlPath
        self.dartApiKey = y["dart_api_key"]

    def load(self, yamlPath):
        byte = open(yamlPath, "r")
        y = yaml.load(byte, Loader=yaml.FullLoader)
        self.yamlPath = yamlPath
        self.dartApiKey = y["dart_api_key"]

def load(yamlPath):
    return Config(yamlPath)