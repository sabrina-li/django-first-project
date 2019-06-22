from django.db import models

# Create your models here.

class Notes(models.Model):
    note_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.note_text

    def get_pub_date(self):
        return self.pub_date
