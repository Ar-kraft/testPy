import unittest
from yandex_api import create_folder


class TestFunctions(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_create_folder(self):
        self.assertEqual(create_folder('test_folder'), 201)


if __name__ == '__main__':
    unittest.main()