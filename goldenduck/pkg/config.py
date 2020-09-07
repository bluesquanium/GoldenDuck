import yaml
import os

class Config:
    yamlPath = ""
    dartApiKey = ""
    outputDir = ""

    #MYSQL
    mysqlHost = ""
    mysqlPort = ""
    mysqlUser = ""
    mysqlPassword = ""
    mysqlDatabase = ""
    mysqlTable = ""
    mysqlCorplistTable = ""

    def __init__(self, yamlPath):
        byte = open(yamlPath, "r")
        y = yaml.load(byte, Loader=yaml.FullLoader)
        self.yamlPath = yamlPath
        self.dartApiKey = y["dart_api_key"]
        self.outputDir = y["output_dir"]
        self.mysqlHost = y["mysql_host"]
        self.mysqlPort = y["mysql_port"]
        self.mysqlUser = y["mysql_user"]
        self.mysqlPassword = y["mysql_password"]
        self.mysqlDatabase = y["mysql_database"]
        self.mysqlTable = y["mysql_table"]
        self.mysqlCorplistTable = y["mysql_corplist_table"]

    def load(self, yamlPath):
        byte = open(yamlPath, "r")
        y = yaml.load(byte, Loader=yaml.FullLoader)
        self.yamlPath = yamlPath
        self.dartApiKey = y["dart_api_key"]
        self.outputDir = y["output_dir"]
        self.mysqlHost = y["mysql_host"]
        self.mysqlPort = y["mysql_port"]
        self.mysqlUser = y["mysql_user"]
        self.mysqlPassword = y["mysql_password"]
        self.mysqlDatabase = y["mysql_database"]
        self.mysqlTable = y["mysql_table"]
        self.mysqlCorplistTable = y["mysql_corplist_table"]

def load(yamlPath):
    return Config(yamlPath)