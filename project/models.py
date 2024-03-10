from django.db import models


class Character(models.Model):
  name = models.CharField(max_length=60)
  status = models.CharField(max_length=30)
  species = models.CharField(max_length=60)
  char_type = models.CharField(max_length=80)
  gender = models.CharField(max_length=30)
  image = models.TextField()

  def __str__(self) -> str:
    return f"{self.name} - {self.status}"
