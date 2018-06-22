import unittest
import diskspace

from diskspace import bytes_to_readable
from diskspace import subprocess_check_output
from diskspace import show_space_list

class diskspaceTest(unittest.TestCase):

    def setUp(self):
        self.command = 'du '
        self.abs_directory = os.path.abspath('.')
        self.command += self.abs_directory
        self.path = 'home/teste'


    def test_bytes_to_readable(self):
        blocks = 250
        result = "50.00Kb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_subprocess_check_output(self):
        command = 'du'
        du_result = subprocess.check_output(command)
        result = subprocess_check_output(command)
        self.assertEqual(du_result, result)

     def test_show_space_list(self):
        self.assertIsNone(show_space_list(directory = '.', depth = 0, order=True))
        result = unittest.TestLoader().loadTestsFromTestCase(TestDiskspace)
        unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
    unittest.main()
