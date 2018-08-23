import requests
import json  
from assets.python.Global import Global

class Ft:
    def __init__(self):
        self.url = Global.URL
        self.header = Global.HEADER
        # TODO: this get url data
        self.data = ""
        # TODO: this get js animator seleium
        self.json = ""

    def setUrl(self,url):
        self.url = url 
        return self
    
    def getUrl(self):
        return self.url 
    
    def getData(self):
        self.data = requests.post(self.url,headers = self.header)
        return self.data.status_code,self.data


    def getJson(self):
        # TODO: the any web's tag to find 
        self.json = self.data.text[1:] 
        self.json = self.json[:-1].split(",")
        
        # TODO: return json
        return self.json
