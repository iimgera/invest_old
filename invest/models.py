from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    budget = models.DecimalField()
    description = models.TextField()
    financial_data = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class InvestmentRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
