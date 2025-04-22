import unittest

from llm_context_length import str_to_tokens, str_to_processing_tokens

ATOMIC_TOKEN = 'fuse'

class TestLib(unittest.TestCase):

    def test_str_to_tokens(self):
        self.assertEqual(str_to_tokens(ATOMIC_TOKEN * 10), 10.0)

    def test_str_to_processing_tokens(self):
        self.assertEqual(str_to_processing_tokens('Webfuse is the world\'s first web augmentation platform.'), 9)
