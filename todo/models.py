from django.db import models
from django.contrib.auth.models import User

# # Profile Model
# class Profile(models.Model):
# 	profile_pic = models.TextField()
# 	bio = models.TextField(default="")
# 	website = models.TextField()
# 	saved = models.TextField()
# 	downloaded = models.TextField()
# 	user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')

# Post Model
class Post(models.Model):
	title = models.TextField()
	description = models.TextField(default="")
	keywords = models.TextField()
	source = models.TextField()
	dataset = models.FileField()
	data_crop_html = models.TextField()
	data_html = models.TextField()

	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')

# class UserSettings(models.Model):
# 	profile_pic = models.ImageField(upload_to='profile', default='http://s3.amazonaws.com/37assets/svn/765-default-avatar.png')
# 	name = models.TextField(default="")
# 	bio = models.TextField(default="")
# 	website = models.TextField(default="")
# 	saved = models.TextField(default="")
# 	downloaded = models.TextField(default="")

# 	poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_attributes')