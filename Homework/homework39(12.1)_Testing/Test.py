import unittest
import main

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_walker = main.Student('Walker')
        self.test_runner = main.Student('Runner')

    def test1(self):
        for _ in range(10):
            self.test_walker.walk()
        self.assertEqual(self.test_walker.distance, 50, f"Дистанции не равны {self.test_walker.distance} != 50")
        self.test_walker.distance = 0

    def test2(self):
        for _ in range(10):
            self.test_runner.run()
        self.assertEqual(self.test_runner.distance, 100, f"Дистанции не равны {self.test_runner.distance} != 100")
        self.test_runner.distance = 0

    def test3(self):
        for _ in range(10):
            self.test_walker.walk()
            self.test_runner.run()
        self.assertGreater(self.test_runner.distance, self.test_walker.distance, f"{self.test_runner} должен преодолеть дистанцию больше, чем {self.test_walker}")