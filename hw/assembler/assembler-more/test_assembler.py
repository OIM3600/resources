import unittest
from assembler import assembler


class TestAssembler(unittest.TestCase):
    def test_case1(self):
        code = '''\
mov a 5
inc a
dec a
mov b a
dec a
inc b'''
        self.assertEqual(assembler(code.splitlines()), {'a': 4, 'b': 6})

    def test_case2(self):
        code = '''\
mov a 0
inc a
dec a
mov b a
inc b
inc b
inc a
inc b
inc a
dec b
inc b
inc b'''
        self.assertEqual(assembler(code.splitlines()), {'a': 2, 'b': 4})

    def test_case3(self):
        code = '''\
mov c 10
inc c
inc c
mov b 0
inc b
dec b
dec c
mov a b
dec a
dec b
inc a
dec b
dec b
dec b
inc c
dec b
dec a
inc a
dec b
dec c
inc a
dec c
dec c'''
        self.assertEqual(assembler(code.splitlines()), {'a': 1, 'b': -6, 'c': 9})


if __name__ == '__main__':
    unittest.main()
