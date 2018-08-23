import unittest 
from assets.python.Model import model
from assets.python.Global import Global

class Test(unittest.TestCase):
    
    def setUp(self):
        self.md = model.BuildModel()
        return self
    
    def tearDown(self):
        self.md = None
        return self

    def test_httpStatus(self):
        self.assertEqual(self.md.httpStatus((Global.SUCCESSSTATUS,"123")),True)
        return self

    def test_run(self):
        self.assertEqual(self.md.run(),None)
        return self
         
        
    