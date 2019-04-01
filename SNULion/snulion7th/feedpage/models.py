from django.db import models
from django.utils import timezone
from faker import Faker

class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def seed(count):
        myfaker = Faker('ko_KR')
        for i in range(count):
            Feed.objects.create(
                title = myfaker.bs(),
                content = myfaker.text(),
            )

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title