from django.db import models

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return str(self.id)+" "+ self.name
