from django.db import models
from user.models import User



class Note(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=500)
    entered_time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, related_name="writer",related_query_name="Query_writer", on_delete=models.CASCADE)


    def __str__(self):
        return self.title



