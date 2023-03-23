from HTMLTestRunner import HTMLTestRunner
import unittest
from MyTest.myTest import  SercheTest

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SercheTest)

        ])

        outfile = open("SmokeTest.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)