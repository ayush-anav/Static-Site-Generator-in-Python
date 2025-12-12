import unittest
from blocktype import BlockType, block_to_block_type

class Test_Block_Type(unittest.TestCase):
    def test_block_type(self):
        expected = BlockType.CODE
        actual = block_to_block_type("```code```")
        self.assertEqual(expected, actual)