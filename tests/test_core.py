import unittest,copy,json
from synthetic_neighbor_distance import run
DEMO={'source': [{'id': 'a', 'values': [10, 100]}, {'id': 'b', 'values': [20, 200]}], 'synthetic': [{'id': 'copy', 'values': [10, 100]}, {'id': 'close', 'values': [10.1, 101]}], 'scales': [10, 100]}
class DomainTests(unittest.TestCase):
 def test_copy_and_close_neighbor(self):
  x=run(DEMO)['rows'];self.assertTrue(x[0]['exact_copy']);self.assertFalse(x[1]['exact_copy']);self.assertTrue(x[1]['near']);self.assertAlmostEqual(x[1]['nearest_distance'],.01)
 def test_scales_are_explicit(self):
  x=run(DEMO);self.assertFalse(x['scales_fitted_from_data']);self.assertFalse(x['privacy_guaranteed'])
 def test_empty_source_not_privacy_success(self):
  with self.assertRaises(ValueError):run(dict(DEMO,source=[]))
