import logging
import unittest
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s \t|\t %(levelname)s \t|\t %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            cur_speed = -10
            self.first_runner = rt_with_exceptions.Runner(name='First', speed=cur_speed)
            for _ in range(10):
                self.first_runner.walk()
            self.assertEqual(self.first_runner.distance, cur_speed, f"Дистанции не равны {self.first_runner.distance} != {cur_speed}")
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            cur_speed = 10
            self.second_runner = rt_with_exceptions.Runner(name=123, speed=cur_speed)
            for _ in range(10):
                self.second_runner.run()
            self.assertEqual(self.second_runner.distance, cur_speed*2, f"Дистанции не равны {self.second_runner.distance} != {cur_speed*2}")
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)