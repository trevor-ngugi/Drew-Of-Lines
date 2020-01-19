class Comment:
    all_comments=[]

    def __init__(self,blog_id,blog,comment):#add blog_title
        self.blog_id=blog_id
        self.blog=blog
        self.comment=comment

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_reviews(cls):
        Comment.all_comments.clear()