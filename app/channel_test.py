import unittest
from models import channel

Channel = channel.Channel

class ChannelTest(unittest.TestCase):
     '''
    Test Class to test the behaviour of the Channel class
    '''

     def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_channel = Channel(1234,'cnn','an international news source','https://cnn.news','politics','us')

     def test_instance(self):
        self.assertTrue(isinstance(self.new_channel,Channel))


if __name__ == '__main__':
    unittest.main()
