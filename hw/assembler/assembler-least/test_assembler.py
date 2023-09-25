import unittest
from assembler import assembler


class TestAssembler(unittest.TestCase):
    def test_case1(self):
        code = '''\
dec
inc
dec
dec
dec
inc'''
        self.assertEqual(assembler(code.splitlines()), -2)

    def test_case2(self):
        code = '''\
inc
dec
inc
inc
dec
dec'''
        self.assertEqual(assembler(code.splitlines()), 0)

    def test_case3(self):
        code = '''\
dec
dec
inc
dec
inc
dec
dec
inc
inc
dec
dec
inc
inc
inc
inc
inc
inc
inc
dec
dec'''
        self.assertEqual(assembler(code.splitlines()), 2)


if __name__ == '__main__':
    unittest.main()
