import unittest
from regex import match


class Test_Program(unittest.TestCase):

    def test_zero_or_more(self):
        test = [
            # regex, string, expected result    
            ('a*', '', True),
            ('a*', 'a', True),
            ('a*', 'b', False),
            ('a*', 'aaaaaa', True),
            ('a*', 'ab', False),
            ('a|b*', '', True),
            ('a|b*', 'bbbc', False),
            ('a|b*', 'bbb', True),
        ]
        
        for t in test:
            self.assertEqual(match(t[0], t[1]),t[2])

    def test_one_or_many(self):
        test = [
            # regex, string, expected result    
            ('a+', '', False),
            ('a+', 'a', True),
            ('a+', 'b', False),
            ('a+', 'aaaaaa', True),
            ('a+', 'ab', False),
            ('a|b+', 'bbbc', False),
            ('a|b+', 'bbb', True),
        ]
        
        for t in test:
            self.assertEqual(match(t[0], t[1]),t[2])


    def test_one_or_none(self):
        test = [
            # regex, string, expected result    
            ('a?', '', True),
            ('a?', 'a', True),
            ('a?', 'b', False),
            ('a?', 'aaaaaa', False),
            ('a?', 'ab', False),
            ('a|b?', '', True),
            ('a|b?', 'bbbc', False),
            ('a|b?', 'b', True),
        ]
        
        for t in test:
            self.assertEqual(match(t[0], t[1]),t[2])


    def test_and(self):
        test = [
            # regex, string, expected result    
            ('a.b', '', False),
            ('a.b', 'a', False),
            ('a.b', 'ab', True),
            ('a.b', 'aaaaaa', False),
            ('aa.bb', 'ab', False),
        ]
        
        for t in test:
            self.assertEqual(match(t[0], t[1]),t[2])


    def test_or(self):
        test = [
            # regex, string, expected result    
            ('a|b', 'a', True),
            ('a|b', 'b', True),
            ('a|b', 'ab', False),
            ('a|b', 'ba', False),
            ('a|b', 'aa', False),
            ('a|b', 'bb', False),
            ('a|b|c', 'a', True),
            ('a|b|c', 'b', True),
            ('a|b|c', 'c', True),
        ]
        
        for t in test:
            self.assertEqual(match(t[0], t[1]),t[2])

