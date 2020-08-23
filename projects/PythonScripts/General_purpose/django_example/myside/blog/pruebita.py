from django.contrib.auth.models import User
from blog.models import Post

all_posts = Post.objects.all()

for item in all_posts:
    print(item)