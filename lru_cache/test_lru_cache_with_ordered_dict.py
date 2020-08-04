import unittest
from lru_cache_with_ordered_dict import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.lru_cache = LRUCache(3)

    def test_items_can_be_added_to_cache(self):
        self.lru_cache.set(1, 500)
        self.lru_cache.set(2, 600)
        self.lru_cache.set(3, 700)

        self.assertEqual(len(self.lru_cache.cache), 3)
        self.assertEqual(self.lru_cache.get(1), 500)
        self.assertEqual(self.lru_cache.get(2), 600)
        self.assertEqual(self.lru_cache.get(3), 700)

    def test_values_are_updated_when_key_already_exists(self):
        self.lru_cache.set(1, 800)
        self.lru_cache.set(1, 900)
        self.lru_cache.set(2, 1000)
        self.lru_cache.set(2, 1100)
        self.lru_cache.set(3, 1200)
        self.lru_cache.set(1, 1300)
        self.lru_cache.set(3, 1400)

        self.assertEqual(len(self.lru_cache.cache), 3)

        self.assertNotEqual(self.lru_cache.get(1), 800)
        self.assertNotEqual(self.lru_cache.get(1), 900)
        self.assertNotEqual(self.lru_cache.get(2), 1000)
        self.assertNotEqual(self.lru_cache.get(3), 1200)

        self.assertEqual(self.lru_cache.get(1), 1300)
        self.assertEqual(self.lru_cache.get(2), 1100)
        self.assertEqual(self.lru_cache.get(3), 1400)

    def test_entries_are_overwritten_when_cache_is_at_capacity(self):
        self.assertEqual(self.lru_cache.get(1), -1)
        self.assertEqual(self.lru_cache.get(2), -1)
        self.assertEqual(self.lru_cache.get(3), -1)
        self.assertEqual(self.lru_cache.get(4), -1)

        self.lru_cache.set(1, 500)
        self.lru_cache.set(2, 600)
        self.lru_cache.set(3, 700)
        self.lru_cache.set(4, 800)

        self.assertEqual(len(self.lru_cache.cache), 3)

        self.assertEqual(self.lru_cache.get(1), -1)
        self.assertEqual(self.lru_cache.get(2), 600)
        self.assertEqual(self.lru_cache.get(3), 700)
        self.assertEqual(self.lru_cache.get(4), 800)

        self.lru_cache.set(5, 900)

        self.assertEqual(len(self.lru_cache.cache), 3)

        self.assertEqual(self.lru_cache.get(1), -1)
        self.assertEqual(self.lru_cache.get(2), -1)
        self.assertEqual(self.lru_cache.get(3), 700)
        self.assertEqual(self.lru_cache.get(4), 800)
        self.assertEqual(self.lru_cache.get(5), 900)


if __name__ == '__main__':
    unittest.main()
