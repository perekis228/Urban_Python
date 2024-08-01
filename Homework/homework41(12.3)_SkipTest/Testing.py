import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_Usain = runner_and_tournament.Runner("Усейн", 10)
        self.runner_Andrey = runner_and_tournament.Runner("Андрей", 9)
        self.runner_Nick = runner_and_tournament.Runner("Ник", 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testUsainNick(self):
        self.tournament = runner_and_tournament.Tournament(90, self.runner_Usain, self.runner_Nick)
        results = self.tournament.start()
        self.assertTrue(results[2] == self.runner_Nick)
        self.all_results.append(results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testAndreyNick(self):
        self.tournament = runner_and_tournament.Tournament(90, self.runner_Andrey, self.runner_Nick)
        results = self.tournament.start()
        self.assertTrue(results[2] == self.runner_Nick)
        self.all_results.append(results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testAndreyUsainNick(self):
        self.tournament = runner_and_tournament.Tournament(90, self.runner_Andrey, self.runner_Usain, self.runner_Nick)
        results = self.tournament.start()
        self.assertTrue(results[3] == self.runner_Nick)
        self.all_results.append(results)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)