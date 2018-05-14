import unittest
from main import comparefile
class TestComapreFile(unittest.TestCase):

    # def test_ExtesionCompare(self):
    #     result=comparefile('.\\testdata\\target').split('\n')
    #     for i in range(len(result)):
    #         if len(result[i]) and i==0:
    #             print(i)
    #             words=result[i].split(" ")
    #             print(words)
    #             self.assertTrue(words[0].endswith("test1.bak"))
    #             self.assertTrue(words[-1].endswith("test1.txt"))
                
    def test_DirectionCompare(self):
        result=comparefile('.\\testdata').split('\n')
        for i in range(len(result)):
            if len(result[i]):
                words=result[i].split(" ")
                if i==0:
                    self.assertTrue(words[0].endswith("test1.bak"))
                    self.assertTrue(words[-1].endswith("test1.txt"))
                elif i==1:
                    self.assertTrue(words[0].endswith("source\\test1.txt"))
                    self.assertTrue(words[-1].endswith("target\\test1.txt"))

if __name__=='__main__':
    unittest.main()