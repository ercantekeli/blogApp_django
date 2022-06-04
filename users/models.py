from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, blank=True, null=True)
    # email = models. EmailField(null=True, blank=True)
    image = models.ImageField(upload_to = 'media/', blank=True, null=True, default='media/default-avatar.png')
    bio = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.username



    