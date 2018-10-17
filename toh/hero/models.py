from django.db import models

class Hero(models.Model): # model.Model을 상속함, Django는 자동적으로 'id'라는 column을 만들어 primary key로 삼음
    name = models.CharField(max_length=120) # column(static variable) 생성
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        print("Hello, my name is {} and my score is {}".format(self.name, self.score))

# 1개 database 내 2개 table 됨
class Team(models.Model):
    name = models.CharField(max_length=120)
    
    # ManyToOne, Hero 1개를 가져옴
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE, # leader가 지워지면 team도 지워지게 만듦
        related_name='leader_set', # reverse-lookup: leader인 hero 1명의 team을 반환하며, hero에 저장됨(hero.leader_set)
    )
    # ManyToMany
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name
