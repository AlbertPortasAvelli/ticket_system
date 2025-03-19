from django.db import models

class Ticket(models.Model):
    
    title= models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Open')
    
    def __str__(self):
        return self.title

