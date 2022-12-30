import os
import unittest

from app.main import downdload_txt_to_file


class MainTest(unittest.TestCase):

    def test_download_txt_to_file(self):
        downdload_txt_to_file(
            "https://raw.githubusercontent.com/TrisNol/sample-python-repo/main/requirements.txt", "./temp.txt")

        self.assertTrue(os.path.exists("./temp.txt"))
