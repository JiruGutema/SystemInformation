import unittest
from src.stats import get_system_stats

class TestStats(unittest.TestCase):

    def test_get_system_stats(self):
        stats = get_system_stats()
        self.assertIn('cpu_usage', stats)
        self.assertIn('memory_total', stats)
        self.assertIn('memory_used', stats)
        self.assertIn('disk_total', stats)
        self.assertIn('network_sent', stats)

if __name__ == '__main__':
    unittest.main()
