import unittest

from app.models import Blog,User,Comment
from app import db

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(id=1,blog_title='Test_post',blog_content='Test_content', blog_author='olga')


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title,'Test_post')
        self.assertEquals(self.new_blog.blog_content,'Test_content')

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blogs(self):
        self.new_blog.save_blog()
        saved_blog = blog.get_blogs()
        self.assertTrue(saved_blog is not None)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        blog = Blog.get_single_blog(1)
        self.assertTrue(blog is not None)
