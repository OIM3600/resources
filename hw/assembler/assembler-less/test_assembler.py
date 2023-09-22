import unittest
from assembler import assembler


class TestAssembler(unittest.TestCase):
    def test_case1(self):
        code = '''\
dec 8
inc 7
inc 6
dec 3
inc 8
dec 2'''
        self.assertEqual(assembler(code.splitlines()), 8)

    def test_case2(self):
        code = '''\
inc 7
inc 1
dec 8
inc 8
inc 5
dec 3'''
        self.assertEqual(assembler(code.splitlines()), 10)

    def test_case3(self):
        code = '''\
dec 9
dec 8
dec 6
inc 2
inc 3
inc 10
dec 5
dec 9
dec 4
inc 4
dec 8
inc 2
dec 3
dec 5
dec 10
inc 1
dec 1
inc 7
inc 5
dec 8'''
        self.assertEqual(assembler(code.splitlines()), -42)


if __name__ == '__main__':
    unittest.main()
