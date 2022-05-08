import unittest

from app.models import Comment

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Commentclass
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Comment = Comment(123,'Hezron','Its cool')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_Comment,Comment))
    

if __name__ == '__main__':
    unittest.main()