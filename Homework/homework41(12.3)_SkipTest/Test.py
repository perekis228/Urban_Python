import unittest
import main

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(self):
        self.test_walker = main.Student('Walker')
        self.test_runner = main.Student('Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test50m(self):
        for _ in range(10):
            self.test_walker.walk()
        self.assertEqual(self.test_walker.distance, 50, f"Дистанции не равны {self.test_walker.distance} != 50")
        self.test_walker.distance = 0

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test100m(self):
        for _ in range(10):
            self.test_runner.run()
        self.assertEqual(self.test_runner.distance, 100, f"Дистанции не равны {self.test_runner.distance} != 100")
        self.test_runner.distance = 0

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRunAndWalk(self):
        for _ in range(10):
            self.test_walker.walk()
            self.test_runner.run()
        self.assertGreater(self.test_runner.distance, self.test_walker.distance, f"{self.test_runner} должен преодолеть дистанцию больше, чем {self.test_walker}")