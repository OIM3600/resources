import unittest
from assembler import assembler


class TestSimpleAssembler(unittest.TestCase):
    def test_case1(self):
        code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
        self.assertEqual(assembler(code.splitlines()), {'a': 1})

    def test_case2(self):
        code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
        self.assertEqual(
            assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600}
        )


if __name__ == '__main__':
    unittest.main()
