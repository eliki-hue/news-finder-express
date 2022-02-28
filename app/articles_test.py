import unittest
from models import article

Articles = article.Article

class ChannelTest(unittest.TestCase):
     '''
    Test Class to test the behaviour of the Channel class
    '''

     def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles(1234,'cnn','https://cnn.news','https://image.png','2222-4-5')

     def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()