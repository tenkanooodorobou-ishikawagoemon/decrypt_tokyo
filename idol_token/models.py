from django.db import models

# Create your models here.
class Idol(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField()
    construct_id = models.CharField(max_length = 250)

    def __str__(self):
        return "{0}".format(self.name)

class Idol_Item(models.Model):
    idol = models.ForeignKey(Idol, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 250)
    price = models.IntegerField(default = 0)
    total_issue_value = models.IntegerField(default = 0)

    def __str__(self):
        return "{0}:{1}:{2}:{3}".format(self.idol, self.contents, self.price, self.total_issue_value)
