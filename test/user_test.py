import unittest

from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Userclass
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(128,'Hezron','hezz@gmail.com','12345')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
    

if __name__ == '__main__':
    unittest.main()