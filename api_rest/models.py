from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False, unique=True)
    user_name = models.CharField(max_length=100, default='')
    user_email = models.EmailField(max_length=100, default='')
    user_age = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return f'User: {self.user_name} | Email: {self.user_email} | Age: {self.user_age}'
    
    
