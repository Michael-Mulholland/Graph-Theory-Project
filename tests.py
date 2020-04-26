import unittest
import regex

class TestProgram(unittest.TestCase):

    def test_check_and(self):
        test = [
            # regex, string, result, message
            ('ab', 'ab', True, 'ab - ab'),
            ('ab', 'abb', False, 'ab - abb'),
            ('ab', 'bb', False, 'ab - bb'),
            ('abcd', 'abcd', True, 'abcd - abcd'),
            ('ab', 'aabb', False, 'ab - aabb'),
            ('ab', '', False, 'ab - NONE'),
            ('a.c', 'abc', True, 'a.c - abc'),
        ]
        nfa = compile()

        for t in test:
            nfa.build(t[0])
            self.assertEqual(t[2], nfa.check(t[1]), t[3])