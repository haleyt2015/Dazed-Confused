from datetime import date
from datetime import datetime
from django.db import models

class SearchInput(models.Model):
	input = models.CharField(max_length=250)

	class Meta:
		managed = True
