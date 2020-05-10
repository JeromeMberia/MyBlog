import unittest
from app.models import Post

class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.new_post = Post(id = 1, title ='cool' ,content='It boring' ,user_id= 2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_variables(self):
        self.assertEquals(self.new_post.id, 1)
        self.assertEquals(self.new_post.title, 'cool')
        self.assertEquals(self.new_post.content, 'It boring')
        self.assertEquals(self.new_post.user_id, 2)