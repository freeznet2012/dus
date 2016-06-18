from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class University(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
	

class Semester(models.Model):
	name = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
	college = models.CharField(max_length=50)
	university = models.ForeignKey(University)
	department = models.ForeignKey(Department)
	semester = models.ForeignKey(Semester, null=True)
	group = models.ForeignKey(Group)

	def __str__(self):
		return self.name
	
