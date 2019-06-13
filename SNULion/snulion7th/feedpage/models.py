from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 자동으로 user.profile이 가능해짐
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    # OneToOneField를 사용하여 User과 Profile를 연결시켰지만, User 객체가 생성되면 자동으로 이와 연결된 Profile 객체가 생성되지는 않습니다.

    def __str__(self):
        return 'id=%d, user id=%d, college=%s, major=%s' % (self.id, self.user.id, self.college, self.major)
    
    # user.prfile.major 가능함
    # Profile.objects.filter(major="미학과")
    # Profile.objects.filter(is_superuser=True)
    # Profile.objects.exclude(major="미학과")
    # User.objects.filter(profile__college="서울대학교").exclude(profile__major="미학과")

# User 객체가 생성되거나 수정될 때마다, 그에 대응되는 Profile 객체도 자동으로 생성 혹은 수정되도록 하는 함수입니다.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()
# college와 같은 추가적인 필드에 대한 수정은 user.profile.college처럼 가져온 다음 user.save()를 하면 됩니다. 이는 user의 변화를 통해 profile를 수정하는 것입니다.

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
    
class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)