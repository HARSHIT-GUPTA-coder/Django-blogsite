from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	heading = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default = timezone.now())
	body= models.TextField()
	def __str__(self):
		return  self.heading
	def get_absolute_url(self):
		return reverse('dash')