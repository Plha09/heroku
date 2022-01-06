from django.db import models

# Create your models here.
class Students(models.Model):
	Name = models.CharField(max_length= 100, blank=True)
	College = models.CharField(max_length= 100, blank=True)
	Email = models.CharField(max_length= 100, blank=True)

	def __str__(self):
		return self.Name