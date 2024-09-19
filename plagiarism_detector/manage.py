#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PlagiarismResult(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    similarity_score = models.FloatField()
    compared_with = models.TextField()
    checked_at = models.DateTimeField(auto_now_add=True)


