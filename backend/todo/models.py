from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    is_completed = models.BooleanField(default=False)

    def mark_as_completed(self):
        self.is_completed = True

    def mark_as_uncompleted(self):
        self.is_completed = False
