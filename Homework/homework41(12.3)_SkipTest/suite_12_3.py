import unittest
import Test
import Testing

justTest = unittest.TestSuite()
justTest.addTest(unittest.TestLoader().loadTestsFromTestCase(Test.RunnerTest))
justTest.addTest(unittest.TestLoader().loadTestsFromTestCase(Testing.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(justTest)