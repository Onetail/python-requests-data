from assets.python.Global import Global
from assets.python.Model import Feature 

class BuildModel:
    def __init__(self):
        self.Ft = Feature.Ft()
        self.url = None
        
    def httpStatus(self,data):
        status , self.url = data 
        return status == Global.SUCCESSSTATUS 

    def run(self):
        if self.httpStatus(self.Ft.getData()):
            print(self.url.text)
        else :
            print("The web have something wrong!")
        
        print(self.Ft.getJson())
        return 
