from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    location = models.CharField(max_length=300)
    date = models.DateField()
    Ramdan_day = models.IntegerField()

    def __str__(self):
        return self.name


class ActivityParticipant(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name='participants',
    )
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.activity.name}'
