import os
import tempfile
import unittest

import rnglfg


class RnglfgTests(unittest.TestCase):
    def test_lfg_to_list_returns_requested_count(self):
        numbers = rnglfg.lfgToList(1000, 24, 55)
        self.assertEqual(len(numbers), 1000)
        self.assertTrue(all(isinstance(n, int) for n in numbers))

    def test_lfg_to_file_writes_requested_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "out.dat")
            rnglfg.lfgToFile(4096, 24, 55, path)
            self.assertEqual(os.path.getsize(path), 4096)


if __name__ == "__main__":
    unittest.main()
