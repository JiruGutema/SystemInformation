import unittest
from src.process import get_process_info

class TestProcess(unittest.TestCase):

    def test_get_process_info(self):
        processes = get_process_info()
        self.assertIsInstance(processes, list)
        if processes:
            self.assertIn('pid', processes[0])
            self.assertIn('name', processes[0])
            self.assertIn('cpu_percent', processes[0])
            self.assertIn('memory_percent', processes[0])

if __name__ == '__main__':
    unittest.main()
