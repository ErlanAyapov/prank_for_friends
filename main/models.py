from django.db import models


class Account(models.Model):

	login = models.CharField('Логин ', max_length = 20)
	password = models.CharField('Пороль ', max_length = 20)

	def __str__(self):
		return self.login + ' | ' + self.password