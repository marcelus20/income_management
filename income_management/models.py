from django.db import models

from django.contrib.auth.models import User




class Description(models.Model):
    name = models.CharField(max_length=100)
    brief_description = models.CharField(max_length=500)

    def __str__(self):
        return '{} {}'.format(self.name, self.brief_description)




# Create your models here.
class Users(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)


    def __str__(self):
        return self.username






class Transactions(models.Model):
    date = models.DateTimeField(auto_now=True)
    income = models.FloatField(default=0)
    expense = models.FloatField(default=0)
    diary_balance = models.FloatField(default=0)
    total_balance = models.FloatField(default=0)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'\
            .format(self.date, self.income, self.expense, self.diary_balance, self.total_balance, self.description)



