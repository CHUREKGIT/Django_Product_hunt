from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()  
    pub_date = models.DateTimeField()
    votels_total = models.IntegerField(default = 1)
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date_pretty('%b %e %Y')