from django.db import models

# Create your models here.
class Task(models.Model):
    item_id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=500)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    comp_date = models.DateTimeField('Completion Date')
    STATUS_CHOICES = (
        ('NC', 'Not completed'),
        ('C', 'Completed')
    )
    status = models.CharField(choices=STATUS_CHOICES, default='NC', max_length=20)
