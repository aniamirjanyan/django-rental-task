from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=30)

    def get_name(self):
        return self.name

    def get_id(self):
        return str(self.id)
